# -*- coding: utf-8 -*-
import scrapy


class PttSpider(scrapy.Spider):
    name = 'ptt'
    allowed_domains = ['ptt.cc']
    start_urls = ['http://ptt.cc/']

    def parse(self, response):
        pass
