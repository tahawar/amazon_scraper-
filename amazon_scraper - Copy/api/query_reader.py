import json

def read_queries(file_path):
    with open(file_path, 'r') as file:
        queries = json.load(file)
    return queries

if __name__ == "__main__":
    queries = read_queries('user_queries.json')
    print(queries)
