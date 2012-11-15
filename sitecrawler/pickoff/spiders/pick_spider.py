from scrapy import log
from pickoff.items import DmozItem
from scrapy.spider import BaseSpider
from scrapy.contrib.spiders import Rule, CrawlSpider
from scrapy.selector import HtmlXPathSelector
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor

class PickSpider(CrawlSpider):
    def __init__(self, address_domains=None, urls=None):
        super(PickSpider, self).__init__()
        print '---------------------'
        print address_domains,urls
        print '---------------------'
        self.start_urls      = ["%s" % urls]
        self.allowed_domains = ["%s" % address_domains]
    name = "dmoz"

    rules = (
        # Rule(SgmlLinkExtractor(allow=('/\w+/')), follow=True),
        Rule(SgmlLinkExtractor(allow=('/\w+/')), callback='parse_item'),
    )
    # rules = (Rule(SgmlLinkExtractor(allow=('/en/0.16/')), callback='parse_item'),)

    def parse_item(self, response):
        hxs = HtmlXPathSelector(response)
        sites = hxs.select('//html')

        item = DmozItem()
        item['url']   = response.url
        item['title'] = sites.select('//title/text()').extract()
        item['text']  = sites.select('//*/text()').extract()
        item['site']  = self.allowed_domains[0]

        return item
        # print '---------------------'
        # print '===================='
