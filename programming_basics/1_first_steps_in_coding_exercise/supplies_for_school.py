count_pencils = int(input())
count_markers = int(input())
count_detergent = int(input())
percentage_off_price = int(input())
pencils = 5.80
markers = 7.20
detergent = 1.20
total_price_without_discount = (count_pencils * pencils + count_markers * markers + count_detergent * detergent)
total_price_with_discount = total_price_without_discount - total_price_without_discount * percentage_off_price / 100
print(total_price_with_discount)
