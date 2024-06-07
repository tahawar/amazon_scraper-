from query_reader import read_queries
from scraper import AmazonScraper
from data_saver import save_data

def main():
    queries = read_queries('user_queries.json')
    for query in queries:
        scraper = AmazonScraper(query)
        products = scraper.scrape()
        save_data(products, query)

if __name__ == "__main__":
    main()
