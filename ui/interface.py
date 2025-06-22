"""
Gradio interface for TextLens OCR application.
"""

import gradio as gr
from .styles import get_custom_css
from .handlers import extract_text_from_image, get_model_status

def create_interface():
    """Create and configure the Gradio interface."""
    
    with gr.Blocks(css=get_custom_css(), title="TextLens - AI OCR", theme=gr.themes.Soft()) as interface:
        # Header
        with gr.Row():
            gr.HTML("""
                <div class="header">
                    <h1>🔍 TextLens - AI-Powered OCR</h1>
                    <p style="margin: 10px 0; font-size: 18px;">
                        Extract text from images using Microsoft Florence-2 Vision-Language Model
                    </p>
                    <p style="margin: 5px 0; opacity: 0.9;">
                        Supports multiple image formats • GPU accelerated • High accuracy
                    </p>
                </div>
            """)
        
        # Model status
        with gr.Row():
            with gr.Column():
                model_status = gr.Markdown(
                    value=get_model_status(),
                    elem_classes=["status-box"]
                )
                refresh_status_btn = gr.Button("🔄 Refresh Status", size="sm")
        
        # Main interface
        with gr.Row():
            with gr.Column(scale=1):
                gr.Markdown("### 📁 Upload Image", elem_classes=["markdown-text"])
                image_input = gr.Image(
                    label="Drop image here or click to upload",
                    type="pil",
                    sources=["upload", "webcam", "clipboard"],
                    elem_classes=["upload-box"]
                )
                
                extract_btn = gr.Button(
                    "🚀 Extract Text", 
                    variant="primary",
                    size="lg"
                )
                
                # gr.Markdown("### 📖 Try with examples:", elem_classes=["markdown-text"])
                # gr.Markdown("""
                #     **Try uploading an image with text:**
                #     • Screenshots of documents
                #     • Photos of signs or billboards
                #     • Handwritten notes  
                #     • Menu cards or receipts
                #     • Book pages or articles
                # """, elem_classes=["markdown-text"])
            
            with gr.Column(scale=1):
                gr.Markdown("### 📝 Extracted Text", elem_classes=["markdown-text"])
                text_output = gr.Textbox(
                    label="Text Output",
                    lines=15,
                    max_lines=25,
                    placeholder="Extracted text will appear here...\n\n• Upload an image to get started\n• The first run may take a few minutes to download the model\n• Subsequent runs will be much faster",
                    show_copy_button=True
                )
                
                # gr.Markdown("""
                #     **💡 Tips:**
                #     - Higher resolution images generally give better results
                #     - Ensure text is clearly visible and not blurry
                #     - The model works best with printed text but also supports handwriting
                #     - First-time model loading may take 2-3 minutes
                #     """,
                #     elem_classes=["tips-section"]
                # )
        
        # # Usage instructions
        # with gr.Row():
        #     gr.Markdown("""
        #         ### 🔧 How to Use
                
        #         1. **Upload an Image**: Drag and drop, use webcam, or paste from clipboard
        #         2. **Extract Text**: Click the "Extract Text" button or text extraction will start automatically
        #         3. **Copy Results**: Use the copy button to copy extracted text
        #         4. **Try Different Images**: Upload multiple images to test various scenarios
                
        #         ### ⚡ Features
                
        #         - **Vision-Language Model**: Uses Microsoft Florence-2 for accurate text recognition
        #         - **Multiple Input Methods**: Upload files, use webcam, or paste from clipboard  
        #         - **Auto-Processing**: Text extraction starts automatically when you upload an image
        #         - **GPU Acceleration**: Automatically uses GPU if available for faster processing
        #         - **Copy Functionality**: Easy one-click copying of extracted text
        #         """, elem_classes=["instructions-section"])
        
        # Event handlers
        image_input.upload(
            fn=extract_text_from_image,
            inputs=image_input,
            outputs=text_output,
            api_name="extract_on_upload"
        )
        
        extract_btn.click(
            fn=extract_text_from_image,
            inputs=image_input,
            outputs=text_output,
            api_name="extract_on_click"
        )
        
        refresh_status_btn.click(
            fn=get_model_status,
            outputs=model_status
        )
    
    return interface 