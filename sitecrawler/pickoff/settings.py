# Scrapy settings for pickoff project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/topics/settings.html
#
import os, sys
import imp
from pprint import pprint as p
from django.core.management import setup_environ

BOT_NAME = 'pickoff'

SPIDER_MODULES = ['pickoff.spiders']
NEWSPIDER_MODULE = 'pickoff.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'pickoff (+http://www.yourdomain.com)'

current_dir = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
django_app = os.path.join(current_dir, '../')
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "picker.settings")
sys.path.insert(0, django_app)