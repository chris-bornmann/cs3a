from decimal import Decimal, ROUND_HALF_UP

TO_NEWTONS = Decimal('9.80')

# Get the mass in kilograms.  Use Decimal so that we don't get
# weird results due to floating point.
mass = Decimal(input("Enter the object's mass in kilograms: "))

# Check boundary conditions and if it's all ok, calculate the weight in newtons.
if mass > 500:
    print('too heavy!')
elif mass < 100:
    print('too light!')
else:
    weight = mass * TO_NEWTONS
    print(f'weight in newtons: {weight.quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)}')
