# from PIL import Image
# import pytesseract

# # Install pytesseract and tesseract-OCR and specify the tesseract path
# pytesseract.pytesseract.tesseract_cmd = r'D:\tesseract'

# def perform_ocr(C:\Users\User\OneDrive\Pictures\Wallpapers\tiraya-adam-FNRIC8aaF4o-unsplash.jpg"):
#     try:
#         # Open the image file
#         image = Image.open("C:\Users\User\OneDrive\Pictures\Wallpapers\tiraya-adam-FNRIC8aaF4o-unsplash.jpg")

#         # Perform OCR on the image
#         text = pytesseract.image_to_string(image)

#         # Print the extracted text
#         print("Extracted Text:")
#         print(text)

#         return text

#     except Exception as e:
#         print(f"An error occurred: {str(e)}")

# # Example usage
# image_path = "path/to/your/image.png"
# extracted_text = perform_ocr(image_path)

# # Now you can use the extracted text with a text-to-speech (TTS) library to create sound
# # For TTS, you can use a library like pyttsx3 (Python Text to Speech)
# # Install pyttsx3: pip install pyttsx3

# import pyttsx3

# def text_to_speech(text):
#     try:
#         engine = pyttsx3.init()
#         engine.say(text)
#         engine.runAndWait()
#     except Exception as e:
#         print(f"An error occurred in text-to-speech: {str(e)}")

# # Example usage
# text_to_speech(extracted_text)








# from PIL import Image
# import pytesseract

# # Install pytesseract and tesseract-OCR and specify the tesseract path
# pytesseract.pytesseract.tesseract_cmd = r'D:\tesseract'

# def perform_ocr(image_path):
#     try:
#         # Open the image file
#         image = Image.open(image_path)

#         # Perform OCR on the image
#         text = pytesseract.image_to_string(image)

#         # Print the extracted text
#         print("Extracted Text:")
#         print(text)

#         return text

#     except Exception as e:
#         print(f"An error occurred: {str(e)}")

# # Example usage
# image_path = 'C:\Users\User\Desktop\info aid tech offer.JPG'
# extracted_text = perform_ocr(image_path)

# # Now you can use the extracted text with a text-to-speech (TTS) library to create sound
# # For TTS, you can use a library like pyttsx3 (Python Text to Speech)
# # Install pyttsx3: pip install pyttsx3

# import pyttsx3

# def text_to_speech(text):
#     try:
#         engine = pyttsx3.init()
#         engine.say(text)
#         engine.runAndWait()
#     except Exception as e:
#         print(f"An error occurred in text-to-speech: {str(e)}")

# # Example usage
# text_to_speech(extracted_text)




from PIL import Image
import pytesseract

# Install pytesseract and tesseract-OCR and specify the tesseract path
pytesseract.pytesseract.tesseract_cmd = r'D:\tesseract'

def perform_ocr(image_path):
    try:
        # Open the image file
        image = Image.open(image_path)

        # Perform OCR on the image
        text = pytesseract.image_to_string(image)

        # Print the extracted text
        print("Extracted Text:")
        print(text)

        return text

    except Exception as e:
        print(f"An error occurred: {str(e)}")

# Example usage
image_path = r'C:\Users\User\Desktop\info aid tech offer.JPG'
extracted_text = perform_ocr(image_path)

# Now you can use the extracted text with a text-to-speech (TTS) library to create sound
# For TTS, you can use a library like pyttsx3 (Python Text to Speech)
# Install pyttsx3: pip install pyttsx3

import pyttsx3

def text_to_speech(text):
    try:
        engine = pyttsx3.init()
        engine.say(text)
        engine.runAndWait()
    except Exception as e:
        print(f"An error occurred in text-to-speech: {str(e)}")

# Example usage
text_to_speech(extracted_text)
