count_chicken_menu = int(input())
count_fish_menu = int(input())
count_vegan_menu = int(input())
chicken_menu_price = 10.35
fish_menu_price = 12.40
vegan_menu_price = 8.15
whole_menu_price_without_desert = count_chicken_menu * chicken_menu_price \
                                  + count_fish_menu * fish_menu_price \
                                  + count_vegan_menu * vegan_menu_price
desert_price = 0.2 * whole_menu_price_without_desert
delivery_price = 2.5
total_price = whole_menu_price_without_desert + desert_price + delivery_price

print(total_price)
