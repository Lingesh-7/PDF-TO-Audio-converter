
# Install the pdfplumber library for extracting text from PDF files
# pip install pdfplumber

# Importing the pdfplumber library for PDF text extraction
import pdfplumber


# Extracting Text from PDF and Formatting as Markdown
# This cell defines the pdf_to_markdown function,
# which is used to extract text from a PDF file and format it in Markdown.

# The process involves:
# Opening the PDF file using pdfplumber, which allows us to access its content.
# Iterating through each page of the PDF.
# Extracting text from each page.
# Applying basic Markdown formatting to the text for better readability.
# This includes adding double newlines for new paragraphs and a separator line between pages.
# The function takes the path of the PDF file as an input and returns the formatted text.
# An example usage is shown at the end of the cell, where the function is called with a
# specified PDF file path, and the output is printed.



def pdf_to_markdown(pdf_path):
    # Open the PDF file at the given path
    with pdfplumber.open(pdf_path) as pdf:
        markdown_content = ""
        # Loop through each page in the PDF
        for page in pdf.pages:
            # Extract text from each page
            text = page.extract_text()
            if text:
                # Format the text with basic Markdown: double newline for new paragraphs
                markdown_page = text.replace('\n', '\n\n')
                # Add a separator line between pages
                markdown_content += markdown_page + '\n\n---\n\n'

        return markdown_content

# Function Usage
pdf_path = 'sd.pdf'  # Replace with the actual PDF file path
markdown_text = pdf_to_markdown(pdf_path)
print(markdown_text)  # Print the extracted and formatted text


# Importing the 're' module for regular expression operations
import re

def markdown_to_plain_text(markdown_text):
    # Remove Markdown URL syntax ([text](link)) and keep only the text
    text = re.sub(r'\[([^\]]+)\]\([^\)]+\)', r'\1', markdown_text)

    # Remove Markdown formatting for bold and italic text
    text = re.sub(r'\*\*([^*]+)\*\*', r'\1', text)  # Bold with **
    text = re.sub(r'\*([^*]+)\*', r'\1', text)      # Italic with *
    text = re.sub(r'\_\_([^_]+)\_\_', r'\1', text)  # Bold with __
    text = re.sub(r'\_([^_]+)\_', r'\1', text)      # Italic with _

    # Remove Markdown headers, list items, and blockquote symbols
    text = re.sub(r'#+\s?', '', text)  # Headers
    text = re.sub(r'-\s?', '', text)   # List items
    text = re.sub(r'>\s?', '', text)   # Blockquotes

    return text

# Function Usage
plain_text = markdown_to_plain_text(markdown_text)
print(plain_text)  # Printing the converted plain text

# Final Text Cleaning
# This cell is dedicated to further cleaning the plain text extracted from the PDF.
# In some cases, the text conversion process may leave behind unwanted artifacts or
# specific words that are not relevant or desirable for the final audio output.
# This step allows for the removal of such elements.
#
# The cell demonstrates how to remove a specific word or artifact from the text.
# In this example, any occurrences of the word "artifact" are being removed from the text.
# This approach can be adapted to target and remove any other specific words or symbols
# that might be present in the text after the initial conversion and formatting steps
#
# Further cleaning of the plain text
# Here, we are removing a specific unwanted word or artifact from the text
# Replace "artifact" with any specific word or symbol you need to remove
cleaned_text = plain_text.replace("artifact", "")

# Printing the cleaned text to verify the changes
print(cleaned_text)



# Import the required module for text
# to speech conversion
import pyttsx3
#
# init function to get an engine instance for the speech synthesis
speak = pyttsx3.init()
# say method on the engine that passing input text to be spoken
speak.say(cleaned_text)
# run and wait method, it processes the voice commands
speak.runAndWait()
