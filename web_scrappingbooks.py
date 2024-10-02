import requests  # Used to send HTTP requests to websites and fetch the content
from bs4 import BeautifulSoup  # Used to parse and extract data from HTML content
import pandas as pd  # Used for organizing data into DataFrame and saving it to a CSV file
import time  # Used to add delays between requests to avoid overloading the server
import matplotlib.pyplot as plt  # Used for plotting graphs and visualizing data
from seaborn import histplot, countplot
import random  # Used to generate random numbers for random delays

# Introduce a random delay between 2 and 5 seconds to mimic human browsing behavior and avoid overwhelming the server
time.sleep(random.uniform(2, 5))

# Initialize empty lists to store book data and categories
books = []
categories = []

# Set base URL for paginated book listings and homepage URL for scraping categories
base_url = "https://books.toscrape.com/catalogue/page-{}.html"
home_url = "https://books.toscrape.com/"

# Fetch the homepage to scrape book categories
try:
    home_response = requests.get(home_url, timeout=10)  # Send a GET request to the homepage
    home_response.raise_for_status()  # Raise an error if the request failed
    home_soup = BeautifulSoup(home_response.content, 'html.parser')  # Parse the HTML content using BeautifulSoup

    # Extract categories from the navigation list in the homepage
    category_list = home_soup.find('ul', class_='nav nav-list').find('ul').find_all('li')
    for category in category_list:
        category_name = category.text.strip()  # Get category name and strip extra whitespace
        categories.append(category_name)  # Add category to the list
    print(f"Categories scraped: {categories}")  # Output the categories scraped

except requests.exceptions.RequestException as e:
    print(f"Error fetching {home_url}: {e}")  # Print error message if request fails

# Fetch the total number of pages dynamically by scraping the pagination info
try:
    first_page_response = requests.get(base_url.format(1), timeout=10)  # Send a GET request to the first page
    first_page_response.raise_for_status()  # Raise an error if the request failed
    first_page_soup = BeautifulSoup(first_page_response.content, 'html.parser')  # Parse the HTML content

    # Find the pagination element that indicates the total number of pages
    pagination = first_page_soup.find('li', class_='current').text.strip()
    total_pages = int(pagination.split()[-1])  # Extract the last number from pagination, which is the total page count
    print(f"Total pages to scrape: {total_pages}")  # Output the total number of pages

except requests.exceptions.RequestException as e:
    print(f"Error fetching page 1: {e}")  # Print error message if request fails
    total_pages = 1  # Default to 1 if unable to fetch the total number of pages

# Scrape each page of the book listings
for i in range(1, total_pages + 1):
    url = base_url.format(i)  # Format the URL for each page

    try:
        response = requests.get(url, timeout=10)  # Send a GET request to each page
        response.raise_for_status()  # Raise an error if the request failed
        soup = BeautifulSoup(response.content, 'html.parser')  # Parse the HTML content using BeautifulSoup
        ol = soup.find('ol')  # Find the ordered list (ol) containing the books
        articles = ol.find_all('article', class_='product_pod')  # Get all articles with the class 'product_pod'

        # Loop through each book on the page and extract details
        for article in articles:
            image = article.find('img')  # Find the image element
            title = image.attrs['alt']  # Get the title of the book from the 'alt' attribute

            star_tag = article.find('p')  # Find the paragraph tag containing the star rating
            star = star_tag['class'][1]  # Get the second class which corresponds to the star rating

            price = article.find('p', class_='price_color').text  # Find the price element and get its text
            price = float(price[1:])  # Convert the price string to a float after removing the currency symbol

            availability = article.find('p', class_='instock availability').text.strip()  # Find and strip availability text

            # Get the URL of the book page for more details
            book_url = article.find('h3').find('a')['href']
            book_url = "https://books.toscrape.com/catalogue/" + book_url  # Build the full URL for the book

            # Append the book details to the books list
            books.append([title, star, price, availability, book_url])

        # Introduce a delay between requests to avoid overloading the server
        time.sleep(2)

    except requests.exceptions.RequestException as e:
        print(f"Error fetching {url}: {e}")  # Print error message if request fails
        continue  # Skip the page and continue with the next one

# Create a DataFrame to store the scraped book data and save it to a CSV file
df = pd.DataFrame(books, columns=['Title', 'Star Rating', 'Price', 'Availability', 'Book URL'])  # Create a DataFrame
df.to_csv("books2.csv", index=False)  # Save the data to 'books2.csv' without row numbers
print("Books data saved to books2.csv")  # Confirm that data has been saved

# Data filtering: Filter books that have a 4 or 5-star rating and cost less than $20
df_filtered = df[df['Star Rating'].isin(['Four', 'Five'])]  # Filter books by star rating
df_filtered = df_filtered[df_filtered['Price'] < 20]  # Filter books with a price below $20
print("Filtered books with 4 or 5 stars and price below $20:")  # Output filtered results
print(df_filtered)

# Visualize the price distribution of all books using a histogram
histplot(df['Price'], kde=True)  # Plot a histogram with a Kernel Density Estimate (KDE)
plt.title('Price Distribution of Books')  # Add title to the plot
plt.xlabel('Price')  # Set x-axis label
plt.ylabel('Frequency')  # Set y-axis label
plt.show()  # Display the plot

# Visualize star ratings distribution using a bar plot
countplot(x='Star Rating', data=df)  # Plot the count of each star rating
plt.title('Star Rating Distribution')  # Add title to the plot
plt.xlabel('Star Rating')  # Set x-axis label
plt.ylabel('Count')  # Set y-axis label
plt.show()  # Display the plot
