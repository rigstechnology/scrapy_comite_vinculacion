# -*- coding: utf-8 -*-
import scrapy
from comite_evaluacion.items import ComiteEvaluacionItem

class BotCeSpider(scrapy.Spider):
    name = "bot_ce"
    allowed_domains = ["comitedevinculacion.com.mx"]
    start_urls = ['http://comitedevinculacion.com.mx/directorio.php']

    def parse(self, response):
        ## Extract table rows from useful data
        for individual_row in response.xpath('//table[contains(@class,"datagrid")]//tr'):
            person_name = individual_row.xpath('./td[1]/text()').extract_first()

            if person_name is None:
                    continue

            person_name = person_name.strip().lower()
            company     = individual_row.xpath('./td[2]/text()').extract_first().strip().lower()
            position    = individual_row.xpath('./td[3]/text()').extract_first().strip().lower()
            phone       = individual_row.xpath('./td[4]/text()').extract_first().strip().lower()
            email       = individual_row.xpath('./td[5]/text()').extract_first().strip().lower()

            ## Send the data to item
            item             = ComiteEvaluacionItem()
            item['name']     = person_name
            item['company']  = company
            item['position'] = position
            item['phone']    = phone
            item['email']    = email

            yield item
        ## End for loop line row

        ## Check if we iterate a next page
        url_next_page = response.xpath('//div[contains(@id, "paginador")]/p[last()]/a/@href').extract_first()

        if url_next_page:
            full_next_page = response.urljoin(url_next_page)
            yield scrapy.Request(full_next_page, callback=self.parse)
        ## End url_next_page
    ## End parse