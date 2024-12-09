
import requests
from bs4 import BeautifulSoup
import pandas as pd

# URL to scrape
url = 'https://example.com'  # Replace with the target URL

# Send HTTP request to the URL
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    print("Successfully fetched the webpage")
else:
    print("Failed to retrieve the webpage")
    exit()

# Parse the content of the webpage using BeautifulSoup
soup = BeautifulSoup(response.content, 'html.parser')

# Example: Extract all headings (h1, h2, etc.)
headings = soup.find_all(['h1', 'h2', 'h3'])

# Store the headings in a list
headings_list = [heading.get_text() for heading in headings]

# Convert the data into a DataFrame (optional for easy handling)
df = pd.DataFrame(headings_list, columns=["Headings"])

# Print or save the data
print(df)

# Optionally, save the extracted data to a CSV file
df.to_csv('headings.csv', index=False)



 
import spacy
from bs4 import BeautifulSoup
import requests

# Load the pre-trained spaCy model for Named Entity Recognition
nlp = spacy.load("en_core_web_sm")

# Example URL to scrape
url = 'https://example.com'

# Send HTTP request
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

# Get all paragraphs or text content
text = soup.get_text()

# Use spaCy to process the text and extract named entities
doc = nlp(text)

# Extract named entities (persons, organizations, locations, etc.)
entities = [(entity.text, entity.label_) for entity in doc.ents]

# Print the extracted entities
for entity in entities:
    print(f"Entity: {entity[0]} | Label: {entity[1]}")
import os
import requests
from bs4 import BeautifulSoup

# URL to scrape
url = 'https://example.com'

# Send HTTP request
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

# Find all image tags
images = soup.find_all('img')

# Create a directory to save images
os.makedirs('downloaded_images', exist_ok=True)

# Loop through each image tag and download the image
for img in images:
    img_url = img.get('src')
    if img_url:
        img_name = img_url.split("/")[-1]
        img_data = requests.get(img_url).content
        with open(f'downloaded_images/{img_name}', 'wb') as f:
            f.write(img_data)

print("Images have been downloaded!")

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Set up the WebDriver (make sure to download the appropriate driver for your browser)
driver = webdriver.Chrome(executable_path='/path/to/chromedriver')

# URL to scrape
url = 'https://example.com'

# Open the website
driver.get(url)

# Wait for dynamic content to load
time.sleep(3)  # You can adjust this depending on the page load time

# Extract the content (for example, extract all product names)
products = driver.find_elements(By.CLASS_NAME, 'product-name')  # Modify based on the actual HTML

# Print the products
for product in products:
    print(product.text)

# Close the browser
driver.quit()