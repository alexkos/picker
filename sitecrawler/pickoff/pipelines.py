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
        print '#################################'
        print item['site']
        print '#################################'
        textsite = TextSite(url=item['url'],
                          title=item['title'],
                          text =item['text'],
                          site =site_obj
                          )
        textsite.save()
        # print '#################################'
        # print textsite.url, textsite.title, textsite.text, textsite.site
        # try:
        # except Exception, e:
        #     print e
        return item
