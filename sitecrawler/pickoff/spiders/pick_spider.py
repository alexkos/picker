from scrapy import log
from pickoff.items import DmozItem
from scrapy.spider import BaseSpider
from scrapy.contrib.spiders import Rule, CrawlSpider
from scrapy.selector import HtmlXPathSelector
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor

class PickSpider(CrawlSpider):
    def __init__(self, address_domains=None, urls=None):
        super(PickSpider, self).__init__()
        self.start_urls      = ["%s" % urls]
        self.allowed_domains = ["%s" % address_domains]
    name = "dmoz"

    rules = (Rule(SgmlLinkExtractor(allow=('\/\w+', '(\/\w+)+/'), ), callback='parse_item'), )

    def parse_item(self, response):
        hxs = HtmlXPathSelector(response)
        sites = hxs.select('//html/body')

        text = ''
        
        # ex = sites.select('//*[not(contains(@type,"text/javascript"))]/text()').extract()       
        # ex = sites.select('//body/child::*[not(contains(@type,"text/javascript"))]/text()').extract()       
        # print '---------------------'
        # print ex
        # print '===================='
        
        # for site in sites.select('//*[not(contains(@type,"text/javascript"))][not(contains(@type,"text/javascript"))]/text()').extract():
        for site in sites.select('//*[not(self::script)]/text()').extract():
            text += site
        # for site in sites.select('//*/text()').extract():
        #     text += site
        
        item = DmozItem()
        item['url']   = response.url
        item['title'] = sites.select('//title/text()').extract()
        item['text']  = text
        item['site']  = self.start_urls[0]
        
        return item
        # print '---------------------'
        # print '===================='
