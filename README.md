yCombinator Data Extractor
This Python script extracts data from the HTML block code of Y Combinator's Companies page and saves it to an Excel file.

Overview
The script works by:
1.Obtaining the HTML code from the target webpage after searching for companies.
2.Locally hosting the HTML code and providing its URL to the index.py Python program for data extraction.
3.Extracting the relevant data and saving it to an Excel file.

Usage
Prerequisites
*Python 3.x
*Libraries: 
1.requests: For making HTTP requests to fetch the webpage content.
2.beautifulsoup4: For parsing HTML content and extracting data.
3.pandas: For data manipulation and handling.
4.re: For regular expression operations.
5.urllib: For handling URLs and joining them.

Installation
1.Clone this repository:
git clone https://github.com/divyanshunishad/yCombinator-dataExtractor.git

2.Install the required libraries:
pip install -r requirements.txt


Usage
1.Run the index.py script:
python index.py
2.Follow the instructions to provide the locally hosted HTML URL.
3.Once the extraction is complete, the extracted data will be saved to an Excel file named company_details.xlsx.

