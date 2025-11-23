import os
import sys
import json

# Load environment variables from the .env file
from dotenv import load_dotenv
load_dotenv()

# Fetch MongoDB connection URL from the environment
MONGO_DB_URL = os.getenv("MONGO_DB_URL")
print(MONGO_DB_URL)   # (Optional) To check if the URL is loaded properly

import certifi
ca = certifi.where()   # Provides the path to SSL certificates (used for secure MongoDB connection)

import pandas as pd
import numpy as np
import pymongo

# Custom exception and logging from your project
from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logging

class NetworkDataExtract():
    """
    This class handles:
    1. Reading CSV data
    2. Converting it into JSON format (MongoDB friendly)
    3. Inserting the data into a MongoDB collection
    """
    def __init__(self):
        try:
            pass   # Currently no initialization needed, but the try-except ensures error logging
        except Exception as e:
            raise NetworkSecurityException(e, sys)

    def csv_to_json_convertor(self, file_path):
        """
        Converts CSV file into a list of JSON records.
        MongoDB accepts data in dictionary format, not CSV.
        """
        try:
            data = pd.read_csv(file_path)                      # Read the CSV file
            data.reset_index(drop=True, inplace=True)          # Reset index to avoid issues while converting
            records = list(json.loads(data.T.to_json()).values())   # Convert DataFrame to JSON-serializable list
            return records
        except Exception as e:
            raise NetworkSecurityException(e, sys)

    def insert_data_mongodb(self, records, database, collection):
        """
        Inserts records into a MongoDB collection.
        """
        try:
            self.database = database
            self.collection = collection
            self.records = records

            # Connect to MongoDB
            self.mongo_client = pymongo.MongoClient(MONGO_DB_URL)

            # Select database and collection
            self.database = self.mongo_client[self.database]
            self.collection = self.database[self.collection]

            # Insert multiple records at once
            self.collection.insert_many(self.records)

            return len(self.records)  # Return how many rows were inserted
        except Exception as e:
            raise NetworkSecurityException(e, sys)

if __name__ == '__main__':
    # File and database configuration
    FILE_PATH = "Network_Data/phisingData.csv"   # Path to CSV file
    DATABASE = "KRISHAI"                         # MongoDB database name
    Collection = "NetworkData"                   # MongoDB collection name

    # Create object of the class
    networkobj = NetworkDataExtract()

    # Convert CSV to JSON records
    records = networkobj.csv_to_json_convertor(file_path=FILE_PATH)
    print(records)   # Optional: View converted records

    # Insert records into MongoDB
    no_of_records = networkobj.insert_data_mongodb(records, DATABASE, Collection)
    print(no_of_records, "records inserted successfully!")
