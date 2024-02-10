import pymongo
import pandas as pd
import os
from dotenv import load_dotenv

load_dotenv()

URL = os.getenv("URL")

# Connect to MongoDB
client = pymongo.MongoClient(URL)
db = client["signLang"]
collection = db["mycollection"]

# Load Kaggle dataset (assuming it's a CSV file)
train_data = pd.read_csv(
    "data/sign_mnist_train/sign_mnist_train.csv")
test_data = pd.read_csv(
    "F:\MongoDB\signLanguage\data\sign_mnist_test\sign_mnist_test.csv")

data = pd.concat([train_data, test_data], ignore_index=True)


# Convert data to dictionary format (assuming each row represents a document)
data_dict = data.to_dict(orient="records")

try:
    # Attempt to insert data into MongoDB
    collection.insert_many(data_dict)
    print("Data inserted successfully!")
except Exception as e:
    print("An error occurred:", e)
finally:
    # Close the MongoDB connection
    client.close()
