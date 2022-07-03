from selenium import webdriver
PATH = "D:\ApplicationDownloads\chromedriver_win32\chromedriver.exe"

driver = webdriver.Chrome(PATH)

driver.get("https://www.mlb.com/stats/caught-stealing")

driver.quit()