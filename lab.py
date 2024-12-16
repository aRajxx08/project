import requests
from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api.formatters import SRTFormatter
from pytube import YouTube
import re




# Function to scrape YouTube video metadata
def scrape_video_metadata(url):
    try:
        # Create YouTube object
        yt = YouTube(url)
        
        # Print video details
        print(f"Video Title: {yt.title}")
        print(f"Video Description: {yt.description[:250]}...")  # Displaying first 250 characters of the description
        print(f"Video Views: {yt.views}")
        print(f"Video Length: {yt.length} seconds")
        print(f"Video Published on: {yt.publish_date}")
        
    except Exception as e:
        print(f"Error: {e}")

# Ask user for the YouTube video URL
video_url = input("Enter YouTube video URL: ")

# Call the function to scrape metadata
scrape_video_metadata(video_url)