from pymongo import MongoClient, ASCENDING, DESCENDING


class Mongo:
    def __init__(self):
        self._client = MongoClient('localhost', 27017)
        self._db = self._client['apsny_news']
        self._collection = self._db['news']

    def read_items(self, page, limit):
        result = self._collection.find().sort('article_time', DESCENDING).skip((page-1)*limit).limit(limit)
        a = []
        for i in result:
            a.append(i)
        return a

    def get_total_items(self):
        result = self._collection.count_documents({})
        return result



def read_item(slug):
    client = MongoClient('localhost', 27017)
    db = client['apsny_news']
    collection = db['news']
    result = collection.find_one({'slug': slug})
    return result
