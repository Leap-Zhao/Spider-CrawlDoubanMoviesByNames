# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import json

import csv
import itertools

class DoubanPipeline(object):
    def __init__(self):
        self.filename = open("douban.json", "w")

    def process_item(self, item, spider):
        text = json.dumps(dict(item), ensure_ascii = False) + ",\n"
        self.filename.write(text.encode("utf-8"))
        return item

    def close_spider(self, spider):
        self.filename.close()



class CSVPipeline(object):
   	def __init__(self):
		self.csvwriter = csv.writer(open('douban.csv', 'wb'), delimiter=',')
		self.csvwriter.writerow(['movie_name','movie_director','movie_writer','movie_starring','movie_type','movie_startdate','movie_length','movie_plot','movie_score','movie_url'])

   	def process_item(self, item, ampa):
		rows = zip(item['movie_name'],item['movie_director'],item['movie_writer'],item['movie_starring'],item['movie_type'],item['movie_startdate'],item['movie_length'],item['movie_plot'],item['movie_score'],item['movie_url'])
		for row in rows:
			self.csvwriter.writerow(row)
		return item
