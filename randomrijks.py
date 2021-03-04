from app import create_app, db

app = create_app()

@app.cli.command()
def seed_database():
    """Add objects ids from csv file to database"""

    from app.seed.object_ids import insert_object_ids
    message = insert_object_ids(db)

    print(message)
