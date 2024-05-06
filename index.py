import requests
from bs4 import BeautifulSoup
import pandas as pd
import re
from urllib.parse import urljoin

# Get the web page content
url = "http://127.0.0.1:5500/page.html"
response = requests.get(url)

# Parse the web page content with BeautifulSoup
soup = BeautifulSoup(response.text, 'html.parser')

# Extract the company details into a list of dictionaries
companies = []

for company in soup.find_all('a', class_='_company_99gj3_339'):
    details = {}

    details['company-page'] = urljoin("https://www.ycombinator.com", company['href'].strip())
    details['name'] = re.sub(r'\s+', ' ', company.find('span', class_='_coName_99gj3_454').text.strip())
    details['location'] = re.sub(r'\s+', ' ', company.find('span', class_='_coLocation_99gj3_470').text.strip())
    details['description'] = re.sub(r'\s+', ' ', company.find('span', class_='_coDescription_99gj3_479').text.strip())

    # Extract the industries and tags
    industries = []
    for industry in company.find_all('a', class_='_tagLink_99gj3_1024'):
        industries.append(industry.text)

    # Remove \n, \r, and [ ] from industries values without affecting white spaces
    industries_cleaned = [
        ' '.join(filter(None, industry.replace('\n', '').replace('\r', '').replace('[', '').replace(']', '').split()))
        for industry in industries]
    details['industries-details'] = industries_cleaned

    companies.append(details)

# Create a pandas DataFrame from the list of dictionaries
df = pd.DataFrame(companies)

# Save the DataFrame to an Excel file
excel_file = "company_details.xlsx"
df.to_excel(excel_file, index=False)

print("Company details saved to", excel_file)
