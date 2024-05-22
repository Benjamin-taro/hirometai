# Web Scraping and Google Sheets Automation Script

This script automates the process of web scraping from a specified site and updates the data into a Google Sheets document. The script is scheduled to run daily and also includes a confirmation check every hour.

## Table of Contents

- [Setup](#setup)
- [Usage](#usage)
- [Functions](#functions)
  - [job](#job)
  - [confirmation](#confirmation)

## Setup

1. **Install Dependencies:**
   - Ensure you have Python installed on your machine.
   - Install the required Python packages:
     ```sh
     pip install selenium webdriver-manager beautifulsoup4 pandas gspread oauth2client schedule
     ```

2. **ChromeDriver:**
   - This script uses ChromeDriver. It will be automatically downloaded by `webdriver_manager`.

3. **Google API Credentials:**
   - Create a project in the [Google Developer Console](https://console.developers.google.com/).
   - Enable the Google Sheets API and Google Drive API.
   - Create credentials for a service account and download the JSON file.
   - Save the JSON file in the same directory as your script.

4. **Google Sheets:**
   - Create a Google Sheets document named "質問箱".
   - Share the Google Sheets document with the email address in your service account JSON file.

## Usage

1. **Schedule the Script:**
   - This script is set to run daily at a specific time and to run a confirmation check every hour.
   - You can adjust the schedule times in the script as needed.

2. **Run the Script:**
   - Run the script using Python:
     ```sh
     python your_script_name.py
     ```

## Functions

### job

This function performs the web scraping and updates the data into the Google Sheets document.

```python
def job():
    # Implementation
```
### confirmation
This function prints the current date and time, confirming that the script is running.

```python
def confirmation():
    print(datetime.datetime.now())
    print("I'm working...")
```
