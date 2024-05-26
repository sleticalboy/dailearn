from scrapy.cmdline import execute
import os
import sys

# 所有项目中所有的爬虫
_CRAWLS = {
    'books': ['scrapy', 'crawl', 'books', '-o', 'out/%(name)s-%(time)s.json'],
    'matplot': ['scrapy', 'crawl', 'matplot', '-o', 'out/%(name)s-%(time)s.json'],
}

# 调试程序
if __name__ == '__main__':
    sys.path.append(os.path.dirname(os.path.abspath(__file__)))
    execute(_CRAWLS['matplot'])
