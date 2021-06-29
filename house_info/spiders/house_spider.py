import scrapy

from house_info.items import HouseInfoItem


class HouseInfoSpider(scrapy.Spider):
    name = 'house_info_spider'
    allowed_domains = ['lianjia.com']
    start_urls = [
        "https://nj.lianjia.com/ershoufang/103114492335.html",
    ]

    def parse(self, response, **kwargs):
        title = response.xpath('/html/body/div[3]/div/div/div[1]/h1/text()').get()
        title = title.strip()
        subhead = response.xpath('/html/body/div[3]/div/div/div[1]/div/text()').get()
        subhead = subhead.strip()
        totalPrices = response.xpath('/html/body/div[5]/div[2]/div[3]/span[1]/text()').get()
        totalPrices = totalPrices.strip()
        unitPrice = response.xpath('/html/body/div[5]/div[2]/div[3]/div[1]/div[1]/span/text()').get()
        unitPrice = unitPrice.strip()
        acreage = response.xpath('/html/body/div[5]/div[2]/div[4]/div[3]/div[1]/text()').get()
        acreage = acreage.strip()
        houseDoorModel = response.xpath('/html/body/div[7]/div[1]/div[1]/div/div/div[1]/div[2]/ul/li[1]/text()').get()
        houseDoorModel = houseDoorModel.strip()
        floor = response.xpath('/html/body/div[7]/div[1]/div[1]/div/div/div[1]/div[2]/ul/li[2]/text()').get()
        floor = floor.strip()
        familyStructure = response.xpath('/html/body/div[7]/div[1]/div[1]/div/div/div[1]/div[2]/ul/li[4]/text()').get()
        familyStructure = familyStructure.strip()
        insideSpace = response.xpath('/html/body/div[7]/div[1]/div[1]/div/div/div[1]/div[2]/ul/li[3]/text()').get()
        insideSpace = insideSpace.strip()
        buildingTypes = response.xpath('/html/body/div[7]/div[1]/div[1]/div/div/div[1]/div[2]/ul/li[5]/text()').get()
        buildingTypes = buildingTypes.strip()
        buildingStructure = response.xpath(
            '/html/body/div[7]/div[1]/div[1]/div/div/div[1]/div[2]/ul/li[7]/text()').get()
        buildingStructure = buildingStructure.strip()
        buildingHead = response.xpath('/html/body/div[7]/div[1]/div[1]/div/div/div[1]/div[2]/ul/li[6]/text()').get()
        buildingHead = buildingHead.strip()
        decorateSituation = response.xpath(
            '/html/body/div[7]/div[1]/div[1]/div/div/div[1]/div[2]/ul/li[8]/text()').get()
        decorateSituation = decorateSituation.strip()
        ladderHouseholdProportion = response.xpath(
            '/html/body/div[7]/div[1]/div[1]/div/div/div[1]/div[2]/ul/li[9]/text()').get()
        ladderHouseholdProportion = ladderHouseholdProportion.strip()
        haveElevator = response.xpath('/html/body/div[7]/div[1]/div[1]/div/div/div[1]/div[2]/ul/li[10]/text()').get()
        haveElevator = haveElevator.strip()
        propertyType = response.xpath(
            '/html/body/div[7]/div[1]/div[1]/div/div/div[2]/div[2]/ul/li[4]/span[2]/text()').get()
        propertyType = propertyType.replace('/n', '').strip()
        usageOfHouse = response.xpath(
            '/html/body/div[7]/div[1]/div[1]/div/div/div[2]/div[2]/ul/li[6]/span[2]/text()').get()
        usageOfHouse = usageOfHouse.replace('/n', '').strip()
        propertyOwnership = response.xpath(
            '/html/body/div[7]/div[1]/div[1]/div/div/div[2]/div[2]/ul/li[6]/span[2]/text()').get()
        propertyOwnership = propertyOwnership.replace('/n', '').strip()
        villageName = response.xpath('/html/body/div[5]/div[2]/div[5]/div[1]/a[1]/text()').get()
        villageName = villageName.replace('/n', '').strip()
        area = response.xpath(
            '/html/body/div[5]/div[2]/div[5]/div[2]/span[2]/a[1]/text()').get() + ' ' + response.xpath(
            '/html/body/div[5]/div[2]/div[5]/div[2]/span[2]/a[2]/text()').get() + ' ' + response.xpath(
            '/html/body/div[5]/div[2]/div[5]/div[2]/span[2]/text()[2]').get()
        area = area.replace('/n', '').replace('&nbsp;', '').strip()
        communityIsIntroduced = response.xpath('/html/body/div[7]/div[1]/div[2]/div/div[3]/div[2]/text()').get()
        communityIsIntroduced = communityIsIntroduced.replace('/n', '').strip()
        surroundingFacility = response.xpath('/html/body/div[7]/div[1]/div[2]/div/div[4]/div[2]/text()').get()
        surroundingFacility = surroundingFacility.replace('/n', '').strip()
        transportation = response.xpath('/html/body/div[7]/div[1]/div[2]/div/div[5]/div[2]/text()').get()
        transportation = transportation.replace('/n', '').strip()
        coreSellingPoint = response.xpath('/html/body/div[7]/div[1]/div[2]/div/div[2]/div[2]/text()').get()
        coreSellingPoint = coreSellingPoint.replace('/n', '').strip()
        yield HouseInfoItem(title, subhead, totalPrices, unitPrice, acreage, houseDoorModel, floor, familyStructure,
                            insideSpace, buildingTypes, buildingStructure, buildingHead, decorateSituation,
                            ladderHouseholdProportion, haveElevator, propertyType, usageOfHouse, propertyOwnership,
                            villageName, area, communityIsIntroduced, surroundingFacility, transportation,
                            coreSellingPoint)
