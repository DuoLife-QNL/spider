import scrapy
from hw.items import XueTangItem, LianJiaItem # 引入item对象
class XueTangSpider(scrapy.Spider):  
    name = "xuetang" # 爬虫的名字是 xuetang
    allowed_domains = ["www.xuetangx.com/"]  #允许爬取的网站域名
    start_urls = ["http://www.xuetangx.com/partners"] #开始爬取的url

    def parse(self, response): #解析爬取的内容
        item = XueTangItem() #生成一个在 items.py 中定义好的 xuetangitem 对象用于接收爬取的数据

        for each in response.xpath("/html/body/*/section/ul/*/a/div[2]"):
            item['school'] = each.xpath("h3/text()").get()    
            item['course_num'] = each.xpath("p/text()").get().replace('门课程', '')
            if(item['school'] and item['course_num'] ): #去掉值为空的数据
                yield(item) #返回 item 数据给到 pipelines 模块


class LianJiaSpider(scrapy.Spider):
    name = 'lianjia'
    allowed_domains = ['bj.fang.lianjia.com']
    start_urls = []
    for x in range(1, 21):
        url = 'https://bj.fang.lianjia.com/loupan/nhs1pg{}/'.format(x)
        start_urls.append(url)
    
    def parse(self, response):
        item = LianJiaItem()
        # /html/body/div[4]/ul[2]/li[2]/div/div[1]/a            [name]
        # /html/body/div[4]/ul[2]/li[2]/div/div[6]/div/span[1]  [price]
        # /html/body/div[4]/ul[2]/li[1]/div/div[3]/span         [area]
        # /html/body/div[4]/ul[2]/li[1]/div/div[2]/span[1]      [location1]
        # /html/body/div[4]/ul[2]/li[1]/div/div[2]/span[2]      [location2]
        # /html/body/div[4]/ul[2]/li[1]/div/div[2]/a            [location3]
        # /html/body/div[4]/ul[2]/li[1]/div/a/span[1]           [room_type]
        # /html/body/div[4]/ul[2]/li[1]/div/div[6]/div[2]       [total_price]
        for each in response.xpath('/html/body/div[4]/ul[2]/li'):
            # name
            item['name'] = each.xpath('div/div[1]/a/text()').get()
            # locationn
            item['location1'] = each.xpath('div/div[2]/span[1]/text()').get()
            item['location2'] = each.xpath('div/div[2]/span[2]/text()').get()
            item['location3'] = each.xpath('div/div[2]/a/text()').get()
            # room_type
            item['room_type'] = each.xpath('div/a/span[1]/text()').get()
            if item['room_type'] is None:
                item['room_type'] = ''
            # area
            area = each.xpath('div/div[3]/span/text()').get()
            if area:
                area = area.split(' ')[1].split('-')[0]
                i = filter(str.isdigit, list(area))
                item['area'] = ''.join(list(i))
            else:
                item['area'] = ''
            # total_price
            origin_total_price = each.xpath('div/div[6]/div[2]/text()').get()
            if origin_total_price:
                i = filter(str.isdigit, list(origin_total_price))
                total_price = ''.join(list(i))    
                item['total_price'] = total_price
            else:
                item['total_price'] = ''
            # average price
            unit = each.xpath('div/div[6]/div/span[2]/text()').get()
            if unit:
                unit = unit.split('(')[1].split(')')[0]
                if unit == '总价':
                    item['avg_price'] = ''
                elif unit == '均价':
                    avg_price = int(each.xpath('div/div[6]/div/span[1]/text()').get()) / 10000
                    item['avg_price'] = "{:.4f}".format(avg_price)
            else:
                item['avg_price'] = ''
            # item['price'] = each.xpath('div/div[6]/div/span[1]/text()').get() + each.xpath('div/div[6]/div/span[2]/text()').get()
            # if (item['name'] or item['price'] or item['area']):
            yield(item)