import scrapy

from scrapy.loader import ItemLoader

from ..items import PassumpsicbankItem
from itemloaders.processors import TakeFirst


class PassumpsicbankSpider(scrapy.Spider):
	name = 'passumpsicbank'
	start_urls = ['https://www.passumpsicbank.com/news-events']

	def parse(self, response):
		post_links = response.xpath('//a[@class="readMore"]/@href').getall()
		yield from response.follow_all(post_links, self.parse_post)

	def parse_post(self, response):
		title = response.xpath('//div[@class="headerContent"]/h1/text()').get()
		description = response.xpath('//div[@class="content"]//p//text()[normalize-space()]').getall()
		description = [p.strip() for p in description]
		description = ' '.join(description).strip()
		date = response.xpath('//div[@class="headerContent"]/h5/text()').get()

		item = ItemLoader(item=PassumpsicbankItem(), response=response)
		item.default_output_processor = TakeFirst()
		item.add_value('title', title)
		item.add_value('description', description)
		item.add_value('date', date)

		return item.load_item()
