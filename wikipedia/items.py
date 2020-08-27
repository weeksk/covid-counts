# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class WikipediaItem(scrapy.Item):

    # covid_data_retrieval_time = datetime.now().strftime("%Y_%m_%d-%I_%M_%S_%p")
    covid_data_retrieval_time = scrapy.Field()
    covid_locations = scrapy.Field()
    covid_cases = scrapy.Field()
    covid_deaths = scrapy.Field()
    covid_recoveries = scrapy.Field()
  #  covid_reference_links = scrapy.Field()



