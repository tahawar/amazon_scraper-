from datetime import datetime

class Product:
    def __init__(self, title, total_reviews, price, image_url, additional_fields=None):
        self.title = title
        self.total_reviews = total_reviews
        self.price = price
        self.image_url = image_url
        self.additional_fields = additional_fields or {}
        self.creation_timestamp = datetime.now().isoformat()
        self.update_timestamp = datetime.now().isoformat()
        self.scrape_date = datetime.now().date().isoformat()

    def to_dict(self):
        return {
            "title": self.title,
            "total_reviews": self.total_reviews,
            "price": self.price,
            "image_url": self.image_url,
            "additional_fields": self.additional_fields,
            "creation_timestamp": self.creation_timestamp,
            "update_timestamp": self.update_timestamp,
            "scrape_date": self.scrape_date,
        }
