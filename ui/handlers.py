"""
Event handlers for TextLens OCR interface.
"""

import logging
from PIL import Image
from models.ocr_processor import OCRProcessor

logger = logging.getLogger(__name__)

# Global OCR processor instance
ocr_processor = None

def initialize_ocr_processor():
    """Initialize the OCR processor."""
    global ocr_processor
    try:
        logger.info("Initializing OCR processor...")
        ocr_processor = OCRProcessor(model_name="microsoft/Florence-2-base")
        return True
    except Exception as e:
        logger.error(f"Failed to initialize OCR processor: {str(e)}")
        return False

def extract_text_from_image(image):
    """Extract text from image using Florence-2 model."""
    global ocr_processor
    
    if image is None:
        return "❌ No image provided. Please upload an image."
    
    try:
        if ocr_processor is None:
            logger.info("OCR processor not initialized, initializing now...")
            if not initialize_ocr_processor():
                return "❌ Failed to initialize OCR model. Please check your internet connection and try again."
        
        if not isinstance(image, Image.Image):
            return "❌ Invalid image format"
        
        logger.info("Processing image with Florence-2...")
        extracted_text = ocr_processor.extract_text(image)
        return extracted_text
        
    except Exception as e:
        error_msg = f"❌ Error processing image: {str(e)}"
        logger.error(f"Error in extract_text_from_image: {str(e)}")
        return error_msg

def get_model_status():
    """Get current model status information."""
    global ocr_processor
    
    if ocr_processor is None:
        return """
        **Model Status:** Not Initialized
        
        The Florence-2 model will be loaded automatically when you upload your first image.
        """
    
    try:
        info = ocr_processor.get_model_info()
        return f"""
        **Model Status:** ✅ Loaded
        
        **Model:** {info.get('model_name', 'Unknown')}
        **Device:** {info.get('device', 'Unknown')}
        **Parameters:** {info.get('parameters', 'Unknown')}
        **Model Loaded:** {'✅' if info.get('model_loaded') else '❌'}
        **Processor Loaded:** {'✅' if info.get('processor_loaded') else '❌'}
        """
    except Exception as e:
        return f"❌ Error getting model status: {str(e)}" 