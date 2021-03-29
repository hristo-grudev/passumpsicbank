BOT_NAME = 'passumpsicbank'

SPIDER_MODULES = ['passumpsicbank.spiders']
NEWSPIDER_MODULE = 'passumpsicbank.spiders'
FEED_EXPORT_ENCODING = 'utf-8'
LOG_LEVEL = 'ERROR'
DOWNLOAD_DELAY = 0

ROBOTSTXT_OBEY = True

ITEM_PIPELINES = {
	'passumpsicbank.pipelines.PassumpsicbankPipeline': 100,

}

USER_AGENT = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0'
