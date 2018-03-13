deposit = int(input("deposit = "))
percent = float(input("percent = "))
day = int(input("day = "))
fullpercent = 100
year = 365
tax = 0.13

income = deposit*percent*day/fullpercent/year
profit = income-tax*income
total = deposit+profit
#popolnenie!!!!!!!!!!!!

print("Депозит =",deposit)
print("Доход за", day, "дней =",profit)
print("Итог =",total)