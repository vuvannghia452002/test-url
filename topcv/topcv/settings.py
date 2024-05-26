import os
# Scrapy settings for topcv project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = "topcv"

SPIDER_MODULES = ["topcv.spiders"]
NEWSPIDER_MODULE = "topcv.spiders"


# Crawl responsibly by identifying yourself (and your website) on the user-agent
# USER_AGENT = "topcv (+http://www.yourdomain.com)"

# Obey robots.txt rules
ROBOTSTXT_OBEY = True

# Configure maximum concurrent requests performed by Scrapy (default: 16)
# CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
# DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
# CONCURRENT_REQUESTS_PER_DOMAIN = 16
# CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
# COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
# TELNETCONSOLE_ENABLED = False

# Override the default request headers:
# DEFAULT_REQUEST_HEADERS = {
#    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
#    "Accept-Language": "en",
# }

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
# SPIDER_MIDDLEWARES = {
#    "topcv.middlewares.TopcvSpiderMiddleware": 543,
# }

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
# DOWNLOADER_MIDDLEWARES = {
#    "topcv.middlewares.TopcvDownloaderMiddleware": 543,
# }

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
# EXTENSIONS = {
#    "scrapy.extensions.telnet.TelnetConsole": None,
# }

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
# ITEM_PIPELINES = {
#    "topcv.pipelines.TopcvPipeline": 300,
# }

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

















#! Vũ Văn Nghĩa - 20206205

# # Hiển thị thông tin logging
# LOG_ENABLED = False


# Kích hoạt bộ đệm HTTP
HTTPCACHE_ENABLED = True
HTTPCACHE_EXPIRATION_SECS = 0
# HTTPCACHE_EXPIRATION_SECS = 60*60
# HTTPCACHE_EXPIRATION_SECS = 20*60*60
HTTPCACHE_IGNORE_HTTP_CODES = [x for x in range(100, 600) if x != 200]


# # Thêm thông tin proxy để fix 429
# ROTATING_PROXY_LIST_PATH = 'proxies.txt'
# # Số lần thử lại khi gặp lỗi với một proxy
# ROTATING_PROXY_PAGE_RETRY_TIMES = 5  
# # Thời gian chờ trước khi thử lại (tính bằng giây)
# ROTATING_PROXY_BACKOFF_BASE = 300

DOWNLOADER_MIDDLEWARES = {
    # Thêm thông tin user agents ngẫu nhiên để fix 403
    'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware': None,
    'scrapy_user_agents.middlewares.RandomUserAgentMiddleware': 400,
    #
    # 'scrapy.downloadermiddlewares.httpproxy.HttpProxyMiddleware': 1,
    # 'rotating_proxies.middlewares.RotatingProxyMiddleware': 610,
    # 'rotating_proxies.middlewares.BanDetectionMiddleware': 620,


}



# # Thêm thông tin rate-limiting ngẫu nhiên để fix 429
DOWNLOAD_DELAY = 15
DOWNLOAD_DELAY = 5
# DOWNLOAD_DELAY = 1
# DOWNLOAD_DELAY = 0



CONCURRENT_REQUESTS_PER_DOMAIN = 1

AUTOTHROTTLE_ENABLED = True
AUTOTHROTTLE_START_DELAY = 5
AUTOTHROTTLE_MAX_DELAY = 60
AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
AUTOTHROTTLE_DEBUG = True



DATABASE_HOST = os.getenv("DATABASE_HOST")
print(f"🚀 {DATABASE_HOST}")
DATABASE_PORT = os.getenv("DATABASE_PORT")
print(f"🚀 {DATABASE_PORT}")
DATABASE_USERNAME = os.getenv("DATABASE_USERNAME")
print(f"🚀 {DATABASE_USERNAME}")
DATABASE_PASSWORD = os.getenv("DATABASE_PASSWORD")
print(f"🚀 {DATABASE_PASSWORD}")
DATABASE_NAME = os.getenv("DATABASE_NAME")
print(f"🚀 {DATABASE_NAME}")


# ITEM_PIPELINES = {
#     # #     'topcv.pipelines.RemoveDuplicateLinkPipeline': 300
#     'topcv.pipelines.MySQLPipeline': 3
# }
