# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html



import scrapy
from scrapy.loader.processors import  TakeFirst, Identity



class DepopItem(scrapy.Item):
    ID =scrapy.Field(output_processor = TakeFirst())
    slug = scrapy.Field(output_processor = TakeFirst())
    date_created =  scrapy.Field(output_processor=TakeFirst())
    picture_1 = scrapy.Field(output_processor = TakeFirst())
    picture_2 = scrapy.Field(output_processor = TakeFirst())
    picture_3 = scrapy.Field(output_processor = TakeFirst())
    picture_4 = scrapy.Field(output_processor = TakeFirst())
    
    image_urls = scrapy.Field(output_processor=Identity())
    images = scrapy.Field()
    
    
