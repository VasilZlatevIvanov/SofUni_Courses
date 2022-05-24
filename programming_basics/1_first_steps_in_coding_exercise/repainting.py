needed_nylon = int(input())
needed_paint = int(input())
needed_thinner = int(input())
working_hours = int(input())
nylon_price = 1.50
paint_price = 14.50
thinner_price = 5.00
bags = 0.40
add_paint = needed_paint + 0.1 * needed_paint
add_nylon = needed_nylon + 2
sum_materials = add_nylon * nylon_price \
                + add_paint * paint_price \
                + needed_thinner * thinner_price \
                + bags
workers_pay_per_hour = 0.3 * sum_materials
end_price = workers_pay_per_hour * working_hours + sum_materials
print(end_price)
