days = int(input())
available_food = float(input())

biscuits_total = 0
total_food = 0
dog_total_food = 0
cat_total_food = 0

for i in range (1, days + 1):
    dog_food = int(input())
    cat_food = int(input())
    daily_food = dog_food + cat_food
    total_food = total_food + daily_food
    dog_total_food += dog_food
    cat_total_food += cat_food
    if i % 3 == 0:
        biscuits_total = biscuits_total + (0.10 *daily_food)


print(f"Total eaten biscuits: {round(biscuits_total)}gr.")
percent_total = total_food / available_food * 100
print(f"{percent_total:.2f}% of the food has been eaten.")
percent_total_dog = dog_total_food / total_food * 100
print(f"{percent_total_dog}% eaten from the dog.")
percent_total_cat = cat_total_food / total_food * 100
print(f"{percent_total_cat}% eaten from the cat.")
