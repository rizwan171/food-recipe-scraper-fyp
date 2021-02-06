from recipe_scrapers import scrape_me

# TODO Testing with one link
scrapedData = scrape_me("https://www.food.com/recipe/kittencals-italian-melt-in-your-mouth-meatballs-69173")

print(scrapedData.title())
# print(scrapedData.author()) this info may not be needed
for ing in scrapedData.ingredients():
    print(ing)

print(scrapedData.instructions())
print(scrapedData.yields())
print(scrapedData.total_time())
print(scrapedData.image())
print(scrapedData.ratings())