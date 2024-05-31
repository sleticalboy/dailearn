import time
import traceback

from redis.exceptions import ResponseError
from redis import Redis
from redis.client import Pipeline


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
    try:
        print(client.get('users::like'))
        all_keys.remove('users::like')
        print(dict(zip(all_keys, client.mget(all_keys))))
    except UnicodeDecodeError and ValueError as e:
        traceback.print_exception(e)
        pass
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
    print('dbsize: ', client.dbsize())
    pass


def hll(client: Redis):
    print(client.delete('users::like'))
    for i in range(1000):
        client.pfadd('users::like', i)
    print(client.pfcount('users::like'))
    pass


def expire(client: Redis):
    # print(client.set('expire-1', 'in 5s'))
    # print(client.expire('expire-1', 5))
    # print(client.set('expire-1', 'in 2s', px=2000))
    print(client.set('expire-1', 'in 2s', ex=2))
    print(client.get('expire-1'))
    while True:
        ttl = client.ttl('expire-1')
        if ttl < 0:
            break
        print(f'ttl: {ttl}s, wait 0.5s')
        time.sleep(0.5)
    print(client.get('expire-1'))
    pass


def pipline(pipe: Pipeline):
    print(pipe.set('p-msg-1', 'msg-1'))
    print(pipe.set('p-msg-2', 'msg-2'))
    print(pipe.append('p-msg-2', ' --'))
    print(pipe.sadd('p-s-fruits', 'apple', 'cherry', 'banana'))
    print(pipe.incrby('p::counter', 20))
    print(pipe.incrby('p::counter', 200))
    print(pipe.get('p-msg-2'))
    print(pipe.execute())
    pass


def script(client: Redis):
    print(client.eval("return 'hello lua world in redis'", 0))
    print(client.eval("return 3.14", 0))
    print(client.eval("return tostring(3.14)", 0))
    print(client.eval("local var=tostring(3.14); return var", 0))
    try:
        print(client.eval("number=10; return number", 0))
    except ResponseError as e:
        traceback.print_exception(e)
        pass
    pass


if __name__ == '__main__':
    # 以字符串形式打开数据库
    _client = Redis(db=1, password='foobared', decode_responses=True)
    samples(_client)
    hll(_client)
    expire(_client)
    pipline(_client.pipeline(transaction=False))
    script(_client)
    _client.close()
    pass
