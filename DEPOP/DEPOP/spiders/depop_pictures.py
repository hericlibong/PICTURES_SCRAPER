import scrapy
import json
from scrapy.loader import ItemLoader
from DEPOP.items import DepopItem



class DepopPicturesSpider(scrapy.Spider):
    name = "depop_pictures"
    allowed_domains = ["webapi.depop.com"]
    start_urls = ["https://webapi.depop.com/api/v2/search/products/?categories=11&cursor=NHw3MnwxNjc5NjIyODkx&itemsPerPage=24&country=gb&currency=GBP&sort=relevance"]

    def parse(self, response):
        parse_json = json.loads(response.body)
        data = parse_json['products']
        for item in data : 
            l = ItemLoader(item=DepopItem(), response=response)
            l.replace_value('ID', item.get('id'))
            l.replace_value('slug', item.get('slug'))
            l.replace_value('date_created', item.get('dateCreated'))
            for i in range(4):
                picture = item['pictures'][i]['1280'] if len(item['pictures']) > i else None
                #l.replace_value(f'picture_{i+1}', picture)
                
                if picture:
                    field_name = f'picture_{i+1}'
                    l.add_value(field_name, picture)
                    l.add_value('image_urls', picture)
           
            yield l.load_item()
            
       # Set pagination     
        cursor = parse_json['meta']['cursor']
        next_page = parse_json['meta']['hasMore']
        
        if next_page :
            url = f'https://webapi.depop.com/api/v2/search/products/?categories=11&cursor={cursor}&itemsPerPage=24&country=gb&currency=GBP&sort=relevance'
            yield scrapy.Request(url=url, callback=self.parse)
