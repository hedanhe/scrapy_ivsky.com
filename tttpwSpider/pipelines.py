# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from urllib.request import urlopen
import os

class TttpwspiderPipeline(object):

    def process_item(self, item, spider):
        if item['title']:
            img_name = item["url"].split("/")[-1]
            dirs = item["title"] + "/"
            file_path = dirs + img_name
            conn = urlopen(item["url"])

            if not os.path.exists(dirs):
                os.mkdir(dirs)
            with open(file_path, "wb") as f:
                f.write(conn.read())
            return item
