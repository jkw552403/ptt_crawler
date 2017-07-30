# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class PostItem(scrapy.Item):
    post_id = scrapy.Field()
    title = scrapy.Field()
    author_id = scrapy.Field()
    board = scrapy.Field()
    content = scrapy.Field()
    datetime = scrapy.Field()
    ip = scrapy.Field()
    url = scrapy.Field()
    external_urls = scrapy.Field()
    source_hash = scrapy.Field()  # to check if there is any update in this post


class CommentItem(scrapy.Item):
    post_id = scrapy.Field()
    user_id = scrapy.Field()
    user_ip = scrapy.Field()
    datetime = scrapy.Field()
    content = scrapy.Field()
    tag = scrapy.Field()
    n_floor = scrapy.Field()
