# 使用Scrapy编写爬虫

将两个爬虫写在了一起，爬虫的名字分别为```"xuetang"```和```"lianjia"```，其中，第二个爬虫爬取了全部19页的结果
## 主程序源码
```python
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
    for x in range(0, 20):
        url = 'https://bj.fang.lianjia.com/loupan/nhs1pg{}/'.format(x)
        start_urls.append(url)
    
    def parse(self, response):
        item = LianJiaItem()
        # /html/body/div[4]/ul[2]/li[2]/div/div[1]/a            [name]
        # /html/body/div[4]/ul[2]/li[2]/div/div[6]/div/span[1]  [price]
        # /html/body/div[4]/ul[2]/li[1]/div/div[3]/span         [area]
        for each in response.xpath('/html/body/div[4]/ul[2]/li'):
            item['name'] = each.xpath('div/div[1]/a/text()').get()
            item['price'] = each.xpath('div/div[6]/div/span[1]/text()').get() + each.xpath('div/div[6]/div/span[2]/text()').get()
            item['area'] = each.xpath('div/div[3]/span/text()').get()
            if (item['name'] and item['price'] and item['area']):
                item['area'] = item['area'].split(' ')[1]
                yield(item)
```
## 运行结果
运行```scrapy crawl xuetang```后本地```Data.json```文件中的结果：
```json
{"school": "清华大学", "course_num": "152"}
{"school": "台湾清华大学", "course_num": "1"}
{"school": "台湾交通大学", "course_num": "1"}
{"school": "斯坦福大学", "course_num": "1"}
{"school": "中央社会主义学院", "course_num": "0"}
{"school": "西安交通大学", "course_num": "24"}
{"school": "中南财经政法大学", "course_num": "7"}
{"school": "复旦大学", "course_num": "1"}
{"school": "北京理工大学", "course_num": "5"}
{"school": "中国科学技术大学", "course_num": "0"}
{"school": "吉林大学", "course_num": "5"}
{"school": "中国农业大学", "course_num": "4"}
{"school": "华南理工大学", "course_num": "18"}
{"school": "哈尔滨工业大学", "course_num": "14"}
{"school": "山东大学", "course_num": "5"}
{"school": "苏州大学", "course_num": "1"}
{"school": "东南大学", "course_num": "4"}
{"school": "台湾云林科技大学", "course_num": "0"}
{"school": "武汉大学", "course_num": "2"}
{"school": "华中科技大学", "course_num": "1"}
{"school": "同济大学", "course_num": "5"}
{"school": "南开大学", "course_num": "1"}
{"school": "北京工业大学", "course_num": "2"}
{"school": "南京理工大学", "course_num": "2"}
{"school": "西北工业大学", "course_num": "12"}
{"school": "台北艺术大学", "course_num": "0"}
{"school": "国防科技大学", "course_num": "11"}
{"school": "台湾静宜大学", "course_num": "1"}
{"school": "中南大学", "course_num": "11"}
{"school": "南京大学", "course_num": "6"}
{"school": "北京邮电大学", "course_num": "1"}
{"school": "武汉理工大学", "course_num": "4"}
{"school": "长安大学", "course_num": "1"}
{"school": "ACCA", "course_num": "8"}
{"school": "中国创业学院", "course_num": "9"}
{"school": "华东师范大学", "course_num": "1"}
{"school": "河南消防总队", "course_num": "1"}
{"school": "阿德莱德大学", "course_num": "7"}
{"school": "Microsoft", "course_num": "7"}
{"school": "陆军边海防学院", "course_num": "1"}
{"school": "麻省理工学院", "course_num": "65"}
{"school": "宁波大学", "course_num": "2"}
{"school": "南昌大学", "course_num": "2"}
{"school": "台湾宜兰大学", "course_num": "0"}
{"school": "莱斯大学", "course_num": "31"}
{"school": "北京大学", "course_num": "28"}
{"school": "台湾师范大学", "course_num": "0"}
{"school": "教育部在线教育研究中心", "course_num": "1"}
{"school": "科学松鼠会", "course_num": "1"}
{"school": "加州大学伯克利分校", "course_num": "32"}
{"school": "暨南大学", "course_num": "7"}
{"school": "瓦赫宁根大学", "course_num": "4"}
{"school": "中国人民解放军陆军工程大学", "course_num": "3"}
{"school": "韦尔斯利大学", "course_num": "5"}
{"school": "北京体育大学", "course_num": "2"}
{"school": "重庆大学", "course_num": "2"}
{"school": "中国石油大学（北京）", "course_num": "0"}
{"school": "华东理工大学", "course_num": "1"}
{"school": "河北师范大学", "course_num": "2"}
{"school": "哈尔滨工程大学", "course_num": "11"}
{"school": "浙江大学", "course_num": "1"}
{"school": "江苏大学", "course_num": "1"}
{"school": "中国人民大学", "course_num": "0"}
{"school": "西南交通大学", "course_num": "2"}
{"school": "台湾中原大学", "course_num": "0"}
{"school": "大叶大学 ", "course_num": "3"}
{"school": "昆士兰大学", "course_num": "12"}
{"school": "台湾空中大学", "course_num": "0"}
{"school": "台湾慈济大学", "course_num": "1"}
{"school": "红河学院", "course_num": "0"}
{"school": "黑龙江大学", "course_num": "3"}
{"school": "湖北大学", "course_num": "17"}
{"school": "集美大学", "course_num": "0"}
{"school": "河北工业大学", "course_num": "6"}
{"school": "北京交通大学", "course_num": "2"}
{"school": "北京语言大学", "course_num": "3"}
{"school": "北京师范大学", "course_num": "10"}
{"school": "昆明理工大学", "course_num": "6"}
{"school": "宁波城市职业技术学院", "course_num": "7"}
{"school": "温州大学", "course_num": "0"}
{"school": "浙江金融职业学院", "course_num": "4"}
{"school": "浙江纺织服装职业技术学院", "course_num": "1"}
{"school": "云南农业大学", "course_num": "0"}
{"school": "石河子大学", "course_num": "0"}
{"school": "兰州大学", "course_num": "2"}
{"school": "东北大学", "course_num": "14"}
{"school": "浙江农林大学", "course_num": "0"}
{"school": "北京服装学院", "course_num": "2"}
{"school": "福建农林大学", "course_num": "10"}
{"school": "防灾科技学院", "course_num": "0"}
{"school": "江苏大学", "course_num": "1"}
{"school": "中央民族大学", "course_num": "0"}
{"school": "宁波大红鹰学院", "course_num": "1"}
{"school": "陕西工业职业技术学院", "course_num": "0"}
{"school": "国际关系学院", "course_num": "0"}
{"school": "西安工程大学", "course_num": "0"}
{"school": "邢台学院", "course_num": "0"}
{"school": "燕山大学", "course_num": "1"}
{"school": "昆明医科大学", "course_num": "1"}
{"school": "辽宁对外经贸学院", "course_num": "5"}
{"school": "青海大学", "course_num": "1"}
{"school": "云南民族大学", "course_num": "0"}
{"school": "云南大学", "course_num": "2"}
{"school": "湖州师范学院", "course_num": "1"}
{"school": "大连海事大学", "course_num": "3"}
{"school": "河南科技大学", "course_num": "0"}
{"school": "洛阳理工学院", "course_num": "1"}
{"school": "青海师范大学", "course_num": "0"}
{"school": "北京林业大学", "course_num": "3"}
{"school": "首都师范大学", "course_num": "1"}
{"school": "重庆电子工程职业学院", "course_num": "0"}
{"school": "中国传媒大学", "course_num": "4"}
{"school": "贵州理工学院", "course_num": "1"}
{"school": "贵州中医药大学", "course_num": "0"}
{"school": "广州中医药大学", "course_num": "1"}
{"school": "深圳职业技术学院", "course_num": "0"}
{"school": "咸阳师范学院", "course_num": "0"}
{"school": "郑州大学", "course_num": "1"}
{"school": "电子科技大学", "course_num": "0"}
{"school": "台湾静宜大学", "course_num": "1"}
{"school": " 宝鸡文理学院", "course_num": "0"}
{"school": "北京工商大学", "course_num": "0"}
{"school": "首都医科大学", "course_num": "1"}
{"school": "长沙民政职业技术学院 ", "course_num": "0"}
{"school": "中国石油大学（北京）", "course_num": "0"}
{"school": "大连工业大学", "course_num": "2"}
{"school": "大连理工大学", "course_num": "6"}
{"school": "南方医科大学", "course_num": "0"}
{"school": "哈尔滨工程大学", "course_num": "11"}
{"school": "黑龙江大学", "course_num": "3"}
{"school": "辽宁工程技术大学", "course_num": "6"}
{"school": "华北电力大学", "course_num": "0"}
{"school": "东北大学", "course_num": "14"}
{"school": "汕头大学", "course_num": "1"}
{"school": "西南大学", "course_num": "2"}
{"school": "芜湖职业技术学院", "course_num": "0"}
{"school": "武汉科技大学", "course_num": "0"}
{"school": "西安建筑科技大学", "course_num": "0"}
{"school": "延安大学", "course_num": "0"}
{"school": "燕京理工学院", "course_num": "1"}
{"school": "杨凌职业技术学院", "course_num": "3"}
{"school": "清华大学", "course_num": "152"}
{"school": "北京大学", "course_num": "28"}
{"school": "哈佛大学", "course_num": "45"}
{"school": "麻省理工学院", "course_num": "65"}
{"school": "加州大学伯克利分校", "course_num": "32"}
{"school": "乔治城大学", "course_num": "8"}
{"school": "荷兰代尔夫特理工大学", "course_num": "25"}
{"school": "加州理工学院", "course_num": "4"}
{"school": "韦尔斯利大学", "course_num": "5"}
{"school": "康奈尔大学", "course_num": "6"}
{"school": "香港大学", "course_num": "4"}
{"school": "香港科技大学", "course_num": "9"}
{"school": "香港理工大学", "course_num": "3"}
{"school": "德克萨斯大学奥斯汀分校", "course_num": "18"}
{"school": "瑞典卡罗林斯卡学院", "course_num": "6"}
{"school": "昆士兰大学", "course_num": "12"}
{"school": "莱斯大学", "course_num": "31"}
{"school": "波士顿大学", "course_num": "13"}
{"school": "首尔国立大学", "course_num": "3"}
{"school": "印度理工学院孟买分校", "course_num": "5"}
{"school": "澳洲国立大学", "course_num": "7"}
{"school": "多伦多大学", "course_num": "4"}
{"school": "东京大学", "course_num": "1"}
{"school": "麦吉尔大学", "course_num": "4"}
{"school": "华盛顿大学", "course_num": "6"}
{"school": "瑞士洛桑联邦理工学院", "course_num": "11"}
{"school": "伯克利音乐学院", "course_num": "4"}
{"school": "鲁汶大学", "course_num": "5"}
{"school": "美国戴维森学院", "course_num": "5"}
{"school": "京都大学", "course_num": "3"}
{"school": "苏黎士联邦理工大学", "course_num": "5"}
{"school": "Linux基金会", "course_num": "3"}
{"school": "Learning By Giving基金会", "course_num": "1"}
{"school": "哥伦比亚大学", "course_num": "1"}
{"school": "库伯联盟学院", "course_num": "4"}
{"school": "达特茅斯学院", "course_num": "3"}
{"school": "泛美开发银行", "course_num": "3"}
{"school": "国际货币基金组织", "course_num": "4"}
{"school": "圣玛格丽特主教学校", "course_num": "3"}
{"school": "开放教育协会", "course_num": "6"}
{"school": "慕尼黑工业大学", "course_num": "2"}
{"school": "英属哥伦比亚大学", "course_num": "16"}
{"school": "芝加哥大学", "course_num": "2"}
{"school": "瓦赫宁根大学", "course_num": "4"}
```
运行运行```scrapy crawl lianjia```后本地```Data.json```文件中的结果：
```json
{"name": "懋源钓云台", "price": "2900 万/套(总价)", "area": "251㎡"}
{"name": "泰禾金府大院", "price": "1400 万/套(总价)", "area": "175㎡"}
{"name": "泰禾金府大院", "price": "1400 万/套(总价)", "area": "175㎡"}
{"name": "V7九间堂", "price": "1700 万/套(总价)", "area": "220-420㎡"}
{"name": "北京城建国誉府", "price": "48000 元/平(均价)", "area": "143-297㎡"}
{"name": "御汤山熙园", "price": "1800 万/套(总价)", "area": "300-470㎡"}
{"name": "华远和墅", "price": "1580 万/套(总价)", "area": "295㎡"}
{"name": "天资华府", "price": "42000 元/平(均价)", "area": "93-276㎡"}
{"name": "檀香府", "price": "55000 元/平(均价)", "area": "208-320㎡"}
{"name": "观山源墅", "price": "47500 元/平(均价)", "area": "290-437㎡"}
{"name": "绿城西府海棠", "price": "52024 元/平(均价)", "area": "90-135㎡"}
{"name": "北京东湾", "price": "68500 元/平(均价)", "area": "58-130㎡"}
{"name": "天恒水岸壹号", "price": "1000 万/套(总价)", "area": "184-198㎡"}
{"name": "观唐云鼎", "price": "460 万/套(总价)", "area": "170㎡"}
{"name": "运河铭著", "price": "46000 元/平(均价)", "area": "100-140㎡"}
{"name": "万年广阳郡九号", "price": "48500 元/平(均价)", "area": "139-166㎡"}
{"name": "绿城西府海棠", "price": "52024 元/平(均价)", "area": "90-135㎡"}
{"name": "北京东湾", "price": "68500 元/平(均价)", "area": "58-130㎡"}
{"name": "天恒水岸壹号", "price": "1000 万/套(总价)", "area": "184-198㎡"}
{"name": "观唐云鼎", "price": "460 万/套(总价)", "area": "170㎡"}
{"name": "运河铭著", "price": "46000 元/平(均价)", "area": "100-140㎡"}
{"name": "万年广阳郡九号", "price": "48500 元/平(均价)", "area": "139-166㎡"}
{"name": "首开璞瑅公馆", "price": "106000 元/平(均价)", "area": "236㎡"}
{"name": "华远裘马四季", "price": "60000 元/平(均价)", "area": "156-191㎡"}
{"name": "天恒水岸壹号", "price": "600 万/套(总价)", "area": "108-138㎡"}
{"name": "尚峯壹號", "price": "36000 元/平(均价)", "area": "107-265㎡"}
{"name": "电建金地华宸", "price": "64000 元/平(均价)", "area": "180-247㎡"}
{"name": "中国铁建花语金郡", "price": "71000 元/平(均价)", "area": "150㎡"}
{"name": "中国铁建万科翡翠长安", "price": "57000 元/平(均价)", "area": "166-204㎡"}
{"name": "中骏西山天璟", "price": "65000 元/平(均价)", "area": "117-155㎡"}
{"name": "首开璞瑅公馆", "price": "106000 元/平(均价)", "area": "236㎡"}
{"name": "华远裘马四季", "price": "60000 元/平(均价)", "area": "156-191㎡"}
{"name": "玺萌壹號院", "price": "99500 元/平(均价)", "area": "457-548㎡"}
{"name": "紫辰院", "price": "120000 元/平(均价)", "area": "266-345㎡"}
{"name": "天恒摩墅", "price": "370 万/套(总价)", "area": "134-162㎡"}
{"name": "兴创荣墅", "price": "1100 万/套(总价)", "area": "240-411㎡"}
{"name": "景粼原著", "price": "4000 万/套(总价)", "area": "479㎡"}
{"name": "首创禧瑞山", "price": "830 万/套(总价)", "area": "141-226㎡"}
{"name": "观山源墅", "price": "47500 元/平(均价)", "area": "92-150㎡"}
{"name": "北辰墅院1900", "price": "43000 元/平(均价)", "area": "120-136㎡"}
{"name": "利锦府府上", "price": "60000 元/平(均价)", "area": "280-304㎡"}
{"name": "合景中心", "price": "65000 元/平(均价)", "area": "77-114㎡"}
{"name": "中粮天恒天悦壹号", "price": "82000 元/平(均价)", "area": "126-175㎡"}
{"name": "万科大都会滨江N2", "price": "65000 元/平(均价)", "area": "143-275㎡"}
{"name": "香悦四季", "price": "562 万/套(总价)", "area": "159-302㎡"}
{"name": "K2十里春风", "price": "28400 元/平(均价)", "area": "73-89㎡"}
{"name": "K2十里春风", "price": "500 万/套(总价)", "area": "155-156㎡"}
{"name": "奥园北京源墅", "price": "370 万/套(总价)", "area": "120-240㎡"}
{"name": "北京城建·龙樾西山", "price": "55000 元/平(均价)", "area": "118-134㎡"}
{"name": "北辰墅院1900", "price": "43000 元/平(均价)", "area": "251-282㎡"}
{"name": "首创天阅西山", "price": "1500 万/套(总价)", "area": "180-211㎡"}
{"name": "西山燕庐", "price": "65000 元/平(均价)", "area": "123-172㎡"}
{"name": "北科建泰禾丽春湖院子", "price": "1020 万/套(总价)", "area": "468-800㎡"}
{"name": "绿地海珀云翡", "price": "67000 元/平(均价)", "area": "102-178㎡"}
{"name": "泰禾昌平拾景园", "price": "1100 万/套(总价)", "area": "210-480㎡"}
{"name": "国瑞熙墅", "price": "1400 万/套(总价)", "area": "314-329㎡"}
{"name": "领秀翡翠墅", "price": "51000 元/平(均价)", "area": "137-187㎡"}
{"name": "华润西山墅", "price": "760 万/套(总价)", "area": "126-175㎡"}
{"name": "北京怡园", "price": "46000 元/平(均价)", "area": "70-170㎡"}
{"name": "丽景长安", "price": "52000 元/平(均价)", "area": "152-190㎡"}
{"name": "中冶德贤公馆", "price": "1430 万/套(总价)", "area": "186-215㎡"}
{"name": "燕西华府", "price": "52000 元/平(均价)", "area": "195-851㎡"}
{"name": "首开住总熙悦安郡", "price": "79500 元/平(均价)", "area": "83-137㎡"}
{"name": "远洋长安国际中心", "price": "33000 元/平(均价)", "area": "1118-1120㎡"}
{"name": "台湖银河湾", "price": "1100 万/套(总价)", "area": "146-200㎡"}
{"name": "棠颂别墅璟庐", "price": "1900 万/套(总价)", "area": "250-270㎡"}
{"name": "中铁华侨城和园", "price": "55000 元/平(均价)", "area": "121-295㎡"}
{"name": "中海北京世家", "price": "1800 万/套(总价)", "area": "280-380㎡"}
{"name": "都丽华府", "price": "300 万/套(总价)", "area": "90-172㎡"}
{"name": "中粮京西祥云", "price": "58000 元/平(均价)", "area": "115-140㎡"}
{"name": "燕西华府", "price": "49800 元/平(均价)", "area": "60-125㎡"}
{"name": "珠江阙", "price": "73000 元/平(均价)", "area": "330㎡"}
{"name": "远洋五里春秋", "price": "1300 万/套(总价)", "area": "330-500㎡"}
{"name": "林肯时代", "price": "42000 元/平(均价)", "area": "103-223㎡"}
{"name": "公园十七区", "price": "55711 元/平(均价)", "area": "90-144㎡"}
{"name": "通泰国际公馆", "price": "52000 元/平(均价)", "area": "53-89㎡"}
{"name": "首开熙悦观湖", "price": "280 万/套(总价)", "area": "89㎡"}
{"name": "金地·大湖风华", "price": "330 万/套(总价)", "area": "67-139㎡"}
{"name": "金辰府", "price": "53000 元/平(均价)", "area": "89-143㎡"}
{"name": "熙湖悦著", "price": "34000 元/平(均价)", "area": "73-353㎡"}
{"name": "华发中央公园", "price": "41000 元/平(均价)", "area": "85-139㎡"}
{"name": "中海北京世家", "price": "58000 元/平(均价)", "area": "370-380㎡"}
{"name": "翡翠公园", "price": "1100 万/套(总价)", "area": "260-350㎡"}
{"name": "东方蓝海中心", "price": "55000 元/平(均价)", "area": "104-136㎡"}
{"name": "顺鑫颐和天璟", "price": "405 万/套(总价)", "area": "108-132㎡"}
{"name": "顺鑫颐和天璟", "price": "870 万/套(总价)", "area": "241-486㎡"}
{"name": "未来公元", "price": "60800 元/平(均价)", "area": "104-147㎡"}
{"name": "住总香榭8号", "price": "1450 万/套(总价)", "area": "139-145㎡"}
{"name": "通州万国城MOMA", "price": "71000 元/平(均价)", "area": "112-149㎡"}
{"name": "领秀翡翠墅", "price": "1430 万/套(总价)", "area": "270-335㎡"}
{"name": "奥园北京源墅", "price": "23000 元/平(均价)", "area": "110㎡"}
{"name": "北京城建北京合院", "price": "47000 元/平(均价)", "area": "120㎡"}
{"name": "中骏西山天璟", "price": "63000 元/平(均价)", "area": "140-220㎡"}
{"name": "珠光御景西园", "price": "40000 元/平(均价)", "area": "117-156㎡"}
{"name": "和光尘樾", "price": "79800 元/平(均价)", "area": "220-290㎡"}
{"name": "融尚未来", "price": "1250 万/套(总价)", "area": "138-220㎡"}
{"name": "和光尘樾", "price": "3800 万/套(总价)", "area": "380㎡"}
{"name": "国锐金嵿", "price": "78000 元/平(均价)", "area": "285㎡"}
{"name": "首开香溪郡", "price": "45500 元/平(均价)", "area": "90-207㎡"}
{"name": "西山艺境华墅", "price": "42000 元/平(均价)", "area": "205-380㎡"}
{"name": "浅山香邑", "price": "270 万/套(总价)", "area": "89-130㎡"}
{"name": "金隅·金麟府", "price": "52695 元/平(均价)", "area": "89-141㎡"}
{"name": "天润福熙大道", "price": "88000 元/平(均价)", "area": "199-251㎡"}
{"name": "北京城建海梓府", "price": "1400 万/套(总价)", "area": "280-360㎡"}
{"name": "中海丽春湖墅·温榆府", "price": "1100 万/套(总价)", "area": "304㎡"}
{"name": "梵悦108", "price": "150000 元/平(均价)", "area": "108-260㎡"}
{"name": "旭辉城", "price": "35000 元/平(均价)", "area": "75-116㎡"}
{"name": "首创远洋禧瑞天著", "price": "52695 元/平(均价)", "area": "89-138㎡"}
{"name": "世茂西山龙胤", "price": "4000 万/套(总价)", "area": "680-1280㎡"}
{"name": "华润理想国", "price": "49520 元/平(均价)", "area": "90-140㎡"}
{"name": "首开保利熙悦林语", "price": "1100 万/套(总价)", "area": "220-280㎡"}
{"name": "檀香府", "price": "50000 元/平(均价)", "area": "124-170㎡"}
{"name": "金融街金悦府", "price": "55016 元/平(均价)", "area": "73-129㎡"}
{"name": "中海丽春湖墅·温榆府", "price": "470 万/套(总价)", "area": "89㎡"}
{"name": "天瑞宸章", "price": "1500 万/套(总价)", "area": "120-375㎡"}
{"name": "首创远洋·禧瑞春秋", "price": "68924 元/平(均价)", "area": "266-500㎡"}
{"name": "东方太阳城", "price": "2100 万/套(总价)", "area": "411-609㎡"}
{"name": "壹亮马", "price": "98000 元/平(均价)", "area": "171-234㎡"}
{"name": "中粮天恒天悦壹号", "price": "2000 万/套(总价)", "area": "220-280㎡"}
{"name": "中海云熙", "price": "37700 元/平(均价)", "area": "76-89㎡"}
{"name": "龙湾别墅", "price": "1335 万/套(总价)", "area": "218-265㎡"}
{"name": "大兴金茂悦", "price": "37500 元/平(均价)", "area": "74-104㎡"}
{"name": "元熙华府", "price": "82000 元/平(均价)", "area": "62-146㎡"}
{"name": "京贸国际公馆", "price": "660 万/套(总价)", "area": "91-127㎡"}
{"name": "凯德麓语", "price": "35000 元/平(均价)", "area": "280-863㎡"}
{"name": "招商都会湾", "price": "400 万/套(总价)", "area": "88-135㎡"}
{"name": "京贸国际城·峰景", "price": "72000 元/平(均价)", "area": "69-140㎡"}
{"name": "华润西山墅", "price": "1700 万/套(总价)", "area": "338-447㎡"}
{"name": "观唐云鼎", "price": "31000 元/平(均价)", "area": "138-190㎡"}
{"name": "北京城建琨廷", "price": "28000 元/平(均价)", "area": "85-176㎡"}
{"name": "保利首开天誉", "price": "4000 万/套(总价)", "area": "160-350㎡"}
{"name": "新潮嘉园二期", "price": "58500 元/平(均价)", "area": "65-80㎡"}
{"name": "朝青知筑", "price": "78000 元/平(均价)", "area": "121-140㎡"}
{"name": "中海云筑", "price": "340 万/套(总价)", "area": "89㎡"}
{"name": "中海云筑", "price": "719 万/套(总价)", "area": "266㎡"}
{"name": "远洋五里春秋", "price": "52024 元/平(均价)", "area": "90-130㎡"}
{"name": "和锦薇棠", "price": "88000 元/平(均价)", "area": "178-290㎡"}
{"name": "祥云赋", "price": "55583 元/平(均价)", "area": "90㎡"}
{"name": "泰禾金府大院", "price": "2400 万/套(总价)", "area": "362-504㎡"}
{"name": "中海金樾和著", "price": "37000 元/平(均价)", "area": "89-127㎡"}
{"name": "金地悦风华", "price": "55000 元/平(均价)", "area": "89-134㎡"}
{"name": "颐璟万和", "price": "55016 元/平(均价)", "area": "80-135㎡"}
{"name": "和悦华锦", "price": "52695 元/平(均价)", "area": "89-135㎡"}
{"name": "和悦华玺", "price": "49800 元/平(均价)", "area": "89-129㎡"}
{"name": "尊悦光华", "price": "1700 万/套(总价)", "area": "133-171㎡"}
{"name": "天竺悦府", "price": "59500 元/平(均价)", "area": "125-132㎡"}
{"name": "首创·河著", "price": "820 万/套(总价)", "area": "248-310㎡"}
{"name": "华萃西山", "price": "47000 元/平(均价)", "area": "85-128㎡"}
{"name": "招商雍合府", "price": "55800 元/平(均价)", "area": "84-131㎡"}
{"name": "中铁·诺德春风和院", "price": "67702 元/平(均价)", "area": "89-129㎡"}
{"name": "葛洲坝中国府", "price": "125000 元/平(均价)", "area": "185-240㎡"}
{"name": "华萃西山", "price": "780 万/套(总价)", "area": "135-220㎡"}
{"name": "葛洲坝北京紫郡兰园", "price": "53000 元/平(均价)", "area": "89-139㎡"}
{"name": "兴创屹墅", "price": "2900 万/套(总价)", "area": "464㎡"}
{"name": "恒大华府", "price": "88000 元/平(均价)", "area": "271-338㎡"}
{"name": "天恒乐墅", "price": "738 万/套(总价)", "area": "184-253㎡"}
{"name": "中粮瑞府", "price": "4600 万/套(总价)", "area": "468-883㎡"}
{"name": "MAHA缦合北京", "price": "135000 元/平(均价)", "area": "450-520㎡"}
{"name": "丽景长安二期", "price": "52000 元/平(均价)", "area": "152-190㎡"}
{"name": "山水文园五期", "price": "1300 万/套(总价)", "area": "153㎡"}
{"name": "卓越万科翡翠山晓", "price": "425 万/套(总价)", "area": "89㎡"}
{"name": "金地旭辉·江山风华", "price": "55800 元/平(均价)", "area": "89-136㎡"}
{"name": "水岸雁栖", "price": "34000 元/平(均价)", "area": "56-152㎡"}
{"name": "中铁诺德阅墅", "price": "1200 万/套(总价)", "area": "220-320㎡"}
{"name": "中铁华侨城和园", "price": "50000 元/平(均价)", "area": "198-370㎡"}
{"name": "金地·大湖风华", "price": "500 万/套(总价)", "area": "139㎡"}
{"name": "懋源·璟岳", "price": "2300 万/套(总价)", "area": "218㎡"}
{"name": "懋源·璟岳", "price": "5500 万/套(总价)", "area": "465-590㎡"}
{"name": "山屿西山著", "price": "53000 元/平(均价)", "area": "225㎡"}
{"name": "御世佳府", "price": "1300 万/套(总价)", "area": "222-264㎡"}
{"name": "碧桂园世奥龙鼎", "price": "300 万/套(总价)", "area": "89-135㎡"}
{"name": "合景天汇广场", "price": "38000 元/平(均价)", "area": "89-117㎡"}
```