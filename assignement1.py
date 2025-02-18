

salary = int(input("Enter your salary for the month: "))


month = input("Enter the name of the month: ")


savings_percentage = float(input("Enter the percentage for savings: "))
rent_percentage = float(input("Enter the percentage for rent: "))
electricity_percentage = float(input("Enter the percentage for electricity: "))


savings_amount = (savings_percentage / 100) * salary
rent_amount = (rent_percentage / 100) * salary
electricity_amount = (electricity_percentage / 100) * salary

total_expenses = savings_amount + rent_amount + electricity_amount


remainder = salary - total_expenses


yearly_rent = rent_amount * 12
yearly_electricity = electricity_amount * 12


salary_squared = salary ** 2


additional_savings = 50
savings_divided = additional_savings / savings_amount

print("Your salary for the month is: ", salary)
print("The month is: ", month)
print("The percentage for savings is: ", savings_percentage)
print("The percentage for rent is: ", rent_percentage)
print("The percentage for electricity is: ", electricity_percentage)
print("The amount for savings is: ", savings_amount)
print("The amount for rent is: ", rent_amount)
print("The amount for electricity is: ", electricity_amount)
print("The total expenses are: ", total_expenses)
print("The remainder is: ", remainder)
print("The yearly rent is: ", yearly_rent)
print("The yearly electricity is: ", yearly_electricity)
print("The square of the salary is: ", salary_squared)
print("The additional savings is: ", additional_savings)
print("The savings divided by the additional savings is: ", savings_divided)
