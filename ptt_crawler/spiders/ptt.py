# -*- coding: utf-8 -*-
import urlparse

import scrapy
from scrapy.exceptions import CloseSpider


class PttSpider(scrapy.Spider):

    BASE_URL = 'https://www.ptt.cc/'
    name = 'ptt'
    allowed_domains = ['ptt.cc']

    page_count = 0

    def start_requests(self):
        assert self.board is not None
        assert self.n_page is not None
        self.n_page = int(self.n_page)
        url = urlparse.urljoin(self.BASE_URL, 'bbs/{}/index.html'.format(self.board))
        yield scrapy.Request(url, self.parse_links)

    def parse_links(self, response):
        links = response.xpath('//*[@id="main-container"]/div[2]/*/div[3]/a/@href').extract()
        for l in links:
            url = urlparse.urljoin(self.BASE_URL, l)
            yield scrapy.Request(url, self.parse_post)
        next_page_url = urlparse.urljoin(self.BASE_URL,
                                         response.xpath(u'//div[@id="action-bar-container"]//a[contains(text(), "上頁")]/@href').extract_first())
        yield scrapy.Request(next_page_url, self.parse_links)

    def parse_post(self, response):
        self.page_count += 1
        self.log("Page count = {}".format(self.page_count))
        if self.page_count >= self.n_page:
            raise CloseSpider("")
