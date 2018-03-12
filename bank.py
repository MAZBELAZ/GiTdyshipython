deposit=int(input("deposit="))
percent=int(input(("percent="))
day=int(input("day="))
fullpercent=int(100)
year=int(365)

income=deposit*percent*day/fullpercent/year
profit=income-tax*income
total=deposit+profit
#popolnenie!!!!!!!!!!!!

print(deposit)
print(total)