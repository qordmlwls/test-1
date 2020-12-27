import scrapy


class DmozSpider(scrapy.Spider):##상속 전체 페이지 크롤링
    name = "dmoz"
    allowed_domains =["dmoz.org"]
    start_urls = [
        'http://www.dmoz.org/Computers/Programming/Languages/Python/Books/',
        'http://www.dmoz.org/Computers/Programming/Languages/Python/Resources/',
    ]

    def parse(self, response):
        page = response.url.split("/")[-2]
        filename='dmoz-%s.html' % page
        with open(filename, 'wb') as f:
            f.write(response.body)

"""title 출력 ur
    def parse(self, response):
        for sel in response.xpath('//ul/li'): ##tag
            title = sel.xpath('a/text()').extract()
            link = sel.xpath('a/@href').extract()
            desc = sel.xpath('text()').extract()
            prin(title,link, desc)"""