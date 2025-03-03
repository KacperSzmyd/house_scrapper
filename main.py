import sys
from HouseScrapper import HouseScrapper
from DataManager import HouseDataManager

sys.stdout.reconfigure(encoding="utf-8")

hs = HouseScrapper("Tarnow")
hs.get_houses()
hs.apply_filters(min_price=1000000, max_price=1400000)

houses_data = hs.get_house_tiles()

for offer, data in houses_data.items():
    house_dm = HouseDataManager(
        price=data["price"],
        area=data["area"],
        ppm2=data["price per m2"],
        link=data["url"],
    )
    house_dm.pass_to_form()
    house_dm.quit()
