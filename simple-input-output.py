# this is a simple program to demonstrate print() output function and input()
# keyboard capture function
print()                               # print() output a blank line... like stdout
print('-----------')
print('Hello World')
print('-----------')
print()
print('What is your name?')
inputName=input()                     # input() keyboard... like stdin
print('Hi '+inputName+', it is good to meet you.')
print()
print(inputName+', your name is '+str(len(inputName))+' characters long.')
print()
print('How old are you?')
inputAge=input()
print()
print(inputName+', will be able to retire in '+ str(68-(int(inputAge)))+' years.')
print('That\'s all for now!')
