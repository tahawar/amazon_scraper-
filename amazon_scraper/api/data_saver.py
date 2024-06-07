import json

def save_data(data, query):
    file_name = f"{query}.json"
    with open(file_name, 'w') as file:
        json.dump(data, file, indent=4)

if __name__ == "__main__":
    sample_data = [{"title": "Sample Product", "price": "$19.99"}]
    save_data(sample_data, "sample_query")
