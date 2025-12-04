'''
Real-World Example : Multithreading for I/O-Bound Tasks

Scenario: Web Scraping
----------------------
Web scraping involves downloading data from multiple web pages.
This is an I/O-bound task because the program spends most of its time
WAITING for the server to respond.

Using MULTITHREADING allows us to request multiple web pages at the
same time, making the whole operation much faster.
'''

# Import threading module to create multiple threads
import threading

# Import requests module to fetch web pages
import requests

# BeautifulSoup helps in parsing HTML content
from bs4 import BeautifulSoup

# List of URLs to scrape
urls = [
    'https://docs.langchain.com/oss/python/langchain/overview/',
    'https://docs.langchain.com/oss/python/langchain/philosophy/',
    'https://docs.langchain.com/oss/python/langchain/quickstart/'
]

# Function that downloads and processes the content of a single URL
def fetch_content(url):
    response = requests.get(url)   # Send GET request to fetch webpage
    soup = BeautifulSoup(response.content, 'html.parser')  # Parse HTML content
    print(f'Fetched {(len(soup.text))} characters from {url}')  # Print number of characters received

# List to store created thread objects
threads = []

# Loop through all URLs and create a separate thread for each
for url in urls:
    thread = threading.Thread(target=fetch_content, args=(url,))  # Create a thread for fetch_content()
    threads.append(thread)   # Store the thread in the list
    thread.start()           # Start the thread → begins downloading the URL immediately

# Wait for all threads to finish downloading
for thread in threads:
    thread.join()  # join() ensures the main program waits until thread completes

print("All web pages fetched.")  # This prints only after all threads are done
