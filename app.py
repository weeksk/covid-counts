"""Script to crawl Wikipedia for covid data and store results in MongoDB
"""

from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from apscheduler.schedulers.twisted import TwistedScheduler
from wikipedia.spiders import WikipediaSpider

# process = CrawlerProcess(get_project_settings())
# scheduler = TwistedScheduler()
# scheduler.add_job(process.crawl, 'interval', args=WikipediaSpider, seconds=300)
# scheduler.start()
# process.start(False)
