import scrapy

class Item(scrapy.Item):
	word = scrapy.Field()
	link = scrapy.Field()
	trads = scrapy.Field()