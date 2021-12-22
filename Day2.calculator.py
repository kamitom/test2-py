print('Welcome to the tip calculator.')
total_bill = float(input('What was the total bill?$'))
how_many_people = int(input('How many people to split the bill?'))
what_percentage = float(
    input('What percentage tip would you like to give?10, 12 or 15?'))
each_person_should_pay = (
    total_bill * ((100+what_percentage)/100))/how_many_people
the_answer = round(each_person_should_pay, 1)
print('Each person should pay $', str(the_answer))
