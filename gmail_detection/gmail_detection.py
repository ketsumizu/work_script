#!/usr/bin/env python3
import os
import re
import requests
import xml.etree.ElementTree as ET

# Load environment variables from .env file
from dotenv import load_dotenv

load_dotenv()

TARGET_EMAIL = "target@example.com"
KEYWORDS_REGEX = "test|テスト|てすと"

# Connect to Gmail
print("Connecting to Gmail...")
response = requests.get("https://mail.google.com/mail/feed/atom", auth=(os.getenv("GMAIL_USERNAME"), os.getenv("APP_PASSWORD")))
xml_data = response.text

# Debug: Print XML data
# print("XML data:")
# print(xml_data)

# Parse XML feed and process emails
print("Processing emails...")

# Extract titles and email addresses from the XML
root = ET.fromstring(xml_data)
entries = root.findall("{http://purl.org/atom/ns#}entry")  # namespaceを指定して検索する

# Process emails
for entry in entries:
    title = entry.find("{http://purl.org/atom/ns#}title").text
    email = entry.find("{http://purl.org/atom/ns#}author/{http://purl.org/atom/ns#}email").text

    # Debug: Print title and email
    # print("Title:", title)
    # print("Email:", email)

    if email == TARGET_EMAIL and re.search(KEYWORDS_REGEX, title):
        # Describe some process here.

print("Script execution completed.")

