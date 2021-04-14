#!/usr/bin/env python3

# for loop

people = {'firstname': 'Muhammad', 'lastname': 'Salisu', 'age': 40}

# print(people)

# for p in people:
#     print(p)

#for k, v in people.items():
 #   print(f'{k}: {v}')

# for i in range(1,11):
#     print(i, end=', ', flush=True)

# while 
# display a welcome message
print("The Test Scores program")
print()

# initial variables
score_total = 0
counter = 0
test_score = 0

while True:
    test_score = int(input('Enter score total: '))
    if test_score >= 0 and test_score <= 100:
        score_total += test_score
        counter += 1
    elif test_score == 999:
        break
    else:
        print('Test score must be from 0 through 100.')
    
# calculate average score
average_score = round(score_total / counter)

#Format and display the result
print(f'counter {counter}')
print(f'Total Score: {score_total} \nAverage Score: {average_score}')
