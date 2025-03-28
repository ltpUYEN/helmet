import requests
import json
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


# The API endpoint, now without the language parameter.
api_url = "https://helmet.finna.fi/OrganisationInfo/OrganisationList/List?building=0&lookfor=&type=AllFields&filter%5B%5D=building_id%3A%220%22&filter%5B%5D=library_type_ss%3A%22library%22&sort=id"
# remove filter%5B%5D=available_in_language%3A%22en-gb%22

try:
    response = requests.get(api_url)
    response.raise_for_status()  # Check for HTTP errors

    data = response.json()  # Parse the JSON response

    # The library data is in data['organisations'].
    libraries = []
    for org in data['organisations']:
        # IMPORTANT: Check if the keys are different for the Finnish data!
        library_info = {
            'id': org['id'],
            'name': org.get('name','Not Found'),  # Use .get() for safety
            'short_name': org.get('shortName', 'Not Found'),
            'email': org.get('email', 'Not Found'),  # Handle missing data
            'homepage': org.get('homepage', 'Not Found'),
            'address': org.get('visitingAddress', {}).get('street', 'Not Found'), # Nested value
            'latitude': org.get('latitude', 'Not Found'),
            'longitude': org.get('longitude', 'Not Found'),
        }
        libraries.append(library_info)

    df = pd.DataFrame(libraries)
    print(df)

     #save to csv
    df.to_csv("libraries_finna_fi.csv", index=False) #different file name

except requests.exceptions.RequestException as e:
    print(f"Error fetching data: {e}")
except json.JSONDecodeError as e:
    print(f"Error decoding JSON: {e}")
except Exception as e:
     print(f"An unexpected error occurred:{e}")
