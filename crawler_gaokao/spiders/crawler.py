
import scrapy
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors import LinkExtractor

from crawler_gaokao.items import CrawlerGaokaoItem


class MySpider(CrawlSpider):
    name = 'myspider'
    allowed_domains = ['www.heao.gov.cn']
    #www.heao.gov.cn / JHCX / PZ / enrollplan / SchoolList.aspx
    start_urls = ['http://www.heao.gov.cn/JHCX/PZ/enrollplan/PCList.aspx?YXDH=' + str(i).zfill(4) for i in range(9953)]

    rules = (
        # 提取匹配 'category.php' (但不匹配 'subsection.php') 的链接并跟进链接(没有callback意味着follow默认为True)
        #Rule(LinkExtractor(allow=('SchoolList\.aspx', ), deny=('PlanContent\.aspx', 'default\.aspx', 'PCList\.aspx'))),

        # 提取匹配 'item.php' 的链接并使用spider的parse_item方法进行分析
        #Rule(LinkExtractor(allow=('SchoolList\.aspx', )), callback='parse_item'),

        # 下面是符合规则的网址,但是不抓取内容,只是提取该页的链接(这里网址是虚构的,实际使用时请替换)
        # Rule(SgmlLinkExtractor(allow=(r'http://test_url/test?page_index=\d+'))),
        # 下面是符合规则的网址,提取内容,(这里网址是虚构的,实际使用时请替换)
        Rule(LinkExtractor(allow=(r'http://www.heao.gov.cn/JHCX/PZ/enrollplan/PCList.aspx?YXDH=\d+')), callback="parse"),
    )

    def parse(self, response):
        self.log('Hi, this is an item page! %s' % response.url)

        item = CrawlerGaokaoItem()
        item['school_id'] = response.xpath('//*[@id="SpanPlanSchoolInfo"]/table[1]/tr[2]/td/table/tr[1]/td[2]/text()').extract_first()
        item['school_name'] = response.xpath('//*[@id="SpanPlanSchoolInfo"]/table[1]/tr[2]/td/table/tr[1]/td[4]/text()').extract_first()
        item['price'] = response.xpath('//*[@id="SpanPlanSchoolInfo"]/table[1]/tr[2]/td/table/tr[6]/td[2]/text()').extract_first()

        item['pici1'] = response.xpath(
            '//*[@id="SpanPlanSchoolInfo"]/table[2]/tr[3]/td/table/tr[2]/td[1]/a/text()').extract_first()
        item['count1'] = response.xpath(
            '//*[@id="SpanPlanSchoolInfo"]/table[2]/tr[3]/td/table/tr[2]/td[2]/text()').extract_first()
        item['pici2'] = response.xpath(
            '//*[@id="SpanPlanSchoolInfo"]/table[2]/tr[3]/td/table/tr[3]/td[1]/a/text()').extract_first()
        item['count2'] = response.xpath(
            '//*[@id="SpanPlanSchoolInfo"]/table[2]/tr[3]/td/table/tr[3]/td[2]/text()').extract_first()

        item['pici3'] = response.xpath(
            '//*[@id="SpanPlanSchoolInfo"]/table[2]/tr[3]/td/table/tr[4]/td[1]/a/text()').extract_first()
        item['count3'] = response.xpath(
            '//*[@id="SpanPlanSchoolInfo"]/table[2]/tr[3]/td/table/tr[4]/td[2]/text()').extract_first()


        item['pici4'] = response.xpath(
            '//*[@id="SpanPlanSchoolInfo"]/table[2]/tr[3]/td/table/tr[5]/td[1]/a/text()').extract_first()
        item['count4'] = response.xpath(
            '//*[@id="SpanPlanSchoolInfo"]/table[2]/tr[3]/td/table/tr[5]/td[2]/text()').extract_first()


        item['pici5'] = response.xpath(
            '//*[@id="SpanPlanSchoolInfo"]/table[2]/tr[3]/td/table/tr[6]/td[1]/a/text()').extract_first()
        item['count5'] = response.xpath(
            '//*[@id="SpanPlanSchoolInfo"]/table[2]/tr[3]/td/table/tr[6]/td[2]/text()').extract_first()

        item['pici6'] = response.xpath(
            '//*[@id="SpanPlanSchoolInfo"]/table[2]/tr[3]/td/table/tr[7]/td[1]/a/text()').extract_first()
        item['count6'] = response.xpath(
            '//*[@id="SpanPlanSchoolInfo"]/table[2]/tr[3]/td/table/tr[7]/td[2]/text()').extract_first()

        item['pici7'] = response.xpath(
            '//*[@id="SpanPlanSchoolInfo"]/table[2]/tr[3]/td/table/tr[8]/td[1]/a/text()').extract_first()
        item['count7'] = response.xpath(
            '//*[@id="SpanPlanSchoolInfo"]/table[2]/tr[3]/td/table/tr[8]/td[2]/text()').extract_first()

        item['pici8'] = response.xpath(
            '//*[@id="SpanPlanSchoolInfo"]/table[2]/tr[3]/td/table/tr[9]/td[1]/a/text()').extract_first()
        item['count8'] = response.xpath(
            '//*[@id="SpanPlanSchoolInfo"]/table[2]/tr[3]/td/table/tr[9]/td[2]/text()').extract_first()

        #print(item.__str__())
        yield item
