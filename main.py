

print("lista zakupów")
 
shopping_dict = { 
    "piekarnia": ['Chleb', 'Pączek', 'Bułki'], 
    "warzywniak": ['Marchew', 'Seler', 'Rukola']
}

for shop, list in shopping_dict.items():
    print(f"Idę do {shop.capitalize()} kupuje tu nstępujące rzeczy: {list}")
print(f"W sumie kupuje tu {sum([len(item) for item in shopping_dict.values()])} produktów")

print("Commit nr 2")