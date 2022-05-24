tax_for_one_year = int(input())
shoes = tax_for_one_year - 0.4 * tax_for_one_year
suit = shoes - 0.2 * shoes
ball = (1 / 4) * suit
additional = (1 / 5) * ball
end_price = tax_for_one_year + shoes + suit + ball + additional

print(end_price)
