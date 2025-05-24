import pytesseract
from PIL import Image

def extract_text_from_image(image_path):
    """
    Extracts text from an image file.

    Args:
        image_path (str): The path to the image file.

    Returns:
        str: The extracted text.
    """
    try:
        img = Image.open(image_path)
        text = pytesseract.image_to_string(img)
        return text
    except FileNotFoundError:
        return "Error: Image file not found."
    except Exception as e:
        return f"An error occurred: {e}"

# TODO: Add PDF processing

if __name__ == '__main__':
    # Example usage (optional, can be removed or commented out)
    # Replace 'path/to/your/image.png' with an actual image path for testing
    # text_output = extract_text_from_image('path/to/your/image.png')
    # print(text_output)
    pass
