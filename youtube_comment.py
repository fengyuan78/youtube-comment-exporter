# Import necessary libraries
from googleapiclient.discovery import build  # For interacting with the YouTube API
import pandas as pd  # For handling data and exporting to Excel
from datetime import datetime  # For timestamping exported files
import tkinter as tk  # For creating a graphical user interface (GUI)
from tkinter import messagebox  # For displaying popup messages in the GUI
import re  # For regular expressions to extract video IDs from YouTube links

# Replace with your API key
# Ensure the API key is valid and has the necessary permissions for accessing the YouTube Data API.
api_key = "your_own_api_key" #such as "AIzaSyDehrFa78c-hGfAG7uN0Gg7_t7Mt1cLiCc"
youtube = build('youtube', 'v3', developerKey=api_key)  # Initialize the YouTube API client

# Function to fetch comments and replies from a YouTube video
def get_comments(video_id):
    """
    Fetches all comments and replies for a given YouTube video.
    
    Args:
        video_id (str): The ID of the YouTube video.
    
    Returns:
        list: A list of dictionaries containing comments and replies.
    """
    comments = []  # List to store comments and replies
    request = youtube.commentThreads().list(
        part="snippet,replies",  # Include snippet (comment details) and replies
        videoId=video_id,  # The YouTube video ID
        textFormat="plainText",  # Retrieve comments in plain text format
        maxResults=100  # Maximum number of results per request (API limit)
    )
    
    while request:  # Loop through all available pages of comments
        response = request.execute()  # Execute the API request
        for item in response["items"]:  # Iterate through each comment thread
            # Get the top-level comment
            top_comment = item["snippet"]["topLevelComment"]["snippet"]["textDisplay"]
            comments.append({"Text": top_comment, "Type": "Comment"})  # Store as a top-level comment

            # Check if the top-level comment has replies
            if "replies" in item:
                for reply in item["replies"]["comments"]:  # Iterate through each reply
                    reply_text = reply["snippet"]["textDisplay"]
                    comments.append({"Text": reply_text, "Type": "Reply"})  # Store as a reply

        # Check for next page token to fetch additional comments
        if "nextPageToken" in response:
            request = youtube.commentThreads().list(
                part="snippet,replies",
                videoId=video_id,
                textFormat="plainText",
                maxResults=100,
                pageToken=response["nextPageToken"]  # Token for the next page
            )
        else:
            break  # Exit the loop if there are no more pages
    return comments

# Function to export comments to an Excel file
def export_comments_to_excel(video_id, comments):
    """
    Exports comments and replies to an Excel file.
    
    Args:
        video_id (str): The YouTube video ID.
        comments (list): List of dictionaries containing comments and replies.
    
    Returns:
        str: The filename of the exported Excel file.
    """
    # Generate a timestamp for the filename
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"youtube_comments_{video_id}_{timestamp}.xlsx"

    # Convert the list of comments to a pandas DataFrame
    df = pd.DataFrame(comments)

    # Reorder columns so "Type" (Comment or Reply) appears first
    df = df[['Type', 'Text']]

    # Save the DataFrame to an Excel file
    df.to_excel(filename, index=False)
    return filename

# Function to handle the "Export Comments" button click event
def run_script():
    """
    Handles the logic for extracting comments and exporting them to Excel when the button is clicked.
    """
    # Get the video link entered by the user
    video_link = video_link_entry.get()

    # Extract video ID from the YouTube URL using a regular expression
    video_id_match = re.search(r'v=([a-zA-Z0-9_-]+)', video_link)
    if video_id_match:  # If a valid video ID is found
        video_id = video_id_match.group(1)
    else:
        # Display an error message if the link is invalid
        messagebox.showerror("Error", "Invalid YouTube link.")
        return

    # Fetch comments and replies for the video
    comments = get_comments(video_id)

    # Export the comments to an Excel file
    exported_file = export_comments_to_excel(video_id, comments)

    # Display a success message with the file name
    messagebox.showinfo("Success", f"Comments exported to {exported_file}")
    
    # Close the GUI window after the message box is closed
    root.destroy()

# Create the GUI window
root = tk.Tk()
root.title("YouTube Comment Exporter")  # Set the title of the GUI window

# Create and place the label for the YouTube video link input
video_link_label = tk.Label(root, text="YouTube Video Link:")
video_link_label.pack(pady=5)  # Add padding for better spacing

# Create and place the entry field for the YouTube video link
video_link_entry = tk.Entry(root, width=50)
video_link_entry.pack(pady=5)

# Create and place the "Export Comments" button
run_button = tk.Button(root, text="Export Comments", command=run_script)
run_button.pack(pady=10)

# Start the GUI event loop
root.mainloop()
