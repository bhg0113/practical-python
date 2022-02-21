# mortgage.py

principal = 500000.0 # 대출금
rate = 0.05 # 이율
payment = 2684.11 # 상환금액
total_paid = 0.0
month = 0

extra_payment_start_month = 61
extra_payment_end_month = 108
extra_payment = 1000

while principal > 0:
    month += 1
    if month <= extra_payment_end_month and month >=extra_payment_start_month:
        payment = 2684.11 + extra_payment
    else:
        payment = 2684.11
    principal = principal * (1+rate/12) - payment
    total_paid = total_paid + payment
    
    print(month, total_paid, principal)

    if principal <0:
        total_paid += principal
    
print('Total paid', f'{total_paid:0.2f}', '\n','month',month)

# Exercise 1.7


#kkkkkk
