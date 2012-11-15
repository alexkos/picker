# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/topics/item-pipeline.html
# from django.db.utils import IntegrityError
from capturing.models import NewSites, TextSite
from django.db.utils import IntegrityError


class SitePipeline(object):
    def process_item(self, item, spider):
        site_obj = NewSites.objects.get(url=item['site'])
        obj_len  = len(site_obj.url.split('.'))
        item_len = len(item['url'].split('.'))

        if obj_len == item_len:
            textsite = TextSite(url=item['url'],
                              title=item['title'],
                              text =item['text'],
                              site =site_obj
                              )
            textsite.save()
        # try:
        # except IntegrityError, e:
        #     print e
        return item
