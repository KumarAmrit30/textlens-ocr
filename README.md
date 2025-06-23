---
title: TextLens - AI-Powered OCR
emoji: 🔍
colorFrom: blue
colorTo: purple
sdk: gradio
sdk_version: 4.44.0
app_file: app.py
pinned: false
license: mit
---

# 🔍 TextLens - AI-Powered OCR

[![Deploy to HuggingFace](https://img.shields.io/badge/🤗-Deploy%20to%20Spaces-blue)](https://huggingface.co/spaces/GoConqurer/textlens-ocr)
[![GitHub](https://img.shields.io/badge/GitHub-Repository-green)](https://github.com/KumarAmrit30/textlens-ocr)
[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)
[![Gradio](https://img.shields.io/badge/gradio-4.44+-orange.svg)](https://gradio.app/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](./LICENSE)

A modern, streamlined OCR application powered by state-of-the-art vision-language models. Built with a simple, fast architecture for high-performance text extraction from images.

## 🚀 Live Demo: [Textlens](https://huggingface.co/spaces/GoConqurer/textlens-ocr)

## ✨ Features

### 🤖 Three Powerful OCR Models

- **🔥 Nanonets-OCR-s**: State-of-the-art image-to-markdown OCR with intelligent content recognition
- **🚀 Qwen2-VL-OCR-2B-Instruct**: Fast general-purpose OCR optimized for speed and accuracy
- **📄 RolmOCR**: Specialized for complex documents, scanned text, and structured layouts

### ⚡ Performance Optimized

- **Single-file Architecture**: Streamlined for maximum performance
- **GPU Acceleration**: CUDA and MPS support with @spaces.GPU optimization
- **Real-time Streaming**: Live text generation with immediate results
- **Smart Model Loading**: Models loaded once at startup and kept in memory

### 🎨 Modern Interface

- **Clean Gradio UI**: Beautiful, responsive web interface
- **Model Selection**: Choose the best OCR model for your task
- **Advanced Options**: Fine-tune generation parameters (temperature, top-p, etc.)
- **Multiple Input Methods**: Upload files, paste from clipboard
- **One-click Copy**: Easy copying of extracted text

## 🚀 Quick Start

### 📋 Prerequisites

- Python 3.9 or higher
- pip (Python package installer)
- Optional: CUDA-compatible GPU for faster processing

### 💻 Installation

1. **Clone the Repository**

   ```bash
   git clone https://github.com/KumarAmrit30/textlens-ocr.git
   cd textlens-ocr
   ```

2. **Create Virtual Environment** (Recommended)

   ```bash
   python -m venv textlens_env
   source textlens_env/bin/activate  # On Windows: textlens_env\Scripts\activate
   ```

3. **Install Dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Launch the Application**

   ```bash
   python app.py
   ```

5. **Access the Interface**
   - Open your web browser and navigate to: `http://localhost:7860`
   - The interface will be ready to use immediately

### 🧪 Quick Test

```bash
# Verify installation
python -c "from models.ocr_processor import OCRProcessor; print('✅ TextLens ready!')"
```

## 📁 Project Structure

```
textlens-ocr/
├── app.py                    # Main application entry point
├── requirements.txt          # Python dependencies
├── models/
│   ├── __init__.py
│   └── ocr_processor.py     # Florence-2 OCR processing logic
├── ui/
│   ├── __init__.py
│   ├── interface.py         # Gradio interface setup
│   ├── handlers.py          # Event handlers and processing logic
│   └── styles.py            # Custom CSS styling
└── utils/
    ├── __init__.py
    └── image_utils.py       # Image preprocessing utilities
```

## 🔧 Configuration

### Model Selection

The application supports two Florence-2 model variants:

```python
# Fast inference (default)
OCRProcessor(model_name="microsoft/Florence-2-base")    # ~270M parameters

# Higher accuracy
OCRProcessor(model_name="microsoft/Florence-2-large")   # ~770M parameters
```

### Environment Variables

| Variable               | Description                          | Default                |
| ---------------------- | ------------------------------------ | ---------------------- |
| `SPACE_ID`             | HuggingFace Space ID (auto-detected) | None                   |
| `TRANSFORMERS_CACHE`   | Model cache directory                | `~/.cache/huggingface` |
| `CUDA_VISIBLE_DEVICES` | GPU selection                        | All available          |

## 📊 Model Performance

| Model                  | Size  | Speed     | Accuracy     | Best For               |
| ---------------------- | ----- | --------- | ------------ | ---------------------- |
| **Florence-2-base**    | 270M  | ⚡ Fast   | 📈 High      | General OCR, Real-time |
| **Florence-2-large**   | 770M  | 🐌 Medium | 📊 Very High | Maximum accuracy       |
| **EasyOCR** (Fallback) | ~100M | 🚀 Medium | 📋 Good      | Backup, Multilingual   |

## 🎯 Supported Use Cases

- 📄 **Documents**: PDFs, scanned papers, forms, contracts
- 🧾 **Receipts**: Shopping receipts, invoices, bills
- 📱 **Screenshots**: App interfaces, error messages, code snippets
- 🚗 **Signs**: Street signs, license plates, billboards
- 📚 **Books**: Printed text, handwritten notes, articles
- 🌐 **Multi-language**: Various languages (with EasyOCR fallback)

## 💡 Usage Tips

1. **Image Quality**: Higher resolution images generally produce better results
2. **Text Clarity**: Ensure text is clearly visible and not blurry
3. **Lighting**: Good lighting improves text recognition accuracy
4. **First Run**: Initial model download may take 2-3 minutes
5. **GPU Usage**: CUDA/MPS acceleration significantly improves performance

## 🔍 Technical Details

### Dependencies

- **torch**: PyTorch for deep learning operations
- **transformers**: HuggingFace Transformers for Florence-2 models
- **gradio**: Web interface framework
- **pillow**: Image processing
- **easyocr**: Fallback OCR engine
- **accelerate**: Hardware acceleration support

### Hardware Requirements

- **Minimum**: 4GB RAM, CPU
- **Recommended**: 8GB+ RAM, CUDA-compatible GPU
- **Optimal**: 16GB+ RAM, Modern GPU (RTX 30/40 series, etc.)

## 🐛 Troubleshooting

### Common Issues

**1. Model Loading Fails**

```bash
# Clear cache and retry
rm -rf ~/.cache/huggingface/transformers/
python app.py
```

**2. GPU Not Detected**

```bash
# Check CUDA installation
python -c "import torch; print(torch.cuda.is_available())"
```

**3. Memory Issues**

- Try using Florence-2-base instead of Florence-2-large
- Close other applications to free up RAM
- Restart the application

**4. Network Issues**

- Ensure stable internet connection for model download
- Check firewall/proxy settings

## 🤝 Contributing

We welcome contributions! Here's how to get started:

1. **Fork the Repository**

   ```bash
   git clone https://github.com/YOUR_USERNAME/textlens-ocr.git
   cd textlens-ocr
   ```

2. **Create a Feature Branch**

   ```bash
   git checkout -b feature/your-feature-name
   ```

3. **Make Your Changes**

   - Add new features or fix bugs
   - Follow the existing code style
   - Test your changes thoroughly

4. **Submit a Pull Request**
   ```bash
   git add .
   git commit -m "feat: add your feature description"
   git push origin feature/your-feature-name
   ```

### Development Setup

```bash
# Install development dependencies
pip install -r requirements.txt

# Run tests (if available)
python -m pytest tests/

# Check code style
flake8 . --exclude=textlens_env
```

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- **Microsoft**: For the Florence-2 vision-language models
- **HuggingFace**: For the Transformers library and model hosting
- **Gradio**: For the web interface framework
- **EasyOCR**: For the reliable fallback OCR engine

## 📞 Support

If you encounter any issues or have questions:

1. Search existing [GitHub Issues](https://github.com/KumarAmrit30/textlens-ocr/issues)
2. Create a new issue with detailed information

---

**⭐ If you find TextLens useful, please give it a star on GitHub!**
