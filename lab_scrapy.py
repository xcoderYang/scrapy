import scrapy

class lab_scrapy(scrapy.Spider):
    name="lab"
    
    def start_requests(self):
        url = 'https://cs.fang.anjuke.com/loupan/s?kw='
        tag = getattr(self, 'tag', None)
        if tag is not None:
            url = url + 'tag/' + tag
        yield scrapy.Request(url, self.parse)

    def parse(self, response):

        infos = response.css('div.item-mod')
        for info in infos:
            money = info.css('.favor-pos .price span::text').get()
            local = info.css('.infos .address .list-map::text').get()
            print('----------------')
            print(money)
            print(local)
            print('----------------')
        
        # for lab in labs:
        #     text = lab.css('.text::text').extract_first()
        #     tags = lab.css('.tags .tag::text').extract()
        #     tags = ','.join(tags)

        #     filename = '%s-语录.txt' % tags
        #     with open(filename, "a+") as f:
        #         f.write(text)
        #         f.write('\n')
        #         f.write('标签 :'+tags)
        #         f.write('\n----------\n')
        #         f.close()
        
        # next_page = response.css('li.next a::attr(href)').extract_first()
        # if next_page is not None:
        #     next_page = response.urljoin(next_page)
        #     yield scrapy.Request(next_page, callback=self.parse)
        # with open(filename, 'wb') as f:
        #     f.write(response.body)
        # self.log('保存文件: %s' % filename)