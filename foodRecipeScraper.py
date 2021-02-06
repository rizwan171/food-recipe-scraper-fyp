from bs4 import BeautifulSoup

import os

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

# open the list of classes and read each line
foodClassesFile = open('classes.txt', 'r')
foodClassesList = foodClassesFile.readlines()

# note: first line in file is not a class
foodClassesList = foodClassesList[1 : len(foodClassesList)]
print("Number of food classes: " + str(len(foodClassesList)))

# cleaning up the class names
foodClassesListClean = []
for foodClass in foodClassesList:
    foodClass = foodClass.strip("\n")
    foodClass = foodClass.replace("_", "+")
    foodClassesListClean.append(foodClass)

# construct the search request for each class to obtain url's to the recipe pages
baseSearchUrl = "https://www.food.com/search/"
urlsToScrape = []

for foodClass in foodClassesListClean:
    urlsToScrape.append(baseSearchUrl + foodClass)


# define a function to scrape the website for url's to the recipes
def scrapeUrlForRecipeUrl(url):
    # set the driver to run in headless mode
    options = Options()
    options.headless = True
    options.add_argument("log-level=2")

    # get web driver location
    driverLocation = os.getcwd() + "\\chromedriver.exe"

    # initialise webdriver
    # driver = webdriver.Chrome(options=optionsForDriver, executable_path=driverLocation)
    driver = webdriver.Chrome(options=options, executable_path=driverLocation)

    # load the URL passed and wait for the elements to load
    driver.get(url)
    WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.ID, "searchModuleTitle")))

    # get the source data of page
    pageSource = driver.page_source
    htmlData = BeautifulSoup(pageSource, features="lxml")

    # get all links on the page
    allLinks = htmlData.find_all("a")

    # find the links relating to the recipe and save them
    recipeLinks = []
    for link in allLinks:
        href = link.attrs["href"]
        if href.startswith("https://www.food.com/recipe/") and href not in recipeLinks:
            recipeLinks.append(href)

    recipeLinks.append("==========")

    # close the browser
    driver.quit()

    return recipeLinks

# scrape recipe links for all the food classes
recipeLinks = []
for url in urlsToScrape:
    print("Finding recipes on " + str(url))
    links = scrapeUrlForRecipeUrl(url)
    recipeLinks.extend(links)

# write the links to a file
f = open("recipeLinks.txt", "a")
for link in recipeLinks:
    f.write(link + "\n")

f.close()