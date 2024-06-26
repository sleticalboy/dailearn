# Scrapy settings for scrapy_hello project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = "scrapy samples"

SPIDER_MODULES = ["scrapy_hello.spiders"]
NEWSPIDER_MODULE = "scrapy_hello.spiders"

# Crawl responsibly by identifying yourself (and your website) on the user-agent
# USER_AGENT = "scrapy_hello (+http://www.yourdomain.com)"

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
CONCURRENT_REQUESTS = 16

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
# DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
# CONCURRENT_REQUESTS_PER_DOMAIN = 16
# CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
COOKIES_ENABLED = True

# Disable Telnet Console (enabled by default)
TELNETCONSOLE_ENABLED = True

# Override the default request headers:
# DEFAULT_REQUEST_HEADERS = {
#    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
#    "Accept-Language": "en",
# }

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
# SPIDER_MIDDLEWARES = {
#    "scrapy_hello.middlewares.ScrapyHelloSpiderMiddleware": 543,
# }

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
# DOWNLOADER_MIDDLEWARES = {
#    "scrapy_hello.middlewares.ScrapyHelloDownloaderMiddleware": 543,
# }

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
# EXTENSIONS = {
#    "scrapy.extensions.telnet.TelnetConsole": None,
# }

# 自定义 pipeline 管理器
ITEM_PROCESSOR = "scrapy_hello.pipelines.PipelineManager"

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
# ITEM_PIPELINES = {}
# ITEM_PIPELINES_BASE = {}
# 全局自定义 pipeline
ITEM_PIPELINES_ME = {
    'books': {
        "scrapy.pipelines.files.FilesPipeline": 300,  # 使用文件下载
        "scrapy_hello.pipelines.BookPricePipeline": 301,  # 对价格进行汇率转换
    },
    'matplot': {
        "scrapy_hello.pipelines.FilesPipeline": 1,  # 使用自定义文件下载
    },
}
# 文件存储目录
FILES_STORE = '/home/binlee/code/dailearn/sub-python/scrapy_hello/out'

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
# AUTOTHROTTLE_ENABLED = True
# The initial download delay
# AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
# AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
# AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
# AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
# HTTPCACHE_ENABLED = True
# HTTPCACHE_EXPIRATION_SECS = 0
# HTTPCACHE_DIR = "httpcache"
# HTTPCACHE_IGNORE_HTTP_CODES = []
# HTTPCACHE_STORAGE = "scrapy.extensions.httpcache.FilesystemCacheStorage"

# Set settings whose default value is deprecated to a future-proof value
REQUEST_FINGERPRINTER_IMPLEMENTATION = "2.7"
TWISTED_REACTOR = "twisted.internet.asyncioreactor.AsyncioSelectorReactor"
FEED_EXPORT_ENCODING = "utf-8"
# 自定义导出
FEED_EXPORTERS = {'txt': 'scrapy_hello.exporters.TxtExporter'}
# 哪些字段可以被导出
FEED_EXPORT_FIELDS = [
    # books
    'upc', 'name', 'price', 'stock', 'review_rating', 'review_num', 'img_url',
    # matplotlib
    'title', 'url', 'img_urls', 'sample_codes',
]

# 日志相关设置
LOG_FORMAT = "%(asctime)s.%(msecs)03d [%(name)s] %(levelname)s: %(message)s"
LOG_DATEFORMAT = "%y-%m-%d %H:%M:%S"
# LOG_FILE = f'{FILES_STORE}/log.log'
# LOG_FILE_APPEND = True
# LOG_STDOUT = False
LOG_LEVEL = "INFO"
LOG_SHORT_NAMES = False
