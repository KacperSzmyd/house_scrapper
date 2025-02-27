import sys
from HouseScrapper import HouseScrapper

sys.stdout.reconfigure(encoding="utf-8")

hs = HouseScrapper("Sanok")
hs.get_houses()
hs.apply_filters()

houses_data = hs.get_house_tiles()
