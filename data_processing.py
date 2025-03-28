import requests
from bs4 import BeautifulSoup
import pandas as pd

# Fetch the HTML content
url = 'https://www.helmet.fi/en-US/Libraries_and_services'
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the HTML content
    soup = BeautifulSoup(response.text, 'html.parser')

    # Extract the library names and opening times
    libraries_info = []
    for optgroup in soup.find_all('optgroup'):
        zone = optgroup.get('label')
        for option in optgroup.find_all('option'):
            library_name = option.text.strip()
            library_id = option['value'].strip()
            # Here you would need to extract the opening times from another part of the page or a different page
            # since this information is not provided in the current selection
            libraries_info.append((library_id, library_name, zone))

    # Create a Pandas DataFrame for library names and another for locations
    df_libraries = pd.DataFrame(libraries_info, columns=['Library ID', 'Library Name', 'Zone'])

    # You can add another DataFrame for locations, but you need to extract that data similarly

    # Now, you can export this data to CSV
    df_libraries.to_csv('libraries.csv', index=False)

    # For locations, you would need to scrape the individual library pages or find another source for this data
else:
    print(f"Failed to retrieve content: {response.status_code}")
