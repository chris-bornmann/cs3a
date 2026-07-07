from decimal import Decimal, ROUND_HALF_UP

# Get the total budget amont as a Decimal so that floats don't
# goof the math up.
budget = Decimal(input('Enter budget for month: $'))

running_total = Decimal('0.00')

while True:
    line_item = Decimal(input('Enter expense amount (or 0 to quit): $'))
    if line_item == 0:
        break
    running_total = running_total + line_item

over_under = budget - running_total

if over_under > 0:
    print(f'Congratulations!  You are under budget by ${over_under.quantize(Decimal("0.01"))}.')
elif over_under < 0:
    print(f'Ouch!  Beans and rice next month...  You are over by ${abs(over_under.quantize(Decimal("0.01")))}')
else:
    print('Perfect - you are exactly on budget.')
