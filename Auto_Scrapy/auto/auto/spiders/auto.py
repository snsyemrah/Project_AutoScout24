from traceback import print_exception
from urllib.parse import urljoin
import scrapy
import psycopg2



class SdSpider(scrapy.Spider):
    name = 'auto'
    # allowed_domains = ['https://www.autoscout24.nl/']
    start_urls = ['https://www.autoscout24.nl/lst/bmw?sort=standard&desc=0&ustate=N,U&atype=C&cy=NL&fregfrom=2018',
                  'https://www.autoscout24.nl/lst/mercedes-benz?sort=standard&desc=0&ustate=N,U&atype=C&cy=NL&fregfrom=2018',
                  'https://www.autoscout24.nl/lst/toyota?sort=standard&desc=0&ustate=N,U&atype=C&cy=NL&fregfrom=2018']

    def parse(self, response):

        hrefs = response.xpath('//*[@class="cldt-summary-full-item listing-impressions-tracking list-page-item ListItem_article__ppamD"]')
       
        
        
        for href in hrefs:
            ek = href.css('a ::attr(href)').get()
            new_url = response.urljoin(ek)
            yield scrapy.Request(new_url,callback=self.detail)

        # # next = response.xpath('//*[@id="__next"]/div/div/div[4]/div[3]/main/div[16]/nav/ul/li[5]/a/@href')
        # next = response.css('li.prev-next a ::attr(href)').get()
        # print(next)
        # # sayac = 1
        # if next:
            
        #     url = response.urljoin(next)
        #     print("/*/*/*/*-/*-/*-/*-/*-/*-/*/*/*/*/*/*/*/*/*")
        #     print(url)
        #     yield scrapy.Request(url,callback=self.parse)

        next = "https://www.autoscout24.nl/lst/toyota?sort=standard&desc=0&ustate=N%2CU&atype=C&cy=NL&fregfrom=2018&search_id=6oaf5q9nlw&page={x}"
        for page in range(2,21):
            url = next.format(x=page)
            print(url)

            yield scrapy.Request(url,callback=self.parse)
        next = "https://www.autoscout24.nl/lst/bmw?sort=standard&desc=0&ustate=N%2CU&atype=C&cy=NL&fregfrom=2018&search_id=1ysl1kxp6ll&page={x}"
        for page in range(2,21):
            url = next.format(x=page)
            print(url)

            yield scrapy.Request(url,callback=self.parse)
            
        next = "https://www.autoscout24.nl/lst/mercedes-benz?sort=standard&desc=0&ustate=N%2CU&atype=C&cy=NL&fregfrom=2018&search_id=1agykg8x1k7&page={x}"
        for page in range(2,21):
            url = next.format(x=page)
            print(url)

            yield scrapy.Request(url,callback=self.parse)



    def detail(self,response):
        Model1 = response.xpath('///*[@id="__next"]/div/div/main/div[5]/div[2]/div[1]/div[2]/h1/div[1]/span[1]/text()').get()
        Model2 = response.xpath('//*[@id="__next"]/div/div/main/div[5]/div[2]/div[1]/div[2]/h1/div[2]/text()').get()
        Model = Model1 + Model2

        # x = Model.replace("|","").replace("*","").replace("-","").replace("!","").replace("+","").replace("[","").replace(".","").replace(" ","_")
        
        # Mercedes-Benz C | Designo iridium mat | Achterasbesturing | Dist

        Plate = response.xpath('//*[@id="__next"]/div/div/main/div[6]/div[3]/div/div[2]/div/dl/dd[6]/text()').get()
        if Plate ==None:
            Plate="Geen Kenteken"         
        print("Plaka----------  ",Plate)

        Year = response.xpath('//*[@id="__next"]/div/div/main/div[5]/div[3]/div[2]/div[3]/div[4]/text()').get()
        Kilometer = response.xpath('//*[@id="__next"]/div/div/main/div[5]/div[3]/div[2]/div[1]/div[4]/text()').get().split(' ')[0]

        Price = response.xpath('//*[@id="__next"]/div/div/main/div[5]/div[2]/div[3]/div[1]/div/div/div[1]/div[1]/span/text()').get().split(' ')[1].split(',')[0]
        City = response.xpath('//*[@id="__next"]/div/div/main/div[5]/div[2]/a/text()').get().split(',')[0]
        Image = response.xpath('//*[@id="__next"]/div/div/main/div[5]/div[1]/div/div/div[1]/div[1]/div/div[1]/picture/img/@src').get()
        if Image ==None:
            Image="Geen Image"
        yield{"Model: ":x,"Kilometer: ":Kilometer,"City: ":City,"Year: ":Year,"Price: ":Price,"Plate: ":Plate,"Image: ":Image}

  




        
       
     
        

       
