# The first draft of the subreddit scraper (similar to the tutorial in the documentation)
# This is only a test, so the code may change over time as development continues.
import scrapy

class SubredditSpider(scrapy.Spider):
	name = "subreddits"

	def start_requests(self):
		urls = [
			'https://www.reddit.com/r/subreddit',
		]
		for url in urls:
			yield scrapy.Request(url=url, callback=self.parse)

	def parse(self, response):
		page = response.url.split("/")[-2]
		filename = 'subreddit-%s.html' % page
		with open(filename, 'wb') as f:
			f.write(response.body)
		self.log('Saved file %s' % filename)
