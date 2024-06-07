# from flask import Flask, jsonify, send_file
# from flask_cors import CORS
# import os

# app = Flask(__name__)
# CORS(app)

# BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# @app.route('/api/user_queries.json')
# def get_user_queries():
#     return send_file(os.path.join(BASE_DIR, 'user_queries.json'))

# @app.route('/api/<category>.json')
# def get_category_data(category):
#     filename = f"{category}.json"
#     file_path = os.path.join(BASE_DIR, filename)
#     if os.path.exists(file_path):
#         return send_file(file_path)
#     else:
#         return jsonify({"error": "Category not found"}), 404

# if __name__ == '__main__':
#     app.run(host='0.0.0.0', port=5000)


# from flask import Flask, jsonify, send_file
# from flask_cors import CORS
# import os

# app = Flask(__name__)
# CORS(app)

# BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# @app.route('/api/user_queries.json')
# def get_user_queries():
#     return send_file(os.path.join(BASE_DIR, 'user_queries.json'))

# @app.route('/api/<category>.json')
# def get_category_data(category):
#     filename = f"{category}.json"
#     file_path = os.path.join(BASE_DIR, filename)
#     if os.path.exists(file_path):
#         return send_file(file_path)
#     else:
#         return jsonify({"error": "Category not found"}), 404

# if __name__ == '__main__':
#     app.run(host='0.0.0.0', port=5000)


from flask import Flask, jsonify, send_file
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

@app.route('/api/user_queries.json')
def get_user_queries():
    return send_file(os.path.join(BASE_DIR, 'user_queries.json'))

@app.route('/api/<category>.json')
def get_category_data(category):
    filename = f"{category}.json"
    file_path = os.path.join(BASE_DIR, filename)
    if os.path.exists(file_path):
        return send_file(file_path)
    else:
        return jsonify({"error": "Category not found"}), 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
