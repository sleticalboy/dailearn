from pymongo import MongoClient
from pymongo.database import Database
from bson import ObjectId


def basic_samples(db: Database):
    print(db.list_collection_names())
    # 单个插入
    print(db.book.insert_one({'title': 0, 'seq': -1}))
    # 批量插入
    # books = []
    # for i in range(20):
    #     books.append({'title': str(i * i + 1), 'seq': i})
    # print(db.get_collection('book').insert_many(books))
    # 条件查询
    print(db.get_collection('book').find_one({'title': 0}))
    for item in db.get_collection('book').find({'seq': {'$gt': 3, '$lt': 10}}):
        print(item)
    print()
    for item in db.get_collection('book').find({'title': {'$regex': r'^\d$'}}):
        print(item)
    print()
    for item in db.get_collection('book').find({'title': {'$regex': r'\d'}}):
        print(item)
    print()
    # 查询所有，不显示 _id 字段
    for item in db.book.find({}, {'_id': 0}):
        print(item, end=' ')
    # 删除
    print(db.get_collection('book').delete_many({'title': 0, 'seq': -1}))
    print(db.book.insert_many([{'hello': 'mongodb world'}, {'hello': 'mongodb test'}]))
    print(db.get_collection('book').delete_many({'hello': {'$regex': r'mongodb'}}))
    print(db.get_collection('book').delete_many({
        '_id': {
            '$in': [
                ObjectId('6658726a78b8994e7754be4b'),
                ObjectId('66592c530a5cf46d54808d93'),
                ObjectId('66592c530a5cf46d54808d94'),
                ObjectId('66592c530a5cf46d54808d95'),
            ]
        }
    }))
    pass


def capped_(db: Database):
    table = db.get_collection('logs')
    if table is not None:
        table.drop()
    # 固定大小的集合，数据达到限定后，后续插入的数据会覆盖之前的
    table = db.create_collection("logs", capped=True, size=4096*2)
    print(table)
    rows = []
    for i in range(2000):
        rows.append({'tag': f'row-{i + 1}', 'id': id(i)})
        pass
    table.insert_many(rows)
    print(table.create_index({'tag': 1, 'id': 1}))
    for item in table.find({}, {'_id': 0}):
        print(item)
    # 查看集合大小
    print(db.command('dbstats'))
    print(db.command('collstats', 'logs'))
    pass


if __name__ == '__main__':
    _client = MongoClient('localhost', 27017)
    print(_client.list_database_names())
    _db = _client.get_database('test')
    # basic_samples(_client)
    capped_(_db)
    _client.close()
    pass
