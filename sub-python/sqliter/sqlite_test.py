import logging
import sqlite3
import threading

import requests

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(levelname)s %(message)s')

g_lock = threading.Lock()


def task(conn, delta=0):
    tag = threading.current_thread().name
    cursor = conn.cursor()
    logging.info(f'conn: {conn}, cursor: {cursor}, {threading.current_thread()}')
    for i in range(5):
        with g_lock:
            cursor.execute(
                f"insert into user (_name, _email, _password) values "
                f"('bin.li-{i + delta}', '{tag}', '{tag}-{i + delta}');")
            conn.commit()
    print(conn.total_changes)


def run_sqlite():
    conn = sqlite3.connect('sqler.db')
    cursor = conn.cursor()
    logging.info(f'conn: {conn}, cursor: {cursor}')
    cursor.execute('''create table if not exists user(
    _id integer primary key autoincrement default 0 ,
    _name varchar(32) not null ,
    _email varchar(32) not null ,
    _password varchar(32) not null ,
    _token text default null
    );''')
    for i in range(20):
        cursor.execute(
            "insert into user (_name, _email, _password) values ('bin.li', 'bin.li@quvideo.com', 'hello')")
    conn.commit()

    cursor.execute('create index if not exists idx_uname on user (_name);')
    cursor.execute('create index if not exists idx_uemail on user (_email);')
    cursor.execute('create index if not exists idx_up on user (_password);')
    cursor.execute('create index if not exists idx_une on user (_name, _email);')
    cursor.execute('drop index idx_up;')

    columns = cursor.execute('PRAGMA table_info(user)').fetchall()
    columns = [it[1] for it in columns]
    logging.info(f'columns: {columns}')

    return

    cursor.execute('select * from user')
    # 全部数据
    # res = cursor.fetchall()
    while True:
        # 分页获取
        res = cursor.fetchmany(size=20)
        logging.info(f'fetch 20, res: {len(res)}, type: {type(res)}')
        if not res or len(res) == 0:
            break
        if res and len(res) > 0:
            for i, val in enumerate(res):
                logging.info(f'{dict(zip(columns, val))}')
                pass
    cursor.execute('delete from user where _name=?', ('bin.li',))
    res = cursor.fetchall()
    logging.info(res)
    cursor.execute('alter table user add column _results text default null')
    cursor.execute('alter table user drop column _results')
    res = cursor.fetchall()
    logging.info(res)

    cursor.close()
    conn.close()
    pass


def get_robots_rules(url: str):
    if not url.endswith('robots.txt'):
        url = url + ('robots.txt' if '/' == url[-1] else '/robots.txt')
    with requests.get(url) as res:
        lines = res.text.splitlines()
        rules = {}
        disallow = []
        started = False
        for i in range(len(lines)):
            line = lines[i]
            if line == '' or line.startswith('#') or line.startswith('Sitemap:'):
                continue
                pass
            if line.startswith('User-agent:'):
                disallow = rules.setdefault(line.split()[1].strip(), [])
                started = True
                continue
            if started and line.startswith('Disallow:'):
                disallow.append(line.split()[1].strip())
        return rules
    pass


if __name__ == '__main__':
    # run_sqlite()
    db_conn = sqlite3.connect('sqler.db', check_same_thread=False)
    t1 = threading.Thread(target=task, args=(db_conn,))
    t2 = threading.Thread(target=task, args=(db_conn, 5))
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    db_conn.close()
    # print(get_robots_rules('https://www.baidu.com'))
    # print(get_robots_rules('https://www.google.com'))
    # print(get_robots_rules('https://www.zillow.com'))
    # test_doc()
    # get_wiki_info()
    # get_doc_info()
    pass
