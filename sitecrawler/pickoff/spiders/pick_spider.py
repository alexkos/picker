from scrapy import log
from pickoff.items import DmozItem
from scrapy.spider import BaseSpider
from capturing.models import NewSites
from django.contrib.auth.models import User
from scrapy.selector import HtmlXPathSelector
from scrapy.contrib.spiders import Rule, CrawlSpider
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor

class PickSpider(CrawlSpider):
    def __init__(self, address_domains=None, urls=None, userid=None):
        super(PickSpider, self).__init__()
        self.start_urls      = ["%s" % urls]
        self.allowed_domains = ["%s" % address_domains]
        self.userid          = int('%s' % userid)
    name = "pick"

    rules = (Rule(SgmlLinkExtractor(allow=('\/\w+', '(\/\w+)+/'), ), callback='parse_item'), )

    def parse_item(self, response):
        hxs = HtmlXPathSelector(response)
        sites = hxs.select('//html/body')

        text = ''
        
        for site in sites.select('//*[not(self::script)][not(self::style)][not(self::title)]/text()').extract():
            text += site

        user     = User.objects.get(id=self.userid)
        site_obj = NewSites.objects.get(url=self.start_urls[0],user=user)

        item = DmozItem()
        if response.url.startswith(self.start_urls[0]):
            item['url']   = response.url
            item['title'] = sites.select('//title/text()').extract()[0]
            item['text']  = text
            item['site']  = site_obj
            
        return item
        # print '---------------------'
        # print '===================='
