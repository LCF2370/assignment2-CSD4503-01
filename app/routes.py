from dotenv import load_dotenv
from pymongo import MongoClient
import os

from app import flask_app, render_template, jsonify

#Read the .env file
load_dotenv()

# Username and Password
db_username = os.environ["MONGODB_USERNAME"]
db_password = os.environ.get("MONGODB_PASSWORD")

# Creates the Mongodb Client
mongodb_client = MongoClient(f"mongodb+srv://{db_username}:{db_password}@cluster0.dr7cs.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")

# To access database from the client
db = mongodb_client["flask_app"]
products_collection = db["products"]

# Empty table
products_collection.drop()

# To add data to MongoDB we can use the client and the functions insert_many() or insert_one()
# insert_many() allows you to add a list of JSONs
# insert_one() allows you to add a single JSON

mock_data = [{"name": "Laptop", "tag": "Electronics", "price": 899.99, "image_path": "/static/images/laptop.png"},
             {"name": "Coffee Mug", "tag": "Kitchenware", "price": 12.99, "image_path": "/static/images/mug.png"},
             {"name": "Headphones", "tag": "Electronics", "price": 199.99, "image_path": "/static/images/headphones.png"},
             {"name": "HP Laptop", "tag": "Electronics", "price": 525.99, "image_path": "/static/images/hp-laptop.png"},
             {"name": "Jaei Coffee Mug", "tag": "Kitchenware", "price": 8.99, "image_path": "/static/images/jaei-mug.png"},
             {"name": "Dell Headphones", "tag": "Electronics", "price": 120.99, "image_path": "/static/images/dell-headphones.png"}]

products_collection.insert_many(mock_data)

@flask_app.route("/")
def home():
    return render_template("home.html")

@flask_app.route("/products")
def products():
    product = list(products_collection.find())
    return render_template("products.html", products=product)

@flask_app.route("/mongo_conn")
def mongo_conn():
    client = mongodb_client
    client.products.command('ping')
    return jsonify({"status": "Successfully Connected to MongoDB"}), 200