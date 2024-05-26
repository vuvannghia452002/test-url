import scrapy


class TopcvCrawlerSpider(scrapy.Spider):
    name = "topcv-crawler"
    allowed_domains = ["www.topcv.vn"]
    start_urls = ["https://www.topcv.vn/tim-viec-lam-moi-nhat"]

    def parse(self, response):
        pass
