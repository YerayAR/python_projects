import os
from ocr_reader import extract_text_from_image

def run_example():
    """
    Runs the OCR example by processing a sample image and printing the extracted text.
    """
    script_dir = os.path.dirname(os.path.abspath(__file__))
    image_name = "sample_image.png"
    image_path = os.path.join(script_dir, image_name)

    # Check if ocr_reader.py exists (though import would fail anyway)
    ocr_reader_path = os.path.join(script_dir, "ocr_reader.py")
    if not os.path.exists(ocr_reader_path):
        print(f"Error: ocr_reader.py not found at {ocr_reader_path}")
        return

    # Check if the sample image exists
    if not os.path.exists(image_path):
        print(f"Error: Sample image '{image_name}' not found at {image_path}")
        print("Please ensure 'sample_image.png' exists in the 'python_ocr' directory.")
        print("You might need to run 'create_sample_image.py' first.")
        return

    print(f"Processing image: {image_path}")
    extracted_text = extract_text_from_image(image_path)

    print("\n--- Extracted Text ---")
    print(extracted_text)
    print("----------------------")

if __name__ == "__main__":
    run_example()
