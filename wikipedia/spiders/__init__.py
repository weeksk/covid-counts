import scrapy

from ..items import WikipediaItem



class WikipediaSpider(scrapy.Spider):


    name = 'wikipedia' # consider changing to country
    start_urls = [
        'https://en.wikipedia.org/wiki/COVID-19_pandemic_by_country_and_territory'
    ]

    def parse(self, response):

        items = WikipediaItem()

        covid_locations = response.css('#thetable i a , #thetable th > a').css('::text').extract()
        covid_cases = response.css('#thetable th+ td').css('::text').extract()
        covid_deaths = response.css('#thetable td:nth-child(4)').css('::text').extract()
        covid_recoveries = response.css('#thetable td:nth-child(5)').css('::text').extract()
        # covid_reference_links = response.css(
        #     '#thetable td:nth-child(6) , #cite_ref-24 a , #cite_ref-\:1p3a_19-0 a').css('::attr(href)').extract()

        covid_cases_test = []
        covid_deaths_test = []
        covid_recoveries_test = []
        for item in covid_cases: # add conditional for if item[1] is not alpha
            if item[0].isdigit():
                covid_cases_test.append(item[:-1])
            elif item == '\n':
                covid_cases_test.append('')
            else:
                covid_cases_test.append(item)
        for item in covid_deaths:
            if item[0].isdigit():
                covid_deaths_test.append(item[:-1])
            elif item == '\n':
                covid_deaths_test.append('')
            else:
                covid_deaths_test.append(item)
        for item in covid_recoveries:
            if item[0].isdigit():
                covid_recoveries_test.append(item[:-1])
            elif item == '\n':
                covid_recoveries_test.append('')
            else:
                covid_recoveries_test.append(item)





        items['covid_locations'] = covid_locations
        items['covid_cases_test'] = covid_cases_test
        items['covid_deaths_test'] = covid_deaths_test
        items['covid_recoveries_test'] = covid_recoveries_test
        # items['covid_reference_links'] = covid_reference_links

        yield items



