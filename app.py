from flask import Flask, render_template
from pymongo import MongoClient

# Creates the application instance
app = Flask(__name__)

# Creates the Mongodb Client
mongodb_client = MongoClient("mongodb+srv://root:s0GVaV6lBLtaXrZg@cluster0.dr7cs.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")

# To access database from the client
db = mongodb_client["app"]
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

@app.route("/")
def index():
    return render_template("home.html")

@app.route("/products")
def products():
    products = list(products_collection.find())
    return render_template("products.html", products=products)

app.run(host="0.0.0.0", port=5000)