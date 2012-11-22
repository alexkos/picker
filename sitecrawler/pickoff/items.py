# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/topics/items.html

from scrapy.item import Item, Field
from capturing.models import TextSite

class DmozItem(Item):
    url   = Field()
    title = Field()
    text  = Field()
    site  = Field()