import requests
from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api.formatters import SRTFormatter
from pytube import YouTube
import re
import sys

# Function to get the YouTube video ID from the URL
def extract_video_id(url):
    # Regular expression to extract the video ID from the URL
    regex = r'(?:https?:\/\/(?:www\.)?youtube\.com(?:\/(?:[^\/\n\s]+\/\S+|(?:v|e(?:mbed)?)\/|\S*?[?&]v=))|(?:https?:\/\/(?:www\.)?youtu\.be\/))([^"&?\/\s]{11})'
    match = re.match(regex, url)
    if match:
        return match.group(1)
    else:
        print("Invalid YouTube URL.")
        return None

# Function to get the transcript using the YouTubeTranscriptApi
def get_transcript(video_id):
    try:
        transcript = YouTubeTranscriptApi.get_transcript(video_id)
        return transcript
    except Exception as e:
        print(f"Error fetching transcript: {e}")
        return None

# Function to format the transcript into SRT format
def format_transcript_to_srt(transcript):
    formatter = SRTFormatter()
    srt = formatter.format_transcript(transcript)
    return srt

# Main function to get video details and transcript
def main():
    if len(sys.argv) < 2:
        print("Please provide a YouTube URL.")
        sys.exit(1)

    url = sys.argv[1]
    video_id = extract_video_id(url)

    if video_id:
        print(f"Fetching transcript for video ID: {video_id}")
        transcript = get_transcript(video_id)
        if transcript:
            srt_transcript = format_transcript_to_srt(transcript)
            # Save transcript to a file
            with open(f"{video_id}_transcript.srt", "w") as f:
                f.write(srt_transcript)
            print(f"Transcript saved as {video_id}_transcript.srt")
        else:
            print("No transcript available.")
    else:
        print("Failed to extract video ID.")

if __name__ == "__main__":
    main()