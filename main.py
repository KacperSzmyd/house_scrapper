from HouseScrapper import HouseScrapper
from bs4 import BeautifulSoup

hs = HouseScrapper("Sanok")
hs.get_houses()
hs.apply_filters()
  