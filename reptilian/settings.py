# -*- coding: utf-8 -*-

# Scrapy settings for reptilian project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html
import os

BOT_NAME = 'reptilian'

SPIDER_MODULES = ['reptilian.spiders']
NEWSPIDER_MODULE = 'reptilian.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
# USER_AGENT = 'reptilian (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
# CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://doc.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
DOWNLOAD_DELAY = 1
# The download delay setting will honor only one of:
# CONCURRENT_REQUESTS_PER_DOMAIN = 16
# CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
# TELNETCONSOLE_ENABLED = False

# Override the default request headers:
# DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
# }

# Enable or disable spider middlewares
# See https://doc.scrapy.org/en/latest/topics/spider-middleware.html
# SPIDER_MIDDLEWARES = {
#    'reptilian.middlewares.ReptilianSpiderMiddleware': 543,
# }

# Enable or disable downloader middlewares
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
    # 'reptilian.middlewares.ReptilianDownloaderMiddleware': 543,
    # 'reptilian.middlewares.RandomUserProxyMiddleware': 544,
    'reptilian.middlewares.RandomUserAgentMiddleware': 545,
}

# Enable or disable extensions
# See https://doc.scrapy.org/en/latest/topics/extensions.html
MYEXT_ENABLED=True # 是否启用扩展，启用扩展为 True， 不启用为 False
IDLE_NUMBER  = 1 # 30秒 关闭爬虫的持续空闲次数，持续空闲次数超过IDLE_NUMBER，爬虫会被关闭。默认为 360 ，也就是30分钟，一分钟12个时间单位
EXTENSIONS = {
    'reptilian.extensions.RedisSpiderSmartIdleClosedExensions': 500,
}

# Configure item pipelines
# See https://doc.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
    # 将Pipeline序列化发送到redis中
    # 'scrapy_redis.pipelines.RedisPipeline': 300
    # 'reptilian.pipelines.JobboleArticPipeline': 300,
    # 'reptilian.pipelines.JobboleImagePipeline': 100,
    # 'reptilian.pipelines.JobboleMysqlPipeline': 400,
    # 'reptilian.pipelines.MysqlTwistedPipeline': 600,
}

IMAGES_URLS_FIELD = "image_url"
object_dir = os.path.abspath(os.path.dirname(__file__))
IMAGES_STORE = os.path.join(object_dir, "images")

import sys
sys.path.append(object_dir)

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/autothrottle.html
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
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
# HTTPCACHE_ENABLED = True
# HTTPCACHE_EXPIRATION_SECS = 0
# HTTPCACHE_DIR = 'httpcache'
# HTTPCACHE_IGNORE_HTTP_CODES = []
# HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'

# mysql config
MYSQL_HOST      = "127.0.0.1"
MYSQL_USER      = "root"
MYSQL_PASSWORD  = "zngz123456"
MYSQL_DBNAME    = "reptilian"

# redis config
REDIS_HOST      = "127.0.0.1"
REDIS_PORT      = 6379
REDIS_DB        = 0
REDIS_PWD       = ""

# chrom、firefox、ie
USER_AGENR_TYPE = 'chrome'

# scrapy-redis
# 队列存redis
SCHEDULER        = "scrapy_redis.scheduler.Scheduler"
# 队列的类型(先进先出/FifoQueue/PriorityQueue/LifoQueue)
QUEUE_CLASS      = "scrapy_redis.queue.PriorityQueue"
# 去重RFPDupeFilter方案
DUPEFILTER_CLASS = "scrapy_redis.dupefilter.RFPDupeFilter"

# log (DEBUG\INFO\WARNING\ERROR)
LOG_FILE  = "scrapy.log"
LOG_LEVEL = "DEBUG"