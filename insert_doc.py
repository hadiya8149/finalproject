from mongo import get_database

dbname = get_database()
print(dbname)
collection_name = dbname["posts"]
item = {
    "title":"",
    "text": "",
    "score":float, 
    "vader_score":float

}
collection_name.insert_one(item)