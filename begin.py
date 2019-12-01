from scrapy import cmdline

with open('Data.csv', 'w') as f:
    f.write('"name","location1","location2","location3","room_type","area","total_price","avg_price"\n')

cmdline.execute('scrapy crawl lianjia'.split())