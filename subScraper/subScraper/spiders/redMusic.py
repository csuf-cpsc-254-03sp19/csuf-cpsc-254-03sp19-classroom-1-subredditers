# -*- coding: utf-8 -*-
import scrapy


class RedmusicSpider(scrapy.Spider):
    name = 'redMusic'
    allowed_domains = ['www.reddit.com/r/Music']
    start_urls = ['http://www.reddit.com/r/Music/']

    def parse(self, response):
        #Extracting the content using css selectors
        titles = response.css(".s1okktje-0.pgXlo::text").extract()
        votes = response.css("._1rZYMD_4xY3gRcSS3p8ODO::text").extract()

       
        #Give the extracted content row wise
        for item in zip(titles,votes):
            #create a dictionary to store the scraped info
            scraped_info = {
                'title' : item[0],
                'vote' : item[1],

            }

            #yield or give the scraped info to scrapy
            yield scraped_info

