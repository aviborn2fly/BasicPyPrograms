weight = input('weight:')
unit = input('Enter (L)lbs or (K)Kg: ')

if unit.upper() == 'K':
    converted_weight = float(weight) * 2.20462
    print(f'Your weight is {converted_weight} lbs')

elif unit.upper() == 'L':
    converted_weight = float(weight) * 0.454
    print(f'Your weight is {converted_weight} kg')

else:
    print('Wrong input')
