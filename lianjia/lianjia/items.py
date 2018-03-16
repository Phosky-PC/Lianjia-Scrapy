# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class LianjiaItem(scrapy.Item):
    # define the fields for your item here like:
    # 房屋标题
    house_title = scrapy.Field()
    # 详情页url
    house_detail_url = scrapy.Field()
    # 售价
    house_price = scrapy.Field()
    # 每平方米价格
    house_single_price = scrapy.Field()
    # 面积
    house_area = scrapy.Field()
    # 地址
    house_adders = scrapy.Field()
    # 发布时间
    house_date = scrapy.Field()
    # 房屋简介
    house_introduction = scrapy.Field()
    # 房型
    house_room_type = scrapy.Field()
    # 房屋朝向
    house_heading = scrapy.Field()
    # 是否有电梯
    house_elevator = scrapy.Field()
    # 楼型
    house_building_type = scrapy.Field()
    # 楼层
    house_floor = scrapy.Field()
    # 装修风格
    house_decoration = scrapy.Field()
    # 房屋年代
    house_year = scrapy.Field()
    # 房屋用途
    house_use = scrapy.Field()
    # 权属
    house_ownership = scrapy.Field()
    # 小区
    house_commiunity = scrapy.Field()

