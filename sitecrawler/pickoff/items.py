# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/topics/items.html

from scrapy.item import Item, Field
from picker.capturing.models import TextSite

class DmozItem(Item):
    # site_model = TextSite
    url   = Field()
    title = Field()
    text  = Field()