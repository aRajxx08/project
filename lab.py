import requests
from bs4 import BeautifulSoup
from transformers import pipeline
import nltk
nltk.download('punkt')

# Function to scrape a website and extract its main content
def scrape_website(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Check if the request was successful
        soup = BeautifulSoup(response.text, 'html.parser')

        # Extract text from paragraphs or headers (adjust based on website structure)
        paragraphs = soup.find_all(['p', 'h1', 'h2', 'h3'])
        text_content = " ".join([para.get_text() for para in paragraphs])

        return text_content
    except requests.exceptions.RequestException as e:
        print(f"Error while accessing the website: {e}")
        return None

# Function to summarize the extracted text using Hugging Face's transformer model
def summarize_text(text):
    # Use a pre-trained summarization model from Hugging Face
    summarizer = pipeline("summarization")
    
    # Split the text if it's too long for the model
    max_input_length = 1024  # This is model-specific
    text_chunks = [text[i:i + max_input_length] for i in range(0, len(text), max_input_length)]

    summary = ""
    for chunk in text_chunks:
        summary += summarizer(chunk)[0]['summary_text'] + "\n"

    return summary

def main():
    # Get the URL from the user
    url = input("Enter the URL of the website to summarize: ")

    # Step 1: Scrape the website
    website_content = scrape_website(url)

    if website_content:
        # Step 2: Summarize the extracted text
        summarized_text = summarize_text(website_content)

        # Step 3: Output the summarized text
        print("\nSummarized Content:")
        print(summarized_text)

if __name__ == "__main__":
    main()