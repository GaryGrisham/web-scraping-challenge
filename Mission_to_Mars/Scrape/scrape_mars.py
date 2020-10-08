from splinter import Browser
from bs4 import BeautifulSoup as bs
import time


def init_browser():
    # @NOTE: Replace the path with your actual path to the chromedriver
    executable_path = {"executable_path": "/usr/gsgbootcamp/Downloads/chromedriver"}
    return Browser("chrome", **executable_path, headless=False)


def scrape_info():
    browser = init_browser()

    # Visit url's
    url1 = "https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest"
    browser.visit(url1)

    time.sleep(1)

    # Scrape page into Soup
    html = browser.html
    soup = bs(html, "html.parser")

    # Get the latest mars news
    news_title = soup.find('div', class_='article_teaser_body')
    news_p = soup.find('div', class_='article_teaser_body' )

    # Store data in a dictionary
    mars_data = {
        "news_title": news_title,
        "news_p": news_p
    }

    # Close the browser after scraping
    browser.quit()

    # Return results
    return mars_data
