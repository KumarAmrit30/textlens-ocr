"""
Image utilities for TextLens OCR application.
"""

from PIL import Image, ImageEnhance, ImageFilter
from typing import Tuple, Optional, Union
import io
import logging

logger = logging.getLogger(__name__)

# Supported image formats
SUPPORTED_FORMATS = {'JPEG', 'PNG', 'WEBP', 'BMP', 'TIFF', 'GIF'}

def validate_image(image: Union[Image.Image, str, bytes]) -> bool:
    """Validate if the input is a valid image."""
    try:
        if isinstance(image, Image.Image):
            return image.format in SUPPORTED_FORMATS
        elif isinstance(image, str):
            with Image.open(image) as img:
                return img.format in SUPPORTED_FORMATS
        elif isinstance(image, bytes):
            with Image.open(io.BytesIO(image)) as img:
                return img.format in SUPPORTED_FORMATS
        return False
    except Exception:
        return False

def preprocess_image(image: Image.Image, target_size: Optional[Tuple[int, int]] = None) -> Image.Image:
    """Preprocess image for optimal OCR results."""
    try:
        if image.mode != 'RGB':
            image = image.convert('RGB')
        
        if target_size:
            image = resize_image(image, target_size)
        
        return image
    except Exception as e:
        logger.error(f"Error preprocessing image: {str(e)}")
        return image

def resize_image(image: Image.Image, target_size: Tuple[int, int], maintain_aspect: bool = True) -> Image.Image:
    """Resize image to target size."""
    try:
        if maintain_aspect:
            image.thumbnail(target_size, Image.Resampling.LANCZOS)
        else:
            image = image.resize(target_size, Image.Resampling.LANCZOS)
        return image
    except Exception as e:
        logger.error(f"Error resizing image: {str(e)}")
        return image

def enhance_image_for_ocr(image: Image.Image) -> Image.Image:
    """Enhance image quality for better OCR results."""
    try:
        enhancer = ImageEnhance.Contrast(image)
        image = enhancer.enhance(1.2)
        
        enhancer = ImageEnhance.Sharpness(image)
        image = enhancer.enhance(1.1)
        
        return image
    except Exception as e:
        logger.error(f"Error enhancing image: {str(e)}")
        return image

def convert_format(
    image: Image.Image,
    target_format: str = 'PNG'
) -> bytes:
    """
    Convert image to specified format.
    
    Args:
        image: PIL Image object
        target_format: Target format (PNG, JPEG, etc.)
        
    Returns:
        bytes: Image data in target format
        
    TODO: Implement format conversion with optimization
    """
    # TODO: Implement format conversion
    buffer = io.BytesIO()
    image.save(buffer, format=target_format)
    return buffer.getvalue() 