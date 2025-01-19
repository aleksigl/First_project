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
