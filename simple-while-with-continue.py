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
# demo continue ... when count reaches 6, the loop will skip output and halts...
# why?  the program jumps up to the beginning of the loop without being
# incremented to 7, falls back again to the if test for spam == 6, which is
# still true, and continue redirects to the top of the loop.
# Essentially, we've created an infinite looping condition when the counter,
# spam, reaches the value 6.
spam = 0                     # init the counter
while spam < 10:             # set the loop counter condition
    if spam == 6:
        continue
    print('Loop count: '+str(spam)+' Howdy World!!')
    spam = spam+1
