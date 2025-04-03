# Helmet.fi - Helsinki Metropolitan Area Libraries Dataset and Analysis

## Project Overview

Driven by a personal interest in exploring local libraries, particularly while living in Helsinki, this project undertakes the collection, cleaning, and analysis of data from Helmet libraries. Serving Helsinki, Espoo, Kauniainen, and Vantaa, the data is sourced via web scraping using Python from the official Helmet website, subsequently processed, and analyzed using SQL to uncover useful insights about these libraries located in the Uusimaa region.

## Data Source

* **Primary Source:** [Helmet Libraries and Services Page](https://www.helmet.fi/en-US/Libraries_and_services)
* **Data Scraped:** Library Name, Library ID, Zone (Geographical Area).
* **Data Format:** Scraped into a Pandas DataFrame and exported as `libraries.csv`. Subsequently loaded into a SQL database table.
* **Note:** The provided Python script focuses on scraping names, IDs, and zones. The Library_URL values were not scraped directly but generated afterwards using Python code. This involved applying a discovered URL pattern to the existing DataFrame of library names/IDs.

## Tech Stack & Workflow

* **Tools:** Python (`requests`, `beautifulsoup4`, `pandas`), MySQL, MySQL Workbench, DBeaver, VS Code extension.
* **Workflow Summary:** Data Scraped (Python) -> Processed & URLs Generated (Python/Pandas) -> Exported to CSV -> Loaded into DBeaver -> Validated, Cleaned & Analyzed (MySQL in VsCode).

## Validation, Analysis & Code

Data validation was performed using MySQL to ensure the integrity and consistency of the Helmet library data. Key validation steps included:
* Standardizing column names for consistency (e.g., renaming `Library ID` to `Library_ID`).
* Identifying and removing duplicate library entries based on `Library_ID`.
* Checking key fields such as `Library_ID`, `Library_Name`, `Zone`, and `Library_URL` for any NULL values.

Subsequent analysis using SQL explored several aspects of the collected library data:
* Calculating the total count of libraries after data cleaning.
* Determining the number of libraries within each service zone (Espoo, Helsinki, Kauniainen, Vantaa).
* Identifying the library with the longest recorded name.
* Searching for and listing mobile library units.

* Scripts & Output example

```sql
--8. Select libraries in Helsinki, excluding specialized types 
SELECT *
FROM libraries
WHERE ZONE = 'Helsinki'
  AND library_Name NOT RLIKE 'mobile|hospital|service|children';
```

| Library_ID | Library_Name                  | Zone     | Library_URL                                                               |
|------------|-------------------------------|----------|---------------------------------------------------------------------------|
| 84921      | Arabianranta Library          | Helsinki | https://www.helmet.fi/en-US/Libraries_and_services/Arabianranta_Library |
| 84878      | Etelä-Haaga Library           | Helsinki | https://www.helmet.fi/en-US/Libraries_and_services/Etelä-Haaga_Library    |
| 86476      | Helsinki Central Library Oodi | Helsinki | https://www.helmet.fi/en-US/Libraries_and_services/Helsinki_Central_Library_Oodi |
| 84911      | Herttoniemi Library           | Helsinki | https://www.helmet.fi/en-US/Libraries_and_services/Herttoniemi_Library    |
| 84927      | Itäkeskus Library             | Helsinki | https://www.helmet.fi/en-US/Libraries_and_services/Itäkeskus_Library      |
| 84854      | Jakomäki Library              | Helsinki | https://www.helmet.fi/en-US/Libraries_and_services/Jakomäki_Library       |
| 86406      | Jätkäsaari Library            | Helsinki | https://www.helmet.fi/en-US/Libraries_and_services/Jätkäsaari_Library     |
| 84854      | Jakomäki Library              | Helsinki | https://www.helmet.fi/en-US/Libraries_and_services/Jakomäki_Library       |
| 84861      | Käpylä Library                | Helsinki | https://www.helmet.fi/en-US/Libraries_and_services/Käpylä_Library         |
| 86738      | Kalasatama Library            | Helsinki | https://www.helmet.fi/en-US/Libraries_and_services/Kalasatama_Library     |
| 84860      | Kallio Library                | Helsinki | https://www.helmet.fi/en-US/Libraries_and_services/Kallio_Library         |
| 84847      | Kannelmäki Library            | Helsinki | https://www.helmet.fi/en-US/Libraries_and_services/Kannelmäki_Library     |
| 84863      | Kontula Library               | Helsinki | https://www.helmet.fi/en-US/Libraries_and_services/Kontula_Library        |
| 84848      | Laajasalo Library             | Helsinki | https://www.helmet.fi/en-US/Libraries_and_services/Laajasalo_Library      |
| 84864      | Lauttasaari Library           | Helsinki | https://www.helmet.fi/en-US/Libraries_and_services/Lauttasaari_Library    |
| 84859      | Malmi Library                 | Helsinki | https://www.helmet.fi/en-US/Libraries_and_services/Malmi_Library          |
| 84866      | Malminkartano Library         | Helsinki | https://www.helmet.fi/en-US/Libraries_and_services/Malminkartano_Library  |
| 84857      | Maunula Library               | Helsinki | https://www.helmet.fi/en-US/Libraries_and_services/Maunula_Library        |
| 84923      | Multilingual Library          | Helsinki | https://www.helmet.fi/en-US/Libraries_and_services/Multilingual_Library   |
| 84867      | Munkkiniemi Library           | Helsinki | https://www.helmet.fi/en-US/Libraries_and_services/Munkkiniemi_Library    |
| 84883      | Myllypuro Library             | Helsinki | https://www.helmet.fi/en-US/Libraries_and_services/Myllypuro_Library      |
| 84862      | Oulunkylä Library             | Helsinki | https://www.helmet.fi/en-US/Libraries_and_services/Oulunkylä_Library      |
| 84852      | Paloheinä Library             | Helsinki | https://www.helmet.fi/en-US/Libraries_and_services/Paloheinä_Library      |
| 84924      | Pasila Library                | Helsinki | https://www.helmet.fi/en-US/Libraries_and_services/Pasila_Library         |
| 84865      | Pitäjänmäki Library           | Helsinki | https://www.helmet.fi/en-US/Libraries_and_services/Pitäjänmäki_Library    |
| 84879      | Pohjois-Haaga Library         | Helsinki | https://www.helmet.fi/en-US/Libraries_and_services/Pohjois-Haaga_Library  |
| 84858      | Pukinmäki Library             | Helsinki | https://www.helmet.fi/en-US/Libraries_and_services/Pukinmäki_Library      |
| 84912      | Rikhardinkatu Library         | Helsinki | https://www.helmet.fi/en-US/Libraries_and_services/Rikhardinkatu_Library  |
| 84868      | Roihuvuori Library            | Helsinki | https://www.helmet.fi/en-US/Libraries_and_services/Roihuvuori_Library     |
| 84871      | Suomenlinna Library           | Helsinki | https://www.helmet.fi/en-US/Libraries_and_services/Suomenlinna_Library    |
| 84881      | Suutarila Library             | Helsinki | https://www.helmet.fi/en-US/Libraries_and_services/Suutarila_Library      |
| 84851      | Töölö Library                 | Helsinki | https://www.helmet.fi/en-US/Libraries_and_services/Töölö_Library          |
| 84776      | Tapanila Library              | Helsinki | https://www.helmet.fi/en-US/Libraries_and_services/Tapanila_Library       |
| 84845      | Tapulikaupunki Library        | Helsinki | https://www.helmet.fi/en-US/Libraries_and_services/Tapulikaupunki_Library |
| 84870      | Vallila Library               | Helsinki | https://www.helmet.fi/en-US/Libraries_and_services/Vallila_Library        |
| 84919      | Viikki Library                | Helsinki | https://www.helmet.fi/en-US/Libraries_and_services/Viikki_Library         |
| 84880      | Vuosaari Library              | Helsinki | https://www.helmet.fi/en-US/Libraries_and_services/Vuosaari_Library       |


**All detailed SQL scripts used for data validation and exploratory analysis are available in:**
[Data analysis](./data_analysis.sql)

**All Python scripts used for data processing are available in:** 
[Data processing](./data_processing.py)

## Key Findings

* The dataset contains information on [Total Number] libraries across the Helmet network after cleaning.
* Data validation confirmed the uniqueness of `Library_ID`s after removing duplicates. NULL value checks were performed.
* The distribution of libraries varies across the zones (Espoo, Helsinki, Kauniainen, Vantaa), with [Zone Name] having the most libraries. 
* The dataset includes entries for mobile libraries operating within the network.

## Future Work / Limitations

* The data reflects the state of the Helmet website at the time of scraping and may become outdated.
* Scraping could be expanded to include detailed information like addresses, opening hours, contact details, and services offered by each library.
* Error handling in the Python script could be enhanced.
