"""
TextLens - AI-Powered OCR Application

Main entry point for the application.
"""

import os
import time
from threading import Thread

import gradio as gr
import spaces
import torch
from PIL import Image

from transformers import (
    Qwen2VLForConditionalGeneration,
    Qwen2_5_VLForConditionalGeneration,
    AutoProcessor,
    TextIteratorStreamer,
)

# Constants for text generation
MAX_MAX_NEW_TOKENS = 2048
DEFAULT_MAX_NEW_TOKENS = 1024
MAX_INPUT_TOKEN_LENGTH = int(os.getenv("MAX_INPUT_TOKEN_LENGTH", "4096"))

device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")

# Load RolmOCR
MODEL_ID_M = "reducto/RolmOCR"
processor_m = AutoProcessor.from_pretrained(MODEL_ID_M, trust_remote_code=True)
model_m = Qwen2_5_VLForConditionalGeneration.from_pretrained(
    MODEL_ID_M,
    trust_remote_code=True,
    torch_dtype=torch.float16 if torch.cuda.is_available() else torch.float32
).to(device).eval()

# Load Qwen2-VL-OCR-2B-Instruct
MODEL_ID_X = "prithivMLmods/Qwen2-VL-OCR-2B-Instruct"
processor_x = AutoProcessor.from_pretrained(MODEL_ID_X, trust_remote_code=True)
model_x = Qwen2VLForConditionalGeneration.from_pretrained(
    MODEL_ID_X,
    trust_remote_code=True,
    torch_dtype=torch.float16 if torch.cuda.is_available() else torch.float32
).to(device).eval()

# Load Nanonets-OCR-s
MODEL_ID_V = "nanonets/Nanonets-OCR-s"
processor_v = AutoProcessor.from_pretrained(MODEL_ID_V, trust_remote_code=True)
model_v = Qwen2_5_VLForConditionalGeneration.from_pretrained(
    MODEL_ID_V,
    trust_remote_code=True,
    torch_dtype=torch.float16 if torch.cuda.is_available() else torch.float32
).to(device).eval()

@spaces.GPU
def generate_ocr(model_name: str, text: str, image: Image.Image,
                 max_new_tokens: int = 1024,
                 temperature: float = 0.6,
                 top_p: float = 0.9,
                 top_k: int = 50,
                 repetition_penalty: float = 1.2):
    """
    Generates OCR responses using the selected model for image input.
    """
    if model_name == "RolmOCR":
        processor = processor_m
        model = model_m
    elif model_name == "Qwen2-VL-OCR-2B-Instruct":
        processor = processor_x
        model = model_x
    elif model_name == "Nanonets-OCR-s":
        processor = processor_v
        model = model_v
    else:
        yield "Invalid model selected."
        return

    if image is None:
        yield "Please upload an image."
        return

    # Default OCR prompt if none provided
    if not text.strip():
        text = "Extract all text from this image"

    messages = [{
        "role": "user",
        "content": [
            {"type": "image", "image": image},
            {"type": "text", "text": text},
        ]
    }]
    
    prompt_full = processor.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)
    inputs = processor(
        text=[prompt_full],
        images=[image],
        return_tensors="pt",
        padding=True,
        truncation=False,
        max_length=MAX_INPUT_TOKEN_LENGTH
    ).to(device)
    
    streamer = TextIteratorStreamer(processor, skip_prompt=True, skip_special_tokens=True)
    generation_kwargs = {**inputs, "streamer": streamer, "max_new_tokens": max_new_tokens}
    
    thread = Thread(target=model.generate, kwargs=generation_kwargs)
    thread.start()
    
    buffer = ""
    for new_text in streamer:
        buffer += new_text
        buffer = buffer.replace("<|im_end|>", "")
        time.sleep(0.01)
        yield buffer

# Define examples for image OCR
image_examples = [
    ["Extract all text from this image", None],
    ["Perform OCR and format as markdown", None],
    ["Extract text and convert to JSON format", None],
    ["OCR this document and preserve formatting", None],
    ["Extract structured data from this form", None]
]

css = """
.submit-btn {
    background-color: #2980b9 !important;
    color: white !important;
}
.submit-btn:hover {
    background-color: #3498db !important;
}
.container {
    max-width: 1200px;
    margin: auto;
}
"""

# Create the Gradio Interface
with gr.Blocks(css=css, theme="bethecloud/storj_theme") as demo:
    gr.Markdown("# 🔍 **TextLens - AI-Powered OCR**")
    gr.Markdown("### Extract text from images using state-of-the-art vision-language models")
    
    with gr.Row():
        with gr.Column(scale=1):
            gr.Markdown("### 📁 Image Input")
            image_query = gr.Textbox(
                label="OCR Instructions", 
                placeholder="Extract all text from this image",
                value="Extract all text from this image",
                lines=2
            )
            image_upload = gr.Image(
                type="pil", 
                label="Upload Image for OCR",
                sources=["upload", "clipboard"]
            )
            image_submit = gr.Button("🚀 Extract Text", elem_classes="submit-btn", variant="primary", size="lg")
            
            gr.Examples(
                examples=image_examples,
                inputs=[image_query, image_upload],
                label="💡 Try these examples"
            )
            
            with gr.Accordion("⚙️ Advanced Options", open=False):
                max_new_tokens = gr.Slider(
                    label="Max new tokens", 
                    minimum=1, 
                    maximum=MAX_MAX_NEW_TOKENS, 
                    step=1, 
                    value=DEFAULT_MAX_NEW_TOKENS
                )
                temperature = gr.Slider(
                    label="Temperature", 
                    minimum=0.1, 
                    maximum=4.0, 
                    step=0.1, 
                    value=0.6
                )
                top_p = gr.Slider(
                    label="Top-p (nucleus sampling)", 
                    minimum=0.05, 
                    maximum=1.0, 
                    step=0.05, 
                    value=0.9
                )
                top_k = gr.Slider(
                    label="Top-k", 
                    minimum=1, 
                    maximum=1000, 
                    step=1, 
                    value=50
                )
                repetition_penalty = gr.Slider(
                    label="Repetition penalty", 
                    minimum=1.0, 
                    maximum=2.0, 
                    step=0.05, 
                    value=1.2
                )
        
        with gr.Column(scale=1):
            gr.Markdown("### 📄 OCR Results")
            output = gr.Textbox(
                label="Extracted Text", 
                interactive=False, 
                lines=15,
                max_lines=25,
                placeholder="Extracted text will appear here...\n\n• Upload an image to get started\n• Results will stream in real-time\n• Use the copy button to copy results",
                show_copy_button=True
            )
            
            model_choice = gr.Radio(
                choices=["Nanonets-OCR-s", "Qwen2-VL-OCR-2B-Instruct", "RolmOCR"],
                label="🤖 Select OCR Model",
                value="Nanonets-OCR-s",
                info="Choose the best model for your OCR task"
            )
            
            with gr.Accordion("📚 Model Information", open=False):
                gr.Markdown("""
                **🔥 Nanonets-OCR-s**: State-of-the-art image-to-markdown OCR model that goes beyond traditional text extraction. Transforms documents into structured markdown with intelligent content recognition and semantic tagging.
                
                **🚀 Qwen2-VL-OCR-2B-Instruct**: Fast general-purpose OCR model fine-tuned for optical character recognition, image-to-text conversion, and math problem solving with LaTeX formatting.
                
                **📄 RolmOCR**: Specialized model designed for parsing complex documents, including scanned documents, handwritten text, and complex layouts. Better for structured documents and tables.
                """)

    # Event handlers
    image_submit.click(
        fn=generate_ocr,
        inputs=[model_choice, image_query, image_upload, max_new_tokens, temperature, top_p, top_k, repetition_penalty],
        outputs=output,
        show_progress="hidden"
    )
    
    # Auto-process on image upload
    image_upload.upload(
        fn=generate_ocr,
        inputs=[model_choice, image_query, image_upload, max_new_tokens, temperature, top_p, top_k, repetition_penalty],
        outputs=output,
        show_progress="hidden"
    )

if __name__ == "__main__":
    print("🚀 Starting TextLens OCR application...")
    print("📊 Loading models - this may take a few minutes on first run...")
    print(f"🔧 Device: {device}")
    print("✅ Models loaded successfully!")
    
    demo.queue(max_size=20).launch(
        share=False,
        server_name="0.0.0.0",
        server_port=7860,
        show_error=True,
        debug=False
    ) 