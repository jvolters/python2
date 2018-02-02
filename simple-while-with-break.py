# simple while loop
# same as ...
# ###########################
#
# spam = 0
# if spam < 5:
#     print('Hello World!')
#     spam = spam + 1
#
# ###########################
#
# demo break ... when count reaches 6, the loop will exit
spam = 0                     # init the counter
while spam < 10:             # set the loop counter condition
    print('Loop count: '+str(spam)+' Howdy World!!')
    if spam == 6:
        break
    spam = spam+1
