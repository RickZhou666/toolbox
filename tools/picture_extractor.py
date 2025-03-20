import pytesseract
from PIL import Image

# Load the image
image_path = "./resources/imgs/Xnip2025-03-19_21-53-14.jpg"
image = Image.open(image_path)

# Extract text using OCR
extracted_text = pytesseract.image_to_string(image)

# Display extracted text
print(extracted_text)