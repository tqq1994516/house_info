# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import attr


@attr.s
class HouseInfoItem:
    title = attr.ib()  # 标题
    subhead = attr.ib()  # 副标题
    totalPrices = attr.ib()  # 总价
    unitPrice = attr.ib()  # 单价
    acreage = attr.ib()  # 面积
    houseDoorModel = attr.ib()  # 房屋户型
    floor = attr.ib()  # 所在楼层
    familyStructure = attr.ib()  # 户型结构
    insideSpace = attr.ib()  # 套内面积
    buildingTypes = attr.ib()  # 建筑类型
    buildingStructure = attr.ib()  # 建筑结构
    buildingHead = attr.ib()  # 房屋朝向
    decorateSituation = attr.ib()  # 装修情况
    ladderHouseholdProportion = attr.ib()  # 梯户比例
    haveElevator = attr.ib()  # 是否用电梯
    propertyType = attr.ib()  # 产权类型
    usageOfHouse = attr.ib()  # 房屋用途
    propertyOwnership = attr.ib()  # 产权所属
    villageName = attr.ib()  # 小区名称
    area = attr.ib()  # 所在地区
    communityIsIntroduced = attr.ib()  # 小区介绍
    surroundingFacility = attr.ib()  # 周边配套
    transportation = attr.ib()  # 交通出现
    coreSellingPoint = attr.ib()  # 核心卖点
