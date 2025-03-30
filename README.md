# Helmet.fi - Libraries Dataset and Analysis

## Project Overview

Driven by a personal interest in exploring local libraries, particularly while living in Helsinki, this project undertakes the collection, cleaning, and analysis of data from Helmet libraries. Serving Helsinki, Espoo, Kauniainen, and Vantaa, the data is sourced via web scraping using Python from the official Helmet website, subsequently processed, and analyzed using SQL to uncover useful insights about these libraries located in the Uusimaa region.

## Data Source

* **Primary Source:** [Helmet Libraries and Services Page](https://www.helmet.fi/en-US/Libraries_and_services)
* **Data Scraped:** Library Name, Library ID, Zone (Geographical Area).
* **Data Format:** Scraped into a Pandas DataFrame and exported as `libraries.csv`. Subsequently loaded into a SQL database table.
* **Note:** The provided Python script focuses on scraping names, IDs, and zones. The Library_URL values were not scraped directly but generated afterwards using Python code. This involved applying a discovered URL pattern to the existing DataFrame of library names/IDs.

## Tech Stack & Workflow

1.  **Web Scraping (Python):**
    * `requests`: To fetch the HTML content from the Helmet website.
    * `BeautifulSoup4`: To parse the HTML and extract relevant data elements.
    * `pandas`: To structure the scraped data into a DataFrame and export it to a CSV file (`libraries.csv`).
2.  **Data Storage:**
    * CSV file (`libraries.csv`) as an intermediate storage format.
  
3.  **Data Cleaning & Analysis (SQL):**
    * Standard SQL queries were used for data validation, cleaning, and performing analytical tasks.

**Workflow:**

## Tech Stack & Workflow

* **Tools:** Python (`requests`, `beautifulsoup4`, `pandas`), MySQL, MySQL Workbench, DBeaver, VS Code extension.
* **Workflow Summary:** Data Scraped (Python) -> Processed & URLs Generated (Python/Pandas) -> Exported to CSV -> Loaded into DBeaver -> Validated, Cleaned & Analyzed (MySQL in VsCode).

## Validation, Analysis & Code

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

**All detailed SQL scripts used for data validation and exploratory analysis are available in:**
[Data analysis](./data_analysis.sql)

**(Optional) The database schema definition, if created separately, can be found in:**
[Data analysis](./data_analysis.sql)

## Key Findings

* The dataset contains information on [Total Number] libraries across the Helmet network after cleaning.
* Data validation confirmed the uniqueness of `Library_ID`s after removing duplicates. NULL value checks were performed.
* The distribution of libraries varies across the zones (Espoo, Helsinki, Kauniainen, Vantaa), with [Zone Name] having the most libraries. 
* The dataset includes entries for mobile libraries operating within the network.

## Future Work / Limitations

* The data reflects the state of the Helmet website at the time of scraping and may become outdated.
* Scraping could be expanded to include detailed information like addresses, opening hours, contact details, and services offered by each library.
* Error handling in the Python script could be enhanced.
