### CONVERT PDF BOOKS TO AUDIOBOOKS ###
# To use this script, save the PDF book in the same folder you created for this proyect.
# If you want to call the PDF from another location, you must import the Path package
# from pathlib and you must create an instance with the path where the PDF is located.

# Import the packages
import pyttsx3
import pdfplumber as pp
# from pathlib import Path

# Create an instance of pyttsx3
engine = pyttsx3.init()
# path = Path(r"complete path of the PDF book")

# Define the variable that will contain the PDF text
all_the_data = ''

# Extract text from PDF
# If you use a path, change the name of the book to "path"
with pp.open('the_book.pdf') as book:
    for page_no, page in enumerate(book.pages, start=1):
        data = page.extract_text()
        all_the_data += data

# Convert extracted text to audio
engine.save_to_file(all_the_data, 'the_audiobook.mp3')
engine.runAndWait()
engine.stop()
