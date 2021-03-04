from csv import reader
import pandas as pd
import os


def insert_object_ids(db):
    from app.models import Object

    if db.session.query(Object).first():
        return "Database already up to date"

    basedir = os.path.abspath(os.path.dirname(__file__))
    object_csv_file = os.path.join(basedir, "data/202001-rma-csv-collection.csv")

    object_ids = []

    # Utilize Panda's chunk size functionality to read the csv file in smaller batches
    # to circumvent the servers memory constraints
    chunk_size = 1000
    count = 1
    for chunk in pd.read_csv(object_csv_file, chunksize=chunk_size):
        for row in chunk.iterrows():
            if row[1]["objectImage"]:
                object_ids.append(Object(number=row[1]["objectInventoryNumber"]))

    # with open(object_csv_file, "r") as f:
    #     r = reader(f)
    #     for row in r:
    #         # Check if the object has an image availble
    #         if row[1]:
    #             object_ids.append(Object(number=row[0]))

    db.session.bulk_save_objects(object_ids)
    db.session.commit()

    return "Added object IDs to database"
