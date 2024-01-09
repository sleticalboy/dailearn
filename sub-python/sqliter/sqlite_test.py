import sqlite3

import requests


def run_sqlite():
    conn = sqlite3.connect('sqler.db')
    cursor = conn.cursor()
    print(conn, cursor)
    cursor.execute('''create table if not exists user(
    _id integer primary key autoincrement default 0 ,
    _name varchar(32) not null ,
    _email varchar(32) not null ,
    _password varchar(32) not null ,
    _token text default null
    );''')
    for i in range(20):
        cursor.execute("insert into user (_name, _email, _password) values ('bin.li', 'bin.li@quvideo.com', 'hello')")
    conn.commit()
    cursor.execute('select * from user')
    res = cursor.fetchall()
    for r in res:
        print(r)
    cursor.execute('delete from user where _name=?', ['bin.li'])
    res = cursor.fetchall()
    print(res)
    # cursor.execute('alter table user add column results text default null')
    cursor.execute('alter table user drop column _results')
    res = cursor.fetchall()
    print(res)
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
    # print(get_robots_rules('https://www.baidu.com'))
    # print(get_robots_rules('https://www.google.com'))
    # print(get_robots_rules('https://www.zillow.com'))
    # test_doc()
    # get_wiki_info()
    # get_doc_info()
    pass
