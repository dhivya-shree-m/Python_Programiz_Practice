principal_amount = float(input())
rate_of_interest = float(input())
time_in_years = float(input())
simple_interest = principal_amount * rate_of_interest*time_in_years*0.01
print(simple_interest)
final_amount = principal_amount + simple_interest
print(final_amount)
