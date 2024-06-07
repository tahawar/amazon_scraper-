from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import time
import random
import logging
from product import Product

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class AmazonScraper:
    def __init__(self, query):
        self.query = query
        self.base_url = "https://www.amazon.com/s"
        self.chrome_driver_path = 'C:\\Users\\pc\\Desktop\\chromedriver-win64\\chromedriver.exe'  # Update with your actual path
        self.service = Service(self.chrome_driver_path)
        self.options = Options()
        self.options.add_argument("--headless")  # Run in headless mode (no browser UI)
        self.options.add_argument("start-maximized")
        self.options.add_argument("disable-infobars")
        self.options.add_argument("--disable-extensions")

    def get_search_url(self, page):
        return f"{self.base_url}?k={self.query}&page={page}"

    def fetch_page(self, url):
        driver = webdriver.Chrome(service=self.service, options=self.options)
        driver.get(url)
        time.sleep(random.uniform(2, 5))  # Random delay to mimic human interaction
        page_content = driver.page_source
        driver.quit()
        return page_content

    def parse_product(self, item):
        try:
            title_element = item.select_one('span.a-text-normal')
            title = title_element.text.strip() if title_element else "N/A"

            reviews_element = item.select_one('span.a-size-base')
            total_reviews = reviews_element.text.strip() if reviews_element else "0"

            price = "N/A"
            price_element = item.select_one('span.a-price')
            if price_element:
                price_offscreen = price_element.select_one('span.a-offscreen')
                if price_offscreen:
                    price = price_offscreen.text.strip()
                else:
                    price_whole = price_element.select_one('span.a-price-whole')
                    price_fraction = price_element.select_one('span.a-price-fraction')
                    price_symbol = price_element.select_one('span.a-price-symbol')
                    if price_symbol and price_symbol.text.strip() == "$":
                        if price_whole and price_fraction:
                            price = f"${price_whole.text.strip()}.{price_fraction.text.strip()}"
                        elif price_whole:
                            price = f"${price_whole.text.strip()}"
                        elif price_fraction:
                            price = f"$0.{price_fraction.text.strip()}"

            image_element = item.select_one('img.s-image')
            image_url = image_element['src'] if image_element else "N/A"

            # Ensure the product has valid details before returning
            if title != "N/A" and image_url != "N/A":
                return Product(title, total_reviews, price, image_url)
        except Exception as e:
            logger.error(f"Error parsing product: {e}")
        return None

    def scrape(self):
        products = []
        for page in range(1, 21):
            url = self.get_search_url(page)
            try:
                logger.info(f"Fetching page: {url}")
                page_content = self.fetch_page(url)
                soup = BeautifulSoup(page_content, 'html.parser')
                items = soup.select('div.s-main-slot div.s-result-item, div.s-main-slot div.ad-holder')  # Including sponsored items
                for item in items:
                    product = self.parse_product(item)
                    if product:
                        products.append(product.to_dict())
                logger.info(f"Scraped {len(products)} products so far.")
            except Exception as e:
                logger.error(f"An error occurred: {e}")
            time.sleep(random.uniform(1, 3))  # Random delay between 1 to 3 seconds
        return products

if __name__ == "__main__":
    scraper = AmazonScraper("headphones")
    products = scraper.scrape()
    print(products)
