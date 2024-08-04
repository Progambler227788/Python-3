import requests
from bs4 import BeautifulSoup

# URL of the university portal page to scrape
url = 'https://horizon.ucp.edu.pk/web/login'

# Send an HTTP request to fetch the webpage content
response = requests.get(url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse the HTML content of the webpage
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Extract all links from the webpage
    links = soup.find_all('a')
    
    # Print out information about each link
    for link in links:
        href = link.get('href')
        text = link.text.strip() if link.text else "No text available"  # Handle cases where link text is empty
        if href:  # Check if the link has an href attribute
            print(f"URL: {href} | Text: {text}")
else:
    print('Failed to retrieve the webpage. Status code:', response.status_code)
