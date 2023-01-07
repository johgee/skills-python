total = 0
counter = 1
number = int(input('how many numbers will be given?'))

while counter <= number:
  current_number = input('provide a number: ')
  while not current_number.isnumeric():
    current_number = input('wrong! thats\'s not a number! try again: ')
  total += int(current_number)
  counter += 1
print(total/number)