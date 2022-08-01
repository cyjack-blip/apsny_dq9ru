from pymongo import MongoClient, ASCENDING, DESCENDING


def read_items(limit):
    client = MongoClient('localhost', 27017)
    db = client['apsny_news']
    collection = db['news']
    result = collection.find().sort('article_time', DESCENDING).limit(limit)

    a = []
    for i in result:
        a.append(i)

    return a


def read_item(slug):
    client = MongoClient('localhost', 27017)
    db = client['apsny_news']
    collection = db['news']
    result = collection.find_one({'slug': slug})
    return result
