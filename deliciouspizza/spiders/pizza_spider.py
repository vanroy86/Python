from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector
from deliciouspizza.items import *

class pizzaSpider(BaseSpider):
	name = "pizza"
	allowed_domains= ["hotukdeals.com/vouchers/"]
	start_urls = [
		"http://www.hotukdeals.com/vouchers/dominos.co.uk"
	]

	def parse(self, response):
		sel = HtmlXPathSelector(response)
		sites = sel.select('//body')
		items = []
		for site in sites:
			item = DeliciouspizzaItem()
			item['code'] = site.select('//input[(@class="hidden-code") and (@type="text")]/@value').extract()
			item['desc'] = site.select('//span[@class="voucher-discount"]/text()').extract()
			items.append(item)
		return items