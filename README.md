# YouTube Comment Exporter

This Python application enables users to fetch all comments and replies from a specific YouTube video and export them to an Excel file. It provides a simple GUI for entering the video link and automates the entire process.

## Features
- Fetches top-level comments and replies from a YouTube video.
- Exports the data to an Excel file with a timestamped filename.
- Simple GUI for easy use.
- Handles pagination to retrieve all comments for videos with many responses.

## Technologies Used
- **Python**: Core programming language.
- **YouTube Data API**: For accessing YouTube video comments.
- **Tkinter**: For building the graphical user interface.
- **Pandas**: For data manipulation and Excel export.

## Prerequisites
1. Python 3.7 or later installed on your system.
2. A valid YouTube Data API key.
3. Installed Python packages: `google-api-python-client`, `pandas`, and `openpyxl`.

   You can install them using:
   pip install google-api-python-client pandas openpyxl



To use this application, you need a YouTube Data API key. Follow the steps below to create and obtain your API key:

Create a Google Cloud Project

Go to the Google Cloud Console.
Log in with your Google account.
Click on "Select a Project" in the top navigation bar.
Click "New Project" and fill in the project details (e.g., project name).
Click "Create".
Enable the YouTube Data API

After creating the project, go to the API Library.
Search for YouTube Data API v3.
Click on the YouTube Data API v3 result.
Click "Enable".
Create Credentials for the API

Go to the Credentials Page.
Click "Create Credentials" and select "API Key".
Google will generate an API key for you. Copy the key and save it securely.
Restrict Your API Key (Optional but Recommended)

On the Credentials page, click the pencil/edit icon next to your API key.
Under Key Restrictions, you can:
Restrict it to specific APIs (select YouTube Data API v3).
Restrict it by IP addresses or referrer (for security).
Save your changes.
Test Your API Key

Open a terminal or command prompt.
Use a tool like curl to test your key:

curl "https://www.googleapis.com/youtube/v3/videos?part=snippet&id=Ks-_Mh1QhMc&key=YOUR_API_KEY"
Replace YOUR_API_KEY with your actual API key. If successful, you'll get a response with video details.
Add the API Key to Your Project

Open the Python script (youtube_comment_exporter.py).
Replace the api_key variable value with your API key:
api_key = "YOUR_API_KEY"
