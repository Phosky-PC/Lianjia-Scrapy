# -*- coding: utf-8 -*-
import scrapy
from lianjia.items import LianjiaItem

class SpiderSpider(scrapy.Spider):
    name = 'spider'
    allowed_domains = ['lianjia.com']
    start_urls = ['https://m.lianjia.com/bj']

    def start_requests(self):
        url = 'https://m.lianjia.com/bj/ershoufang/pg{}/'
        for i in range(1, 139):
            next_url = url.format(i)
            yield scrapy.Request(next_url, callback=self.parse)

    def parse(self, response):
        # get index data
        index_data_list = response.xpath('//div[@class="mod_cont"]/ul[@class="lists"]/li[@class="pictext"]')
        for index_data in index_data_list:
            host_url = 'https://m.lianjia.com'
            house_detail_url = host_url + index_data.xpath('./a/@href').extract_first() if len(index_data.xpath('./a/@href')) > 0 else None
            yield scrapy.Request(house_detail_url, callback=self.parse_detail)

    def parse_detail(self, response):

       # get detail data
        house_detail_url = response.url
        house_title = response.xpath('//h3[@class="house_desc lazyload_ulog"]/text()').extract_first().replace("\n", "").strip() if len(response.xpath('//h3[@class="house_desc lazyload_ulog"]/text()')) > 0 else None
        house_price = response.xpath('//h3[@class="similar_data"]/div[1]/p[2]/span[1]/text()').extract_first().split("万")[0] if len(response.xpath('//h3[@class="similar_data"]/div/p[2]/span[1]/text()')) > 0 else None
        house_single_price = response.xpath('//ul[@class="house_description big lightblack"]/li[1]/text()').extract_first().split("元/平")[0] if len(response.xpath('//ul[@class="house_description big lightblack"]/li[1]/text()')) > 0 else None
        house_room_type = response.xpath('//h3[@class="similar_data"]/div[2]/p[2]/text()').extract_first() if len(response.xpath('//h3[@class="similar_data"]/div[2]/p[2]/text()')) > 0 else None
        house_heading = response.xpath('//ul[@class="house_description big lightblack"]/li[3]/text()').extract_first() if len(response.xpath('//ul[@class="house_description big lightblack"]/li[3]/text()')) > 0 else None
        house_floor = response.xpath('//ul[@class="house_description big lightblack"]/li[4]/text()').extract_first() if len(response.xpath('//ul[@class="house_description big lightblack"]/li[4]/text()')) > 0 else None
        house_building_type = response.xpath('//ul[@class="house_description big lightblack"]/li[5]/text()').extract_first() if len(response.xpath('//ul[@class="house_description big lightblack"]/li[5]/text()')) > 0 else None
        house_elevator = response.xpath('//ul[@class="house_description big lightblack"]/li[6]/text()').extract_first() if len(response.xpath('//ul[@class="house_description big lightblack"]/li[6]/text()')) > 0 else None
        house_decoration = response.xpath('//ul[@class="house_description big lightblack"]/li[7]/text()').extract_first() if len(response.xpath('//ul[@class="house_description big lightblack"]/li[7]/text()')) > 0 else None
        house_year = response.xpath('//ul[@class="house_description big lightblack"]/li[8]/text()').extract_first() if len(response.xpath('//ul[@class="house_description big lightblack"]/li[8]/text()')) > 0 else None
        house_use = response.xpath('//ul[@class="house_description big lightblack"]/li[9]/text()').extract_first() if len(response.xpath('//ul[@class="house_description big lightblack"]/li[9]/text()')) > 0 else None
        house_ownership = response.xpath('//ul[@class="house_description big lightblack"]/li[10]/text()').extract_first() if len(response.xpath('//ul[@class="house_description big lightblack"]/li[10]/text()')) > 0 else None
        house_commiunity = response.xpath('//ul[@class="house_description big lightblack"]/li[12]/a/text()').extract_first()if len(response.xpath('//ul[@class="house_description big lightblack"]/li[12]/a/text()')) > 0 else None
        house_area = response.xpath('//h3[@class="similar_data"]/div[3]/p[2]/text()').extract_first().split("m²")[0] if len(response.xpath('//h3[@class="similar_data"]/div[3]/p[2]/text()')) > 0 else None
        house_introduction = ''.join(response.xpath('//div[@class="mod_cont fiveline house_intro_mod_cont"]/text()').extract()).replace("\n", "").replace(" ", "") if len(response.xpath('//div[@class="mod_cont fiveline house_intro_mod_cont"]/text()')) > 0 else None
        house_adders = ''.join(response.xpath('//div[@class="sub_mod_box location"]/div/a/div/div[@class="marker_desc"]/p/text()').extract()).replace("\n", "").replace(" ", "") if len(response.xpath('//div[@class="sub_mod_box location"]/div/a/div/div[@class="marker_desc"]/p/text()')) > 0 else None
        house_date = response.xpath('//ul[@class="house_description big lightblack"]/li[2]/text()').extract_first() if len(response.xpath('//ul[@class="house_description big lightblack"]/li[2]/text()')) > 0 else None

        item = LianjiaItem()

        item["house_title"] = house_title
        item["house_price"] = house_price
        item["house_single_price"] = house_single_price
        item["house_room_type"] = house_room_type
        item["house_heading"] = house_heading
        item["house_floor"] = house_floor
        item["house_building_type"] = house_building_type
        item["house_elevator"] = house_elevator
        item["house_decoration"] = house_decoration
        item["house_year"] = house_year
        item["house_use"] = house_use
        item["house_ownership"] = house_ownership
        item["house_commiunity"] = house_commiunity
        item["house_detail_url"] = house_detail_url
        item["house_area"] = house_area
        item["house_introduction"] = house_introduction
        item["house_adders"] = house_adders
        item["house_date"] = house_date

        yield item

