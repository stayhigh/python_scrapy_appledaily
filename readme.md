Python Scrapy for crawling apple daily news
=============================================

Why this project?
--------------------

Inspired by LargitData (http://largitdata.com/course_list/11)

- [[Scrapy 爬蟲] 如何使用items.py整理Scrapy 爬取下來的資料並輸出成JSON檔?](https://www.youtube.com/watch?v=w4PPlkJFzCo)
- [[Scrapy 爬蟲] 如何從蘋果新聞的清單聯結抓取下一層的內容頁面?](https://www.youtube.com/watch?v=Me9SpR0SE08)
- [[Scrapy 爬蟲] 如何使用pipelines.py將Scrapy 爬取下來的資料儲存置資料庫之中?](https://www.youtube.com/watch?v=Xq4yRuePSdk)
- [[Scrapy 爬蟲] 如何使用Scrapy 的CrawlSpider 實現多網頁爬取?](https://www.youtube.com/watch?v=KSA12AKDr_o)
- [[Scrapy 爬蟲] 如何設置 Job 以分段爬蟲任務?](https://www.youtube.com/watch?v=2xjAArPnOH8)

Tools for this project
---------------------------

~~~
- 安裝google chrome plugin，SelectorGadget
快速取得selector與xpath等相關資訊，網頁爬蟲特別實用

- 安裝firefox plugin，sqlite manager
觀看資料庫內容：http://www.minwt.com/website/server/4964.html
~~~

How it works?
---------------------------

### 開啟apple新的scrapy專案 ###
~~~bash
stayhigh@stayhighnet:/Users/stayhigh/projects/apple  $  scrapy startproject apple
~~~

### 執行apple的scrapy專案 ###

~~~shell
stayhigh@stayhighnet:/Users/stayhigh/projects/apple  $  scrapy crawl apple
~~~

### 執行apple的scrap專案，並且將輸出a.json的json格式檔案 ###

~~~shell
stayhigh@stayhighnet:/Users/stayhigh/projects/apple  $  scrapy crawl apple -o a.json -t json
~~~

### 執行分段爬蟲任務並放置相關資料於job1目錄 ###

~~~shell
stayhigh@stayhighnet:/Users/stayhigh/projects/apple  $  scrapy crawl apple -s JOBDIR=job1
~~~

觀看apple專案目錄結構
-----------------------

- crawler.py為使用者自行定義的爬蟲程式，藉由繼承scrapy.Spider類別進行網頁抓取
- items.py 用於定義資料欄位
- pipeline.py 用於定義爬蟲程式的控制流程
- settings.py 設定檔，用於設定啟用的功能，如常見的pipeline功能，並切記設定時指定pipeline.py當中的apple.pipelines.ApplePipeline

~~~python
ITEM_PIPELINES = {
    'apple.pipelines.ApplePipeline': 300,
}
~~~

~~~shell
stayhigh@stayhighnet:/Users/stayhigh/projects/apple  $ tree
.
├── a.json
├── apple
│   ├── __init__.py
│   ├── __init__.pyc
│   ├── items.py
│   ├── items.pyc
│   ├── pipelines.py
│   ├── settings.py
│   ├── settings.pyc
│   └── spiders
│       ├── __init__.py
│       ├── __init__.pyc
│       ├── crawler.py
│       └── crawler.pyc
└── scrapy.cfg
~~~

###如何實現多網頁爬取功能###
~~~python
from scrapy.spiders import CrawlSpider
~~~
###crawler.py內的爬蟲類別繼承CrawlSpider###
~~~python
class AppleCrawler(CrawlSpider):
~~~

Syntax for MarkDown (readme.rd)
------------------------------

https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet#links
