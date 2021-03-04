from csv import reader
import os


def get_object_data(file):
    with open(file, "r") as f:
        r = reader(f)
        # Yield the header row
        yield next(r)
        for row in r:
            # Check if the object has an image availble
            if row[1]:
                yield row[0]


def insert_object_ids(db):
    from app.models import Object

    if db.session.query(Object).first():
        return "Database already up to date"
    
    basedir = os.path.abspath(os.path.dirname(__file__))
    object_csv_file = os.path.join(basedir, "data/202001-rma-csv-collection.csv")

    object_ids = []

    for object_id in get_object_data(object_csv_file):
        db.session.add(Object(number=object_id))

    db.session.bulk_save_objects(object_ids)
    db.session.commit()

    # print(object_ids)

    return "Added object IDs to database"
