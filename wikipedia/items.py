# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

class WikipediaItem(scrapy.Item):

    covid_locations = scrapy.Field()
    covid_cases_test = scrapy.Field()
    covid_deaths_test = scrapy.Field()
    covid_recoveries_test = scrapy.Field()
  #  covid_reference_links = scrapy.Field()



