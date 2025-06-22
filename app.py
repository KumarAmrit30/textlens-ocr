"""
TextLens - AI-Powered OCR Application

Main entry point for the application.
"""

import os
import logging
from ui.interface import create_interface

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def main():
    """Main function to launch the application."""
    logger.info("🚀 Starting TextLens OCR application...")
    
    # Check if running on HuggingFace Spaces
    is_hf_spaces = os.getenv("SPACE_ID") is not None
    
    try:
        interface = create_interface()
        
        # Configure for HuggingFace Spaces or local deployment
        if is_hf_spaces:
            logger.info("🤗 Running on HuggingFace Spaces")
            interface.launch(
                share=False,
                server_name="0.0.0.0",
                server_port=7860,  # HF Spaces default port
                show_error=True
            )
        else:
            logger.info("💻 Running locally")
            interface.launch(
                share=False,
                server_name="0.0.0.0",
                server_port=7861,
                show_error=True,
                favicon_path=None,
                ssl_verify=False
            )
        
    except Exception as e:
        logger.error(f"Failed to start application: {str(e)}")
        raise

if __name__ == "__main__":
    main() 