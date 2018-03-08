import scrapy

class Item(scrapy.Item):
	word = scrapy.Field()
	link = scrapy.Field()
	trads = scrapy.Field()
	
class Trad(scrapy.Item):
	lemma = scrapy.Field()
	lemma_header = scrapy.Field()
	lemma_definition = scrapy.Field()

class BlogSpider(scrapy.Spider):
    name = 'blogspider'
    start_urls = ['http://www.perseus.tufts.edu/hopper/text?doc=Perseus:text:1999.01.0133']	
		
    def parse(self, response):
        for title in response.css('a.text'):
            link = 'http://www.perseus.tufts.edu/hopper/' + title.css('a::attr(href)').extract_first()
            item = Item()
            item['word'] = title.css('a ::text').extract_first()
            item['link'] = link
            itemCompleto  = scrapy.Request(link,callback=self.parse_trads)
            itemCompleto.meta['item'] = item
            yield itemCompleto
			
        for next_page in response.css('.arrow'):
            yield response.follow(next_page, self.parse)
			
    def parse_trads(self, response):
        item = response.meta['item']
        trads = []
        for analisis in response.css('div.analysis'):
            trad = Trad()
            trad['lemma'] = analisis#.xpath('//div[@class="lemma"]').extract() #css('div.lemma ::text').extract_first()
            trad['lemma_definition'] = analisis.xpath('//div[@class="lemma_definition"]').extract() #css('div.lemma_definition ::text').extract_first()
            trads.append(trad)
        item['trads'] = trads  #response.css('div.analysis').extract()		
        yield item
		
#<a href="morph?l=mh%3Dnin&amp;la=greek&amp;can=mh%3Dnin0" onclick="m(this,1,0); return false" class="text" target="morph">μῆνιν</a>
# scrapy runspider illiad.py