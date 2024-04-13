import scrapy
from scrapy.crawler import CrawlerProcess

class LabelSpider(scrapy.Spider):
    name = 'label_spider'
    start_urls = ['https://realpython.com/beautiful-soup-web-scraper-python/']

    def parse(self, response):
        xpath_selector = '/html/body/div[1]/div/aside/div[1]/form/div[1]/p[2]'
        label = response.xpath(xpath_selector).get()
        if label:
            print(label)
        else:
            print("Label not found.")

if __name__ == "__main__":
    process = CrawlerProcess()
    process.crawl(LabelSpider)
    process.start()
