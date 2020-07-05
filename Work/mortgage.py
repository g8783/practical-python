# mortgage.py
#
# Exercise 1.7


principal = 500000.0
rate = 0.05
payment = 2684.11
monthly_payment = payment
total_paid = 0.0
extra_payment_start_month = 61
extra_payment_end_month = 108
extra_payment = 1000
i_month = 0

while principal > 0:
    i_month += 1

    if i_month <= extra_payment_end_month and i_month >= extra_payment_start_month:
        monthly_payment = payment + extra_payment
        
        if principal * (1+rate/12) < monthly_payment:
             monthly_payment = principal * (1+rate/12)             
    else:
        monthly_payment = payment
        if principal * (1+rate/12) < monthly_payment:
             monthly_payment = principal * (1+rate/12)
             
    principal = principal * (1+rate/12) - monthly_payment
    total_paid = total_paid + monthly_payment
    print(f' Month {i_month:>3d} Total ${total_paid:>10.2f} Principal ${principal:>10.2f}')

print(f'Total paid, ${round(total_paid, 2):0.2f}')
print('Months', i_month)