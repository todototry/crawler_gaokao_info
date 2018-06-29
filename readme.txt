注意Item 提取的时候， 如果使用 chrome 的 inspect 功能中的 xpath ，要特别注意 chrome 会自动给 table 加上 tbody， 导致 用它生成的xpath 无法提取到需要的数据。

# 自动爬取，并输出
scrapy crawl myspider -o result.csv

# 测试 parse 逻辑
scrapy parse "http://www.heao.gov.cn/JHCX/PZ/enrollplan/PCList.aspx?YXDH=0001" -c parse_item

# 交互式分析
scrapy shell "http://www.heao.gov.cn/JHCX/PZ/enrollplan/PCList.aspx?YXDH=0001"

# 查看爬取结果
scrapy view "http://www.heao.gov.cn/JHCX/PZ/enrollplan/PCList.aspx?YXDH=0001"

