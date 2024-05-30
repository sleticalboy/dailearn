from pymongo import MongoClient


def run_main():
    client = MongoClient('localhost', 27017)
    print(client.list_database_names())
    db = client.get_database('test')
    print(db.list_collection_names())
    for item in db.book.find():
        print(item)
    pass


if __name__ == '__main__':
    run_main()
    pass
