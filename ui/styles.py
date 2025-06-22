"""
CSS styles for TextLens OCR interface.
"""

def get_custom_css():
    """Return custom CSS for the Gradio interface."""
    return """
    .gradio-container {
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        max-width: 1200px;
        margin: 0 auto;
        background-color: #ffffff;
    }
    .header {
        text-align: center;
        margin-bottom: 30px;
        padding: 20px;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        border-radius: 10px;
        color: white !important;
    }
    .header h1 {
        color: white !important;
        margin: 10px 0;
    }
    .header p {
        color: white !important;
        margin: 10px 0;
    }
    .status-box {
        background-color: #f8f9fa !important;
        border: 1px solid #dee2e6;
        border-radius: 8px;
        padding: 15px;
        margin: 10px 0;
        color: #212529 !important;
    }
    .status-box p, .status-box div, .status-box * {
        color: #212529 !important;
    }
    .upload-box {
        border: 2px dashed #007bff;
        border-radius: 10px;
        padding: 20px;
        text-align: center;
        background-color: #f8f9ff;
        color: #333333 !important;
    }
    .markdown-text {
        color: #212529 !important;
    }
    .markdown-text h1, .markdown-text h2, .markdown-text h3, .markdown-text h4, .markdown-text h5, .markdown-text h6 {
        color: #1a1a1a !important;
    }
    .markdown-text p, .markdown-text li, .markdown-text div {
        color: #333333 !important;
    }
    .markdown-text strong {
        color: #000000 !important;
    }
    .tips-section {
        background-color: #e3f2fd !important;
        border: 1px solid #90caf9;
        border-radius: 8px;
        padding: 15px;
        margin: 10px 0;
        color: #0d47a1 !important;
    }
    .tips-section p, .tips-section ul, .tips-section li {
        color: #0d47a1 !important;
    }
    .tips-section strong {
        color: #01579b !important;
    }
    .instructions-section {
        background-color: #f3e5f5 !important;
        border: 1px solid #ce93d8;
        border-radius: 8px;
        padding: 15px;
        margin: 10px 0;
        color: #4a148c !important;
    }
    .instructions-section p, .instructions-section ul, .instructions-section li {
        color: #4a148c !important;
    }
    .instructions-section strong {
        color: #2e0051 !important;
    }
    .primary-button {
        background-color: #007bff !important;
        color: white !important;
        border: none !important;
    }
    .gradio-container .markdown {
        color: #212529 !important;
    }
    .gradio-container .markdown p {
        color: #333333 !important;
    }
    .gradio-container .markdown h1, 
    .gradio-container .markdown h2, 
    .gradio-container .markdown h3 {
        color: #1a1a1a !important;
    }
    .textbox-container {
        color: #212529 !important;
    }
    """ 