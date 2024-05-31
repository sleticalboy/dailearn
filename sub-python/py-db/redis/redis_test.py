import time

from redis import Redis


def samples(client: Redis):
    # 列出所有的 key
    all_keys = [item for item in client.keys('*') if 'proj-inf:' not in item]
    print(all_keys)
    print(client.set('hello', 'world', nx=False))
    print(client.get('hello'))
    client.append('hello', ' is ours, so do it now!')
    print(client.get('hello'))
    # 设置新值返回旧值
    print(client.getset('world', 'may not exists'))
    print(client.getset('world', 'new world'))
    print(client.getset('world', 'other world'))
    # 多个值存取
    print(client.mset({'name': 'binlee', 'age': 29, 'gender': 'male'}))
    print(client.mget(('name', 'age', 'gender')))
    print(dict(zip(all_keys, client.mget(all_keys))))
    # dict 操作
    print(client.hset('first_h', 'title', 'first hset',
                      mapping={'name': 'binlee', 'age': 29, 'gender': 'male'})
          )
    print(client.hget('first_h', 'title'))
    print(client.hget('first_h', 'name'))
    print(client.hget('first_h', 'age'))
    print(client.hget('first_h', 'gender'))
    print(client.hgetall('first_h'))
    print(client.hset('blog::1', 'date', int(time.time()), mapping={
        'title': 'first blog',
        'type': 'python',
        'content': 'python redis usage'}))
    print(client.hgetall('blog::1'))
    print(client.hmget('blog::1', ('title', 'type', 'content', 'date')))
    print(client.hkeys('first_h'))
    print(client.hkeys('blog::1'))
    # list 操作
    print(client.lpush('list::1', 'python', 'golang', 'java', 'android'))
    print(client.llen('list::1'))
    print(client.lpush('list::1', 'scrapy', 'gin', 'spring', 'mvvm'))
    print(client.llen('list::1'))
    print(client.lrange('list::1', 0, 99))
    while client.llen('list::1') > 4:
        print(client.rpop('list::1'))
    print(client.lrange('list::1', 0, 5))
    # set 操作
    print(client.sadd('set::1', 1, 2, 3))
    print(client.scard('set::1'))
    print(client.sadd('set::1', 1, 2, 3, 4, 5, 6))
    print(client.scard('set::1'))
    print(client.smembers('set::1'))
    print(client.zadd('zset::1', {'me': 10.0, 'tom': 0.01, 'jhon': 2, 'reek': 0.4}))
    print(client.zcard('zset::1'))
    print(client.zrange('zset::1', 0, -1, withscores=True))
    print(client.zrangebyscore('zset::1', 0, 3, withscores=True))
    # print(client.save())
    # print(client.dump('hello-dump.rdb'))
    pass


def hll(client: Redis):
    print(client.delete('users::like'))
    for i in range(1000):
        client.pfadd('users::like', i)
    print(client.pfcount('users::like'))
    pass


if __name__ == '__main__':
    # 以字符串形式打开数据库
    _client = Redis(db=1, password='foobared', decode_responses=True)
    # samples(_client)
    hll(_client)
    _client.close()
    pass
