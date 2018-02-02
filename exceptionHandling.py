# use try block to handle exception
def div(divideBy):
    try:
        return 42 / divideBy
    except ZeroDivisionError:
        print('Error: invalid argument 0, threw a divide by 0 exception.')
