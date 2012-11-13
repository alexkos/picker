from scrapy import log
from pickoff.items import DmozItem
from scrapy.spider import BaseSpider
from scrapy.contrib.spiders import Rule, CrawlSpider
from scrapy.selector import HtmlXPathSelector
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor

class PickSpider(CrawlSpider):
    name            = "dmoz"
    # allowed_domains = ['dmoz.org']
    # start_urls      = ['http://dmoz.org']
    allowed_domains = ['scrapy.org']
    start_urls      = ['http://doc.scrapy.org/en/0.16/']

    # def __init__(self, address_domains=None, urls=None):
    #     self.allowed_domains = ["%s" % address_domains]
    #     self.start_urls      = ["%s" % urls]

    rules = (
            Rule(SgmlLinkExtractor(allow=('/en/0.16/')), callback='parse_item'),
    )

    def parse_item(self, response):
        hxs = HtmlXPathSelector(response)
        sites = hxs.select('//html')

        item = DmozItem()
        item['url']   = response.url
        item['title'] = sites.select('//title/text()').extract()
        # item['text']  = sites.select('//*/text()').extract()

        print '===================='
        print item
        print '===================='

        # print '---------------------'
            
        # items = []
        # for site in sites:
        #     item = DmozItem()
        #     item['url']   = response.url
        #     item['title'] = site.select('//title/text()').extract()
        #     item['text']  = site.select('//*/text()').extract()
        #     items.append(item)

        # print '===================='

        # return items