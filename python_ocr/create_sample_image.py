from PIL import Image, ImageDraw, ImageFont

def generate_sample_image(output_path="python_ocr/sample_image.png"):
    """Generates a simple image with text."""
    try:
        # Create a white image
        img_width = 400
        img_height = 100
        img = Image.new('RGB', (img_width, img_height), color = 'white')
        d = ImageDraw.Draw(img)

        # Add text
        text = "Hello OCR"
        try:
            # Try to load a common font, fallback if not found
            font = ImageFont.truetype("arial.ttf", 40)
        except IOError:
            font = ImageFont.load_default()
        
        # Calculate text position (centered)
        bbox = d.textbbox((0,0), text, font=font)
        text_width = bbox[2] - bbox[0]
        text_height = bbox[3] - bbox[1]
        x = (img_width - text_width) / 2
        y = (img_height - text_height) / 2
        
        d.text((x, y), text, fill=(0,0,0), font=font) # Black text
        img.save(output_path)
        print(f"Sample image saved to {output_path}")
    except ImportError:
        print("Pillow (PIL) is not installed. Cannot create sample image.")
        print("Please install it using: pip install Pillow")
    except Exception as e:
        print(f"An error occurred while generating the image: {e}")

if __name__ == '__main__':
    generate_sample_image()
