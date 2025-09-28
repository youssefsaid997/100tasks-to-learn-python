# Mathmetical operations in Python project

# Bill Calculator
print('Welcome to the split bill calculator!\n')


total_bill_input = input('What was the total bill? $')
total_bill= int(total_bill_input);


tip_amount_input = input('What is the tip amount you want to pay 10, 12 or 15? ')
tip_amount = int(tip_amount_input)

number_of_persons_input = input("What was the total number of persons to split the bill around? ")
number_of_people = int(number_of_persons_input)

each_person_payment = (tip_amount + total_bill) / number_of_people

output_message = 'Each person must pay $'+ str(each_person_payment)
# instead of using concating strings and converting as above we can use something else
# it is called f-string => f"" it is like the template literal in JS without converting each value

output_message = f"Each person must pay $# {each_person_payment}"

print(output_message)
