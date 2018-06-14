# -*- coding: utf-8 -*-
import scrapy
from douban.items import DoubanItem
from get_url import getUrls

import sys
reload(sys)
sys.setdefaultencoding("utf-8")


class DoubanmovieSpider(scrapy.Spider):

    name = 'doubanmovie'
    allowed_domains = ['movie.douban.com']
    start_urls = getUrls()

    def parse(self, response):

     	item = DoubanItem()  
        item['movie_name'] = response.xpath('//span[@property="v:itemreviewed"]/text()').extract()  
        item['movie_director'] = response.xpath('//a[@rel="v:directedBy"]/text()').extract()  
        item['movie_writer'] = response.xpath('//*[@id="info"]/span[2]/span[2]/a/text()').extract()  
        item['movie_starring'] = response.xpath('//a[@rel="v:starring"]/text()').extract()  
        item['movie_type'] = response.xpath('//span[@property="v:genre"]/text()').extract()  
        #item['movie_language'] = response.xpath('//*[@id="info"]').re(r'</span> (.*)<br>\n')[2]  
        item['movie_startdate'] = response.xpath('//span[@property="v:initialReleaseDate"]/text()').extract()  
        item['movie_length'] = response.xpath('//span[@property="v:runtime"]/text()').extract()  
        item['movie_score'] = response.xpath('//strong[@property="v:average"]/text()').extract()  
        # item['movie_5score'] = response.xpath('//span[@class="rating_per"][1]/text()').extract()  
        # item['movie_4score'] = response.xpath('//span[@class="rating_per"][2]/text()').extract()  
        # item['movie_3score'] = response.xpath('//span[@class="rating_per"][3]/text()').extract()  
        # item['movie_2score'] = response.xpath('//span[@class="rating_per"][4]/text()').extract()  
        # item['movie_1score'] = response.xpath('//span[@class="rating_per"][5]/text()').extract()  
        item['movie_plot'] = response.xpath('//*[@id="link-report"]/span/text()').re(r'\S+')  
        item['movie_url'] = response.url
  
 		yield item
        # return item

    	# url = ""
       	# yield scrapy.Request(url, callback=self.parse_each_movie)

    # def parse_each_movie(self,response):
    #     item = DoubanItem()  
    #     item['movie_name'] = response.xpath('//span[@property="v:itemreviewed"]/text()').extract()  
    #     item['movie_director'] = response.xpath('//a[@rel="v:directedBy"]/text()').extract()  
    #     item['movie_writer'] = response.xpath('//*[@id="info"]/span[2]/span[2]/a/text()').extract()  
    #     item['movie_starring'] = response.xpath('//a[@rel="v:starring"]/text()').extract()  
    #     item['movie_type'] = response.xpath('//span[@property="v:genre"]/text()').extract()  
    #     #item['movie_language'] = response.xpath('//*[@id="info"]').re(r'</span> (.*)<br>\n')[2]  
    #     item['movie_startdate'] = response.xpath('//span[@property="v:initialReleaseDate"]/text()').extract()  
    #     item['movie_length'] = response.xpath('//span[@property="v:runtime"]/text()').extract()  
    #     item['movie_score'] = response.xpath('//strong[@property="v:average"]/text()').extract()  
    #     # item['movie_5score'] = response.xpath('//span[@class="rating_per"][1]/text()').extract()  
    #     # item['movie_4score'] = response.xpath('//span[@class="rating_per"][2]/text()').extract()  
    #     # item['movie_3score'] = response.xpath('//span[@class="rating_per"][3]/text()').extract()  
    #     # item['movie_2score'] = response.xpath('//span[@class="rating_per"][4]/text()').extract()  
    #     # item['movie_1score'] = response.xpath('//span[@class="rating_per"][5]/text()').extract()  
    #     item['movie_plot'] = response.xpath('//*[@id="link-report"]/span/text()').re(r'\S+')  
    #     item['movie_url'] = response.url
  
 
    #     yield item

