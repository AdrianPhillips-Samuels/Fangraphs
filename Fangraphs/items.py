# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class FangraphsItem(scrapy.Item):
    # define the fields for your item here like:
	Name = scrapy.Field()
	Year = scrapy.Field()
	Team = scrapy.Field()
	PA = scrapy.Field()
	BBp = scrapy.Field()
	Kp = scrapy.Field()
	BBtoK = scrapy.Field()
	AVG = scrapy.Field()
	OBP = scrapy.Field()
	SLG = scrapy.Field()
	OPS = scrapy.Field()
	ISO = scrapy.Field()
	Spd = scrapy.Field()
	BABIP = scrapy.Field()
	UBR = scrapy.Field()
	wGDP = scrapy.Field()
	wSB = scrapy.Field()
	wRC = scrapy.Field()
	wRAA = scrapy.Field()
	wOBA = scrapy.Field()
	wRCpl = scrapy.Field()
	GBtoFB = scrapy.Field()
	LDp = scrapy.Field()
	GBp = scrapy.Field()
	FBp = scrapy.Field()
	IFFBp = scrapy.Field()
	HRtoFB = scrapy.Field()
	IFH = scrapy.Field()
	IFHp = scrapy.Field()
	Pullp = scrapy.Field()
	Centp = scrapy.Field()
	Oppop = scrapy.Field()
	Softp = scrapy.Field()
	Medp = scrapy.Field()
	Hardp = scrapy.Field()
	XVelo = scrapy.Field()