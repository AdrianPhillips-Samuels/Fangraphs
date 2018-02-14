from scrapy import Spider, Request
from Fangraphs.items import FangraphsItem


class FangraphsSpider(Spider):
	name = 'fangraphs_spider'
	allowed_urls = ['www.fangraphs.com','baseballsavant.mlb.com']
	start_urls = [
		'https://www.fangraphs.com/leaders.aspx?pos=all&stats=bat&lg=all&qual=30&type=1&season=2015&month=0&season1=2015&ind=0&team=0&rost=0&age=0&filter=&players=0&page=1_850',
		'https://www.fangraphs.com/leaders.aspx?pos=all&stats=bat&lg=all&qual=30&type=1&season=2016&month=0&season1=2016&ind=0&team=0&rost=0&age=0&filter=&players=0&page=1_850',
		'https://www.fangraphs.com/leaders.aspx?pos=all&stats=bat&lg=all&qual=30&type=1&season=2017&month=0&season1=2017&ind=0&team=0&rost=0&age=0&filter=&players=0&page=1_850'
			]

	def parse(self, response):
		Year = response.xpath('//*[@id="content"]/table[1]/tr/td[1]/table[7]/tr/td/center/text()[last()]').extract_first().split("between ")[1][0:4]
		rows = response.xpath('//*[@id="LeaderBoard1_dg1_ctl00"]//tr[@class="rgRow"]')
		for row in rows:
			Name = row.xpath('./td[2]/a/text()').extract_first()
			Team = row.xpath('./td[3]/a/text()').extract_first()
			PA = row.xpath('./td[4]/text()').extract_first()
			BBp = row.xpath('./td[5]/text()').extract_first()
			Kp = row.xpath('./td[6]/text()').extract_first()
			BBtoK = row.xpath('./td[7]/text()').extract_first()
			AVG = row.xpath('./td[8]/text()').extract_first()
			OBP = row.xpath('./td[9]/text()').extract_first()
			SLG = row.xpath('./td[10]/text()').extract_first()
			OPS = row.xpath('./td[11]/text()').extract_first()
			ISO = row.xpath('./td[12]/text()').extract_first()
			Spd = row.xpath('./td[13]/text()').extract_first()
			BABIP = row.xpath('./td[14]/text()').extract_first()
			UBR = row.xpath('./td[15]/text()').extract_first()
			wGDP = row.xpath('./td[16]/text()').extract_first()
			wSB = row.xpath('./td[17]/text()').extract_first()
			wRC = row.xpath('./td[18]/text()').extract_first()
			wRAA = row.xpath('./td[19]/text()').extract_first()
			wOBA = row.xpath('./td[20]/text()').extract_first()
			wRCpl = row.xpath('./td[21]/text()').extract_first()


			item = FangraphsItem()
				
			item['Name'] = Name
			item['Year'] = Year
			item['Team'] = Team
			item['PA'] = PA
			item['BBp'] = BBp
			item['Kp'] = Kp
			item['BBtoK'] = BBtoK
			item['AVG'] = AVG
			item['OBP'] = OBP
			item['SLG'] = SLG
			item['OPS'] = OPS
			item['ISO'] = ISO
			item['Spd'] = Spd
			item['BABIP'] = BABIP
			item['UBR'] = UBR
			item['wGDP'] = wGDP
			item['wSB'] = wSB
			item['wRC'] = wRC
			item['wRAA'] = wRAA
			item['wOBA'] = wOBA
			item['wRCpl'] = wRCpl

			yield Request(response.url.split(sep='type=1')[0] + 'type=2' + response.url.split(sep='type=1')[1], callback=self.parse_batted, meta={'item': item, 'Name': Name, 'Year': Year}, dont_filter=True)


	def parse_batted(self, response):
		item = response.meta['item']
		Name = response.meta['Name']
		Year = response.meta['Year']
		row = response.xpath('//*[@id="LeaderBoard1_dg1_ctl00"]//tr[@class="rgRow"][td[2]/a/text() = "' + Name + '"]')

		GBtoFB = row.xpath('./td[5]/text()').extract_first()
		LDp = row.xpath('./td[6]/text()').extract_first()
		GBp = row.xpath('./td[7]/text()').extract_first()
		FBp = row.xpath('./td[8]/text()').extract_first()
		IFFBp = row.xpath('./td[9]/text()').extract_first()
		HRtoFB = row.xpath('./td[10]/text()').extract_first()
		IFH = row.xpath('./td[11]/text()').extract_first()
		IFHp = row.xpath('./td[12]/text()').extract_first()
		Pullp = row.xpath('./td[15]/text()').extract_first()
		Centp = row.xpath('./td[16]/text()').extract_first()
		Oppop = row.xpath('./td[17]/text()').extract_first()
		Softp = row.xpath('./td[18]/text()').extract_first()
		Medp = row.xpath('./td[19]/text()').extract_first()
		Hardp = row.xpath('./td[20]/text()').extract_first()


		item['GBtoFB'] = GBtoFB
		item['LDp'] = LDp
		item['GBp'] = GBp
		item['FBp'] = FBp
		item['IFFBp'] = IFFBp
		item['HRtoFB'] = HRtoFB
		item['IFH'] = IFH
		item['IFHp'] = IFHp
		item['Pullp'] = Pullp
		item['Centp'] = Centp
		item['Oppop'] = Oppop
		item['Softp'] = Softp
		item['Medp'] = Medp
		item['Hardp'] = Hardp

		yield Request('https://baseballsavant.mlb.com/statcast_search?hfPT=&hfAB=&hfBBT=fly%5C.%5C.ball%7Cline%5C.%5C.drive%7C&hfPR=&hfZ=&stadium=&hfBBL=&hfNewZones=&hfGT=R%7C&hfC=&hfSea=' + Year + '%7C&hfSit=&player_type=batter&hfOuts=&opponent=&pitcher_throws=&batter_stands=&hfSA=&game_date_gt=&game_date_lt=&team=&position=&hfRO=&home_road=&hfFlag=&metric_1=h_launch_speed&metric_1_gt=0&metric_1_lt=&hfInn=&min_pitches=0&min_results=0&group_by=name&sort_col=launch_speed&player_event_sort=h_launch_speed&sort_order=desc&min_abs=30#results', 
					callback=self.parse_velo, meta={'item': item, 'Name': Name, 'Year': Year},
					dont_filter=True)


	def parse_velo(self, response):
		item = response.meta['item']
		Name = response.meta['Name']
		row = response.xpath('//*[@id="search_results"]//tr[td[@class="player_name"][text() = "' + Name + '"]]')
		Velo = row.xpath('./td[4]/text()').extract_first().strip().replace(' MPH', '')
		item['XVelo'] = Velo
		yield item

