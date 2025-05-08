from mongoengine import connect



def connectToDb(db_name):
    database = connect(
        db=db_name,
        host="localhost",
        port=27017,
    )