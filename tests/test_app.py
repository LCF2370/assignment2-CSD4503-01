from flask import jsonify

from app import flask_app
import unittest

class FlaskTestCase(unittest.TestCase):

    def setUp(self):
        self.app = flask_app.test_client()
        self.app.testing = True

    #Testing the index if post is implemented
    def test_index_get(self):
        response = self.app.post("/")
        print("The received status code: ", response.status_code)
        print("The expected status code: ", 405)
        self.assertEqual(first=response.status_code, second = 405)

    #Testing the index if get is implemented
    def test_index_post(self):
        response = self.app.get("/")
        print("The received status code: ", response.status_code)
        print("The expected status code: ", 200)
        self.assertEqual(first=response.status_code, second = 200)

    #Testing the index if the "Welcome to Dalmart" is found inside the page
    def test_index_data(self):
        response = self.app.get("/")
        print("Searching for: ", "Welcome to Dalmart")
        print("Found data for: ", response.data)
        self.assertIn(b'Welcome to Dalmart', response.data)

    #Testing the connection of MongoDB
    def test_mongo_conn(self):
        response = self.app.get("/mongo_conn")
        print(response.json)
        self.assertEqual(first=response.json, second={"status": "Successfully Connected to MongoDB"})

    #Testing insert data to MongoDB
    # def test_insert_data_to_db(db):
    #     db.collection.insert_one({"name": "Pen", "tag": "Office Supply", "price": 23.99})
    #     inserted_data = db.collection.fine_one({"name": "Pen", "tag": "Office Supply", "price": 23.99, "image_path": None})
    #     assert inserted_data is not None
    #     assert inserted_data["name"] == "Pen"