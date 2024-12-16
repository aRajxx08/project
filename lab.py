import requests
from bs4 import BeautifulSoup
from transformers import pipeline

def scrape_website(url):
    """Scrape content from the provided URL."""
    try:
        # Send an HTTP request to get the page content
        response = requests.get(url)
        response.raise_for_status()  # Ensure the request was successful
        
        # Parse the page content with BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Extract the text from paragraphs and headers (adjust for the site you're scraping)
        paragraphs = soup.find_all(['p', 'h1', 'h2', 'h3'])
        text_content = " ".join([para.get_text() for para in paragraphs])

        return text_content
    except requests.exceptions.RequestException as e:
        print(f"Error while accessing the website: {e}")
        return None

def summarize_text(text):
    """Summarize the provided text."""
    try:
        # Load Hugging Face summarization pipeline
        summarizer = pipeline("summarization", model="sshleifer/distilbart-cnn-12-6")
        
        # Split text into chunks if it's too large for the model
        max_input_length = 1024  # Token limit for the model
        text_chunks = [text[i:i + max_input_length] for i in range(0, len(text), max_input_length)]

        summary = ""
        for chunk in text_chunks:
            summary_chunk = summarizer(chunk)
            summary += summary_chunk[0]['summary_text'] + "\n"
        
        return summary
    except Exception as e:
        print(f"Error during summarization: {e}")
        return "Error during summarization"

def main():
    """Main function to take URL, scrape, and summarize."""
    url = input("Enter the URL of the website to summarize: ")

    # Scrape the website content
    print("\nScraping website...")
    text_content = scrape_website(url)

    if text_content:
        # Summarize the scraped content
        print("\nSummarizing content...")
        summary = summarize_text(text_content)
        print("\nSummary:")
        print(summary)
    else:
        print("Failed to scrape the website.")

if __name__ == "__main__":
    main()