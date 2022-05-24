deposit = float(input())
deposit_time_months = int(input())
year_deposit_percentage = float(input())
profit_earned_yearly = deposit * (year_deposit_percentage / 100)
profit_earned_monthly = profit_earned_yearly / 12
total_profit = deposit + deposit_time_months * profit_earned_monthly
print(total_profit)
