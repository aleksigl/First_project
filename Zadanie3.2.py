shopping_list = {
    "bakery" : ["bread", "buns", "donut"],
    "fruit&veg" : ["carrot", "celery", "arugula"]
}
for shop, products in shopping_list.items():
    print(f"I'm heading to {shop.title()}, I'm gonna get: {[product.title() for product in products]}.")
shopping_items = sum([
    len(shop) for shop in shopping_list.values()
])
print(f"In total, I'm getting {shopping_items} items.")
print("Anything else you need?")

to_do_list = {
    "bathroom" : ["laundry", "clean the mirror"],
    "kitchen" : ["dinner prep", "coffee machine descaling"]
}
print(to_do_list)
to_do_list["bathroom"].append("empty the bin")
print(to_do_list)

print()
rooms_list = ' and '.join(to_do_list.keys())
chores_list = []
for chores in to_do_list.values():
    chores_list.extend(chores)
print(f"{rooms_list.capitalize()} need to be taken care of by the end of the day. \nHere's a list of chores for Patryk Tokarz: {', '.join(chores_list)}.")
print(f"In total, Patryk is assigned to {len(chores_list)} chores. \nEnjoy your Sunday Patryk, sending my greetings!")