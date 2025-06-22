---
title: TextLens - AI-Powered OCR
emoji: 🔍
colorFrom: blue
colorTo: purple
sdk: gradio
sdk_version: 4.0.0
app_file: app.py
pinned: false
license: mit
---

# 🔍 TextLens - AI-Powered OCR

A modern Vision-Language Model (VLM) based OCR application that extracts text from images using Microsoft Florence-2 model with intelligent fallback systems.

## ✨ Features

- **🤖 Advanced VLM OCR**: Uses Microsoft Florence-2 for state-of-the-art text extraction
- **🔄 Smart Fallback System**: Automatically falls back to EasyOCR if Florence-2 fails
- **🧪 Demo Mode**: Test mode for demonstration when other methods are unavailable
- **🎨 Modern UI**: Clean, responsive Gradio interface with excellent UX
- **📱 Multiple Input Methods**: Upload, webcam, clipboard support
- **⚡ Real-time Processing**: Automatic text extraction on image upload
- **📋 Copy Functionality**: Easy text copying from results
- **🚀 GPU Acceleration**: Supports CUDA, MPS, and CPU inference
- **🛡️ Error Handling**: Robust error handling and user-friendly messages

## 🏗️ Architecture

```
textlens-ocr/
├── app.py                 # Main Gradio application
├── requirements.txt       # Python dependencies
├── README.md             # Project documentation
├── models/               # OCR processing modules
│   ├── __init__.py
│   └── ocr_processor.py  # Advanced OCR class with fallbacks
├── utils/                # Utility functions
│   ├── __init__.py
│   └── image_utils.py    # Image preprocessing utilities
└── ui/                   # User interface components
    ├── __init__.py
    ├── interface.py      # Gradio interface
    ├── handlers.py       # Event handlers
    └── styles.py         # CSS styling
```

## 🚀 Quick Start

### Local Development

1. **Clone the repository**

   ```bash
   git clone https://github.com/KumarAmrit30/textlens-ocr.git
   cd textlens-ocr
   ```

2. **Set up Python environment**

   ```bash
   python3 -m venv textlens_env
   source textlens_env/bin/activate  # On Windows: textlens_env\Scripts\activate
   ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application**

   ```bash
   python app.py
   ```

5. **Open your browser**
   Navigate to `http://localhost:7860`

### Quick Test

Run the test suite to verify everything works:

```bash
python test_ocr.py
```

## 🔧 Technical Details

### OCR Processing Pipeline

1. **Primary**: Microsoft Florence-2 VLM

   - State-of-the-art vision-language model
   - Supports both basic OCR and region-based extraction
   - GPU accelerated inference

2. **Fallback**: EasyOCR

   - Traditional OCR with good accuracy
   - Works when Florence-2 fails to load
   - Multi-language support

3. **Demo Mode**: Test Mode
   - Demonstration functionality
   - Shows interface working correctly
   - Used when other methods are unavailable

### Model Loading Strategy

The application uses an intelligent loading strategy:

```python
try:
    # Try Florence-2 with specific revision
    model = AutoModelForCausalLM.from_pretrained(
        "microsoft/Florence-2-base",
        revision='refs/pr/6',
        trust_remote_code=True
    )
except:
    # Fall back to default Florence-2
    model = AutoModelForCausalLM.from_pretrained(
        "microsoft/Florence-2-base",
        trust_remote_code=True
    )
```

### Device Detection

Automatically detects and uses the best available device:

- **CUDA**: NVIDIA GPUs with CUDA support
- **MPS**: Apple Silicon Macs (M1/M2/M3)
- **CPU**: Fallback for all systems

## 📊 Performance

| Model            | Size   | Speed  | Accuracy  | Use Case              |
| ---------------- | ------ | ------ | --------- | --------------------- |
| Florence-2-base  | 230M   | Fast   | High      | General OCR           |
| Florence-2-large | 770M   | Medium | Very High | High accuracy needs   |
| EasyOCR          | ~100MB | Medium | Good      | Fallback/Multilingual |

## 🔍 Supported Image Formats

- **JPEG** (.jpg, .jpeg)
- **PNG** (.png)
- **WebP** (.webp)
- **BMP** (.bmp)
- **TIFF** (.tiff, .tif)
- **GIF** (.gif)

## 🎯 Use Cases

- **📄 Document Digitization**: Convert physical documents to text
- **🏪 Receipt Processing**: Extract data from receipts and invoices
- **📱 Screenshot Text Extraction**: Get text from app screenshots
- **🚗 License Plate Reading**: Extract text from vehicle plates
- **📚 Book/Article Scanning**: Digitize printed materials
- **🌐 Multilingual Text**: Process text in various languages

## 🛠️ Configuration

### Model Selection

Change the model in `models/ocr_processor.py`:

```python
# For faster inference
ocr = OCRProcessor(model_name="microsoft/Florence-2-base")

# For higher accuracy
ocr = OCRProcessor(model_name="microsoft/Florence-2-large")
```

### UI Customization

Modify the Gradio interface in `app.py`:

- Update colors and styling in the CSS section
- Change layout in the `create_interface()` function
- Add new features or components

## 🧪 Testing

The project includes comprehensive tests:

```bash
# Run all tests
python test_ocr.py

# Test specific functionality
python -c "from models.ocr_processor import OCRProcessor; ocr = OCRProcessor(); print(ocr.get_model_info())"
```

## 🚀 Deployment

### HuggingFace Spaces

1. Fork this repository
2. Create a new Space on HuggingFace
3. Connect your repository
4. The app will automatically deploy

### Docker Deployment

```dockerfile
FROM python:3.9-slim

WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .
EXPOSE 7860

CMD ["python", "app.py"]
```

### Local Server

```bash
# Production server
pip install gunicorn
gunicorn -w 4 -b 0.0.0.0:7860 app:create_interface().app
```

## 🔐 Environment Variables

| Variable               | Description           | Default                |
| ---------------------- | --------------------- | ---------------------- |
| `GRADIO_SERVER_PORT`   | Server port           | 7860                   |
| `TRANSFORMERS_CACHE`   | Model cache directory | `~/.cache/huggingface` |
| `CUDA_VISIBLE_DEVICES` | GPU device selection  | All available          |

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests for new functionality
5. Submit a pull request

## 📝 API Reference

### OCRProcessor Class

```python
from models.ocr_processor import OCRProcessor

# Initialize
ocr = OCRProcessor(model_name="microsoft/Florence-2-base")

# Extract text
text = ocr.extract_text(image)

# Extract with regions
result = ocr.extract_text_with_regions(image)

# Get model info
info = ocr.get_model_info()
```

## 🐛 Troubleshooting

### Common Issues

1. **Model Loading Errors**

   ```bash
   # Install missing dependencies
   pip install einops timm
   ```

2. **CUDA Out of Memory**

   ```python
   # Use CPU instead
   ocr = OCRProcessor()
   ocr.device = "cpu"
   ```

3. **SSL Certificate Errors**
   ```bash
   # Update certificates (macOS)
   /Applications/Python\ 3.x/Install\ Certificates.command
   ```

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- **Microsoft** for the Florence-2 model
- **HuggingFace** for the transformers library
- **Gradio** for the web interface framework
- **EasyOCR** for fallback OCR capabilities

## 📞 Support

- Create an issue for bug reports
- Start a discussion for feature requests
- Check existing issues before posting

---

**Made with ❤️ for the AI community**
