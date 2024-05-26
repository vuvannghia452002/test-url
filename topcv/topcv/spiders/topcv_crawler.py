import scrapy


class TopcvCrawlerSpider(scrapy.Spider):
    name = "topcv-crawler"
    allowed_domains = ["www.topcv.vn"]
    start_urls = ["https://www.topcv.vn/tim-viec-lam-moi-nhat"]

    def parse(self, response):











        
        jobs = response.xpath("//div[contains(@class,'job-ta')]")

        for job in jobs:
            job_url = job.xpath(".//h3[contains(@class,'title')]//@href").get()

            yield{
                "job_url":job_url
            }
