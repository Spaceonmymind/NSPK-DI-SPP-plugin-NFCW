from selenium import webdriver

from logging import config
config.fileConfig('dev.logger.conf')
from NFCW import Nfcw

driver = webdriver.Chrome()

parser = Nfcw(driver)
docs = parser.content()


print(*docs, sep='\n\r\n')