import enum
from recipe_scrapers import scrape_me
import json

# open the file and get each link
linksFile = open('recipeLinksFiltered.txt', 'r')
linksData = linksFile.readlines()

# remove \n from end of each link
recipeLinks = []
for link in linksData:
    link = link.strip("\n")
    recipeLinks.append(link)

# open the list of classes and read each line
foodClassesFile = open('classes.txt', 'r')
foodClassesList = foodClassesFile.readlines()

# note: first line in file is not a class
foodClassesList = foodClassesList[1 : len(foodClassesList)]

# cleaning up the class names
foodClassesListClean = []
for foodClass in foodClassesList:
    foodClass = foodClass.strip("\n")
    foodClass = foodClass.replace("_", " ")
    foodClass = foodClass.title()
    foodClassesListClean.append(foodClass)

# json object that will contain recipe info
recipeDataJSON = {}

jsonFile = open("recipe_data.json", "a")

# for each link, scrape the recipe data and insert it into the json object
for index, link in enumerate(recipeLinks):
    scrapedData = scrape_me(link)

    recipeDataJSON["title"] = foodClassesListClean[index]
    recipeDataJSON["instructions"] = scrapedData.instructions()
    recipeDataJSON["ingredients"] = scrapedData.ingredients()
    recipeDataJSON["yields"] = scrapedData.yields()
    recipeDataJSON["total_time"] = scrapedData.total_time()
    recipeDataJSON["img"] = scrapedData.image()
    
    json.dump(recipeDataJSON, jsonFile)
    jsonFile.write(",")

jsonFile.close()