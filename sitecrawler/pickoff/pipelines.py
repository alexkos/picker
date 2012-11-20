# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/topics/item-pipeline.html
# from django.db.utils import IntegrityError
from capturing.models import TextSite
from django.db.utils import IntegrityError

class SitePipeline(object):
    def process_item(self, item, spider):
        textsite = TextSite(url=item['url'],
                          title=item['title'],
                          text =item['text'],
                          site =item['site']
                          )
        textsite.save()
        # try:
        # except IntegrityError, e:
        #     print e
        return item
