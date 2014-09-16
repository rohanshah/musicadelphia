#! /usr/bin/env python
from scrapers.UnionTransferScraper import UnionTransferScraper
from scrapers.MilkBoyScraper import MilkBoyScraper
from scrapers.BootAndSaddleScraper import BootAndSaddleScraper
from scrapers.ElectricFactoryScraper import ElectricFactoryScraper
import json

unionTransfer = UnionTransferScraper()
milkBoy = MilkBoyScraper()
bootAndSaddle = BootAndSaddleScraper()
electricFactory = ElectricFactoryScraper()
scrapers = [unionTransfer, milkBoy, bootAndSaddle, electricFactory]
allEvents = []

for scraper in scrapers:
	soup = scraper.makeSoup()
	events = scraper.getEvents(soup)
	allEvents = allEvents + events

encoder = json.JSONEncoder()
output = encoder.encode(allEvents)
file = open("events.json", 'w')
file.write(output)
