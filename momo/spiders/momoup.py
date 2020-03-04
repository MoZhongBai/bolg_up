# -*- coding: utf-8 -*-
import scrapy
import json
from momo.getproxy import get_artical_list
import random

class MomoupSpider(scrapy.Spider):
    name = 'momoup'
    allowed_domains = ['maimemo.com']
    atrical_title,artical_dict,start_urls = get_artical_list('https://blog.csdn.net/dfgdgfbb')
    num = 0

    def parse(self, response):
        if response.status == 200:
            self.num += 1
            print('正在刷博客访问量,次数：%d' % self.num)
            try:
                yield scrapy.Request(self.start_urls[random.randint(0,len(self.start_urls))],dont_filter=True)
            except :
                yield scrapy.Request(self.start_urls[random.randint(0,len(self.start_urls))],dont_filter=True)