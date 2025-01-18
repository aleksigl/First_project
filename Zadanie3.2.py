shopping_list = {
    "bakery" : ["bread", "buns", "donut"],
    "fruit&veg" : ["carrot", "celery", "arugula"]
}
for shop, products in shopping_list.items():
    print(f"I'm heading to {shop.title()}, I'm gonna get: {[product.title() for product in products]}.")