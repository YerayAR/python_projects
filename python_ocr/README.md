# Python OCR Reader

## Description
This tool allows you to extract text from images using Python. It utilizes the Tesseract OCR engine and the `pytesseract` and `Pillow` Python libraries.

## Dependencies

### System-Wide
*   **Python 3.x:** Ensure you have Python 3 installed.
*   **Tesseract OCR Engine:** This must be installed on your system. For installation instructions, please refer to the official Tesseract wiki:
    *   [Tesseract OCR Installation Guide](https://github.com/tesseract-ocr/tesseract/wiki)

### Python Libraries
You will need the following Python libraries:
*   `pytesseract`
*   `Pillow`

## Setup/Installation

1.  **Install Tesseract OCR Engine:**
    Follow the instructions provided in the [Tesseract OCR Installation Guide](https://github.com/tesseract-ocr/tesseract/wiki) for your operating system. Ensure that the `tesseract` command is available in your system's PATH.

2.  **Install Python Libraries:**
    Open your terminal or command prompt and run the following command to install the required Python packages:
    ```bash
    pip install pytesseract Pillow
    ```

## Usage

### Running the Example
An example script is provided to demonstrate the OCR functionality. To run it:
1.  Ensure you have generated the sample image by running `python python_ocr/create_sample_image.py` if `sample_image.png` is not already present.
2.  Execute the example script:
    ```bash
    python python_ocr/run_ocr_example.py
    ```
    This will process the `python_ocr/sample_image.png` and print the extracted text.

### Using the `extract_text_from_image` function
To integrate the OCR functionality into your own Python scripts, you can import and use the `extract_text_from_image` function from `ocr_reader.py`:

```python
from ocr_reader import extract_text_from_image

# Replace "path/to/your/image.png" with the actual path to your image file
image_path = "path/to/your/image.png" 
try:
    text = extract_text_from_image(image_path)
    print("Extracted Text:")
    print(text)
except Exception as e:
    print(f"An error occurred: {e}")

```

## Helper Scripts

*   **`create_sample_image.py`:**
    Located in the `python_ocr/` directory, this script can be run (`python python_ocr/create_sample_image.py`) to generate the `sample_image.png` file. This image is used by the `run_ocr_example.py` script. It's useful if you need to regenerate the sample image or if it's missing.
