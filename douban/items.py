# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DoubanItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # 导演,编剧,主演,类型, 
    # 上映时间,片长,剧情简介,豆瓣评分,url

    # 电影名字
    movie_name = scrapy.Field()
    # 导演
    movie_director = scrapy.Field()
    # 编剧
    movie_writer = scrapy.Field()
    # 主演
    movie_starring = scrapy.Field()
    # 类型
    movie_type = scrapy.Field()
    # 上映时间
    movie_startdate = scrapy.Field()
    # 片长
    movie_length = scrapy.Field()
    # 简介
    movie_plot = scrapy.Field()
    # 评分
    movie_score = scrapy.Field()
    # url
    movie_url = scrapy.Field()
    

