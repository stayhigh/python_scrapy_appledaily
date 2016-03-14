import scrapy 
from bs4 import BeautifulSoup
from apple.items import AppleItem
from scrapy.spiders import CrawlSpider
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor

#  original class: class AppleCrawler(scrapy.Spider):
#  replace 'scrapy.Spider' with 'CrawlerSpider'
#  CrawSpider: A class is used to crawl multiple websites
class AppleCrawler(CrawlSpider):
    start_urls = ['http://www.appledaily.com.tw/realtimenews/section/new/']
    rules = [
        Rule(LinkExtractor(allow=('/realtimenews/section/new/[1-3]$')), callback='parse_list', follow=True)
    ]
    name = 'apple'
    def parse_list(self, response):
        domain = "http://www.appledaily.com.tw"
        res = BeautifulSoup(response.body)
        for news in res.select('.rtddt'):
            print news.select('h1')[0].text
            yield scrapy.Request(domain + news.select('a')[0]['href'], self.parse_detail)

    def parse_detail(self, response):
        res = BeautifulSoup(response.body)
        appleitem = AppleItem()
        # define all fields
        appleitem['title'] = res.select('#h1')[0].text
        appleitem['content'] = res.select('#summary')[0].text
        appleitem['time'] = res.select('.gggs time')[0].text
        return appleitem