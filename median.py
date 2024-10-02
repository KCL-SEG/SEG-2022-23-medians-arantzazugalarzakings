"""Median calculator."""
"""Solution by Arantzazu Galarza """

while True:
    try:
        print("Enter a list of numbers separated by commas: ")
        numbers = [float(value) for value in input().split(",")]
    except ValueError:
        print("Some input could not be converted to a number!")
    else:
        break
print(numbers)

 
list_lenght = len(numbers)


if list_lenght % 2 == 0: 
    half = list_lenght / 2 
    half = int(half)
    print (f'median is {numbers[half]} and {numbers[half - 1]}')

else: 
    half = list_lenght / 2 
    half = int(half)
    print (f'median is {numbers[half]}') 
 