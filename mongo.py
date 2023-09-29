from pymongo import MongoClient
def get_database():
    CONNECTION_STRING = "mongodb+srv://blabla:xxeOtlemQRxYPAMY@cluster0.m20qm5i.mongodb.net/?retryWrites=true&w=majority"
    client = MongoClient(CONNECTION_STRING)
    return client['reddit_posts']
if __name__ == "__main__":
    try:

        dbanme  = get_database()
    except:
        print("could not connect to mongodb")
        