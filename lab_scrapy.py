import scrapy

class lab_scrapy(scrapy.Spider):
    name="lab"
    headers = {

    }
    def start_requests(self):
        url = 'https://cs.fang.anjuke.com/loupan/all/'
        tag = getattr(self, 'tag', None)
        if tag is not None:
            url = url + 'tag/' + tag
        yield scrapy.Request(url, callback = self.parse, method='GET', headers={
            ':authority': 'cs.fang.anjuke.com',
            ':method': 'GET',
            ':path': '/loupan/all/',
            ':scheme': 'https',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
            'accept-encoding': 'gzip, deflate, br',
            'accept-language': 'zh-CN,zh;q=0.9',
            'cache-control': 'no-cache',
            'cookie': 'isp=true; isp=true; aQQ_ajkguid=93358DAA-72E0-DA62-BD38-823D4B927DFC; _ga=GA1.2.45587119.1563350501; _gid=GA1.2.645112654.1563350501; 58tj_uuid=d857c9b8-4349-40ff-bd70-4059f77bd2ac; als=0; isp=true; wmda_uuid=f384f07286790e59fceaac84c4ffb7df; wmda_new_uuid=1; wmda_visited_projects=%3B8788302075828; ctid=27; sessid=A72D8C99-4B4D-AFA0-75B0-B795555FF933; lps=http%3A%2F%2Fwww.anjuke.com%2F%3Fpi%3DPZ-baidu-pc-all-biaoti%7Chttps%3A%2F%2Fsp0.baidu.com%2F9q9JcDHa2gU2pMbgoY3K%2Fadrc.php%3Ft%3D06KL00c00f7WWws0cj7b00PpAsa54aqI00000KpAFdC00000v97o3C.THvs_oeHEtY0UWdBmy-bIfK15H64mhcYm103nj0snWD4nj60IHY1nYwjfW01PbNDPH9Af1KKrHfsrDf1nDmvP1fkfbczwfK95gTqFhdWpyfqn1cYnHb3nHmLnzusThqbpyfqnHm0uHdCIZwsT1CEQLILIz49UhGdpvR8mvqVQ1qspHdfyBdBmy-bIidsmzd9UAsVmh-9ULwG0APzm1Ykrj0v%26tpl%3Dtpl_11534_19968_16032%26l%3D1512539670%26attach%3Dlocation%253D%2526linkName%253D%2525E6%2525A0%252587%2525E5%252587%252586%2525E5%2525A4%2525B4%2525E9%252583%2525A8-%2525E6%2525A0%252587%2525E9%2525A2%252598-%2525E4%2525B8%2525BB%2525E6%2525A0%252587%2525E9%2525A2%252598%2526linkText%253D%2525E5%2525AE%252589%2525E5%2525B1%252585%2525E5%2525AE%2525A2-%2525E5%252585%2525A8%2525E6%252588%2525BF%2525E6%2525BA%252590%2525E7%2525BD%252591%2525EF%2525BC%25258C%2525E6%252596%2525B0%2525E6%252588%2525BF%252520%2525E4%2525BA%25258C%2525E6%252589%25258B%2525E6%252588%2525BF%252520%2525E6%25258C%252591%2525E5%2525A5%2525BD%2525E6%252588%2525BF%2525E4%2525B8%25258A%2525E5%2525AE%252589%2525E5%2525B1%252585%2525E5%2525AE%2525A2%2525EF%2525BC%252581%2526xp%253Did%28%252522m3241981673_canvas%252522%29%25252FDIV%25255B1%25255D%25252FDIV%25255B1%25255D%25252FDIV%25255B1%25255D%25252FDIV%25255B1%25255D%25252FDIV%25255B1%25255D%25252FH2%25255B1%25255D%25252FA%25255B1%25255D%2526linkType%253D%2526checksum%253D100%26ie%3Dutf-8%26f%3D8%26tn%3Dbaidu%26wd%3D%25E5%25AE%2589%25E5%25B1%2585%25E5%25AE%25A2%26rqlang%3Dcn%26inputT%3D3534; twe=2; isp=true; Hm_lvt_c5899c8768ebee272710c9c5f365a6d8=1563352661,1563419795; ajk_member_captcha=fa2cc698fdb52705c27ef4472cd0dbbe; propertys=szq8lt-putq8e_ta0tvy-putq7f_; init_refer=; new_uv=4; wmda_session_id_8788302075828=1563432736130-e0e4141b-14ad-4068; new_session=0; __xsptplusUT_8=1; __xsptplus8=8.12.1563434490.1563436547.10%232%7Csp0.baidu.com%7C%7C%7C%25E5%25AE%2589%25E5%25B1%2585%25E5%25AE%25A2%7C%23%23japWkeFuTrceNFF-GLflYAiKGnDT-Vai%23; Hm_lpvt_c5899c8768ebee272710c9c5f365a6d8=1563436548',
            'pragma': 'no-cache',
            'upgrade-insecure-requests': '1',
            'referer': 'https://cs.fang.anjuke.com/loupan/all/p2/',
            'user-agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.109 Safari/537.36'
        })

    def parse(self, response):

        infos = response.css('div.item-mod')
        datas = []
        for info in infos:
            money = info.css('.infos .address .list-map::text').get()
            local = info.css('.favor-pos p span::text').get()
            datas.append({
                'money': money,
                'local': local
            })
            filename = 'cs-local-price.txt'
            with open(filename, 'w+') as f:
                f.write(local)
                f.write(' - ')
                f.write(money)
                f.write(' - \n')
                f.close()
        
        next_page = response.css('.list-page .pagination .next-page::attr(href)').get()
        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log('保存文件: %s' % filename)