import sys
while True:       #set up inifinite loop
    print('Type \'exit\' to halt the loop')
    response = input()
    if response == 'exit':
        sys.exit()
    print('You typed '+str(response) +'.')
    
