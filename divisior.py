num = int(raw_input("Enter any number-"))

listRange = list(range(1,num+1))

output = []

for number in listRange:
    if num % number == 0:
        output.append(number)

print(output)