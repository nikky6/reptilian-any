from scrapy import cmdline
import os
# os.system("rm -rf ./reptilian/images")
cmdline.execute("scrapy crawl jobbole".split())
# cmdline.execute("scrapy crawl gpnews".split())
# cmdline.execute("scrapy crawl aigupiao".split())
# cmdline.execute("scrapy crawl sdifen".split())
# cmdline.execute("scrapy crawl chsi".split())
