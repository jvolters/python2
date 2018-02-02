import random
print('usage: type getAnswer(n), where n is a number between 1 and 9')

def getAnswer(answerNumber):
    if answerNumber == 1:
        return 'It is decreed that it shall come to pass.'
    elif answerNumber == 2:
        return 'It is almost certainly so.'
    elif answerNumber == 3:
        return 'Yes.'
    elif answerNumber == 4:
        return 'It is unclear, try again.'
    elif answerNumber == 5:
        return 'Ask again later.'
    elif answerNumber == 6:
        return 'Concentrate and ask me again.'
    elif answerNumber == 7:
        return 'My reply is no.'
    elif answerNumber == 8:
        return 'Outlook not certain.'
    elif answerNumber == 9:
        return 'Very doubtful.'
    else:
        return 'Your entry was not between 1 and 9!  Bye!'
    # r = random.randint(1,9)
    # outlook = getAnswer(r)
    # print(outlook)
    print(getAnswer(random.randint(1,9)))
