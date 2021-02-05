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

# from bs4 import BeautifulSoup
# import requests

# urlsToScrape

# from recipe_scrapers import scrape_me

# scrapedData = scrape_me("https://www.food.com/recipe/kittencals-italian-melt-in-your-mouth-meatballs-69173")

# print(scrapedData.title())
# # print(scrapedData.author())
# for ing in scrapedData.ingredients():
#     print(ing)

# print(scrapedData.instructions())
# print(scrapedData.yields())
# print(scrapedData.total_time())
# print(scrapedData.image())
# print(scrapedData.ratings())