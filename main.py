

print("lista zakupów")
 
shopping_dict = { 
    "piekarnia": ['Chleb', 'Pączek', 'Bułki'], 
    "warzywniak": ['Marchew', 'Seler', 'Rukola']
}

for shop, list in shopping_dict.items():
    print(f"Idę do {shop.capitalize()} kupuje tu nstępujące rzeczy: {list}")

