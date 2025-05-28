inventory = [
    # name,       category,   unit_price, units_sold, units_left
    ["Strawberry", "Fruit",      3.50,        40,          10],
    ["Broccoli",   "Vegetable",  2.20,        25,           8],
    ["Cheddar",    "Dairy",      5.00,        18,           4],
    ["Baguette",   "Bakery",     2.80,        35,           2],
    ["Blueberry",  "Fruit",      4.00,        22,           6],
    ["Spinach",    "Vegetable",  1.80,        30,          12],
    ["Yogurt",     "Dairy",      1.20,        50,          15],
    ["Croissant",  "Bakery",     3.00,        28,           3],
]
revenue=0
for row in inventory:
    revenue+= row[2]*row[3]
print(revenue)

for row in inventory:
    if row[4]<5:
        print(row[0])


categories=[]
revenues=[]

for row in inventory:
    category = row[1]
    revenue=row[2]*row[3]

    found=False
    for i in range(len(categories)):
        if categories[i]==category:
            revenues[i]+=revenue
            found=True
            break
    if not found:
        categories.append(category)
        revenues.append(revenue)
print("Category-Wisr Revenue:")
for i in range(len(categories)):
    print(f"{categories[i]} : {revenues[i]}")
    
