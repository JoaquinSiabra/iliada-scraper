import scrapy

class BlogSpider(scrapy.Spider):
    name = 'blogspider'
    start_urls = ['http://www.perseus.tufts.edu/hopper/text?doc=Perseus:text:1999.01.0133']

    def parse(self, response):
        for title in response.css('a.text'):
            yield {'word': title.css('a ::text').extract_first(), 'link':title.css('a::attr(href)').extract_first() }

        for next_page in response.css('.arrow'):
            yield response.follow(next_page, self.parse)
			

#<a href="morph?l=mh%3Dnin&amp;la=greek&amp;can=mh%3Dnin0" onclick="m(this,1,0); return false" class="text" target="morph">μῆνιν</a>
# scrapy runspider illiad.py