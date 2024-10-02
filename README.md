# Project Overview
This project is a web scraping and data analysis task designed to gather book-related data from [Books to Scrape]([url](https://books.toscrape.com/)). The aim is to extract information such as book titles, star ratings, prices, availability, and URLs, and then analyze the data to gain insights into pricing trends, ratings distribution, and other metrics.

The project leverages Python libraries like requests for fetching web pages, BeautifulSoup for parsing HTML, pandas for data handling, and matplotlib/seaborn for data visualization.
# Features
1.Scrapes book titles, star ratings, prices, availability, and URLs
2.Extracts book categories dynamically
3.Handles pagination to scrape multiple pages
4.Filters books with 4 and 5-star ratings priced below $20
5.Generates visualizations for price distribution and star rating counts
6.Implements error handling and timeouts to avoid server overload
# Libraries Used
1.requests: Fetches the HTML content from the website pages.
2.BeautifulSoup: Parses and navigates the HTML structure to extract useful data.
3.pandas: Organizes the extracted data into a structured format (DataFrame) and facilitates data analysis.
4.time & random: Adds randomized delays between requests to prevent overloading the server.
5.matplotlib & seaborn: Generates plots for visualizing the price and star rating distributions.
# Setup Instructions
Clone the repository:
git clone https://github.com/username/web-scraping-books-analysis.git
Install the required libraries:
pip install requests beautifulsoup4 pandas matplotlib seaborn
Run the script
# Data Fields
The data extracted and saved includes:

Title: The name of the book.
Star Rating: A rating for the book from one to five stars.
Price: The price of the book in GBP.
Availability: Stock status (e.g., In stock).
Book URL: The direct link to the book's page.
# Output
CSV File: The scraped data is saved to a file called books2.csv.
Filtered Books: A subset of books with a star rating of 4 or 5 and priced below $20 is displayed.
# Visualizations:
A histogram showing the price distribution of all books.
A bar chart displaying the count of books by star rating.
Visualizations
Price Distribution:
Star Rating Count:
# Error Handling
Handles exceptions such as timeouts and invalid URLs.
Implements delays between requests to prevent overloading the server.
# Use Case
This project demonstrates how web scraping can be used in real-world data analysis scenarios. The extracted data can be utilized to perform various forms of analysis, including:

Price trends of books across different genres.
Correlation between star ratings and book prices.
Availability analysis.
# Contribution
Feel free to fork this project and add any additional features, such as:

Extracting more data fields (e.g., book descriptions, number of reviews).
Adding more advanced data visualizations.
Optimizing the scraping process.
# License
This project is open-source and available under the MIT License.















