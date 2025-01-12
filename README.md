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
   ```bash
   pip install google-api-python-client pandas openpyxl
