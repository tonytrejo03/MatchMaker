# Anthony Trejo
# MatchMaker

INTRODUCTION = ''' 
                          *************************
                                 Matchmaker
                            The best dating site
                          *************************

In this game we will see how similar we both are. You'll have to answer 5 questions. 
Each question with the number 1-5. 5 meaning you strongly agree, answer 4 if you agree,
3 is you're neutral, 2 if you disagree, and 1 if you strongly disagre.


What are you waiting for? let's get started!
'''

QUESTION = [ 
    'I love to spend money on my truck.',
    'I love going to Mexico.',
    'Wingstop is better than Bdubs.',
    'I will rather stay home than go party.',
    'I will rather play video games than a sport.'
]

DESIRED_ANSWER = [ 
    5, # strongly agree
    3, # neutral
    1, # Strongly disagree
    4, # Agree
    2, # disagree
]

MAX_SCORE = 5 * len(QUESTION)

print(INTRODUCTION)



response = []
difference = []

for i in range(len(QUESTION)):
    userResponse = int(input(QUESTION[i]))
    response.append(userResponse)

    questionDifference = 5 - abs(userResponse - DESIRED_ANSWER[i])
    difference.append(questionDifference)

    
    print('question %d difference: %d\n' % (i+1, questionDifference))

totalDifference = 0
for d in difference: 
    totalDifference += d

totalDifference *= 100 / MAX_SCORE
print('Total Difference: %d\n\n' % (totalDifference))



# Credits Eric Pogue

def introdcution():
    print('Introduction:... ')

def getAValidNumberBetween1And5():
    UserResponse2String = str(input(('Enter a number between 1 and 5.\n')))
    print('You entered: ' + UserResponse2String)

    if not UserResponse2String.isnumeric():
        print('This is not a number')
        return -1
    else:
        print('This is a valid number')
        UserResponse2Int = int(UserResponse2String)
        if (UserResponse2Int >= 1) and (UserResponse2Int <= 5):
            print("You have entered a number between 1-5.")
            return UserResponse2Int
        else: 

            print("your number is not between 1-5")
            return -1



# Program starts executing here.
introdcution()

number = -1 
while (number == -1):
    number = getAValidNumberBetween1And5()
    if (number == -1):
        print('Please try again.')
print(number)