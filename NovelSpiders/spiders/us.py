# _*_coding:utf-8_*_
import scrapy
from NovelSpiders.items import NovelsItem
from NovelSpiders.items import ChaptersItem


class UsSprider(scrapy.Spider):
    name = "23us"
    allowed_domains = ["23us.so"]
    start_urls = [
        "http://www.23us.so/list/1_1.html",
        "http://www.23us.so/list/2_1.html",
        "http://www.23us.so/list/3_1.html",
        "http://www.23us.so/list/4_1.html",
        "http://www.23us.so/list/5_1.html",
        "http://www.23us.so/list/6_1.html",
        "http://www.23us.so/list/7_1.html",
        "http://www.23us.so/list/8_1.html",
        "http://www.23us.so/list/9_1.html",
        "http://www.23us.so/full.html",
    ]

    def parse(self, response):
        novel_link_list = response.selector.xpath('//td[@class="L"]/a[re:test(@href,".*/xiaoshuo/.*")]/@href').extract()
        for novel_link in novel_link_list:
            yield scrapy.Request(novel_link, callback=self.novel_page)

        next_page = response.xpath('//a[@class="next"]/@href').extract_first()
        if next_page:
            yield scrapy.Request(next_page, callback=self.parse)

    def novel_page(self, response):
        id = response.url.split('/')[-1].split('.')[0]
        title = response.xpath('//dl[@id="content"]/dd/h1/text()').extract_first().split(' ')[0]
        table_td = response.xpath('//tr/td')
        type = table_td[0].xpath('a/text()').extract_first().split(u' ')[-1]
        author = table_td[1].xpath('text()').extract_first().split(u' ')[-1]
        status = table_td[2].xpath('text()').extract_first().split(u' ')[-1]
        length = table_td[4].xpath('text()').extract_first().split(u'字')[0].split(u' ')[-1]
        last_update = table_td[5].xpath('text()').extract_first().split(u' ')[-1]
        background = response.xpath('//img[re:test(@src,".*/'+id+'/.*")]/@src').extract_first()
        content = response.xpath('//dd')[-1].xpath('p/text()').extract()[0]
        yield NovelsItem(
            id=id,
            title=title,
            type=type,
            author=author,
            status=status,
            length=length,
            last_update=last_update,
            background=background,
            content=content
        )

        chapter_url = response.xpath('//a[@class="read"]/@href').extract_first()
        yield scrapy.Request(chapter_url, callback=self.chapter_page)

    def chapter_page(self, response):
        chapters_list = response.xpath('//tr/td[@class="L"]/a/@href').extract()
        for chapter in chapters_list:
            yield scrapy.Request(chapter, callback=self.content_page)

    def content_page(self, response):
        id = response.url.split('/')[-1].split('.')[0]
        novel_id = response.url.split('/')[-2]
        name = response.xpath('//dl/dd/h1/text()').extract_first()
        content = response.xpath('//dd[@id="contents"]').extract_first().split('id="contents">')[-1].split('</dd>')[0]
        yield ChaptersItem(
            id=id,
            novel_id=novel_id,
            name=name,
            content=content
        )



