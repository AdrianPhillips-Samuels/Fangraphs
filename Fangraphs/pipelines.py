# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

from scrapy.exceptions import DropItem
from scrapy.exporters import CsvItemExporter

class ValidateItemPipeline(object):
	def process_item(self, item, spider):
		if not all(item.values()):
			raise DropItem("Missing values!")
		else:
			return item

class FangraphsPipeline(object):
	def __init__(self):
		self.filename = 'XVeloFix.csv'

	def open_spider(self, spider):
		self.csvfile = open(self.filename, 'wb')
		self.exporter = CsvItemExporter(self.csvfile)
		self.exporter.fields_to_export = ['Name','Year','Team','PA','AVG','BABIP','BBp','BBtoK','Centp','FBp','GBp','GBtoFB','HRtoFB','Hardp','IFFBp','IFH','IFHp','ISO','Kp','LDp','Medp','OBP','OPS','Oppop','Pullp','SLG','Softp','Spd','UBR','XVelo','wGDP','wOBA','wRAA','wRC','wRCpl','wSB']
		self.exporter.start_exporting()

	def close_spider(self, spider):
		self.exporter.finish_exporting()
		self.csvfile.close()
	def process_item(self, item, spider):
		self.exporter.export_item(item)
		return item
