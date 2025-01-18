shopping_list = {
    "bakery" : ["bread", "buns", "donut"],
    "fruit&veg" : ["carrot", "celery", "arugula"]
}
for shop, products in shopping_list.items():
    print(f"I'm heading to {shop}, I'm gonna get: {products}.")