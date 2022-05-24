paper_price = int(input())
count_plat = int(input())
count_glue = float(input())
percent_discount = int(input())

price_paper = 5.80
price_plat = 7.20
glue = 1.20

total_paper = paper_price * price_paper
total_plat = price_plat * count_plat
total_glue = count_glue * glue


price = total_paper + total_plat + total_glue
total_discount = price * (percent_discount / 100)
total_price = price - total_discount

print(f"{total_price:.3f}")

