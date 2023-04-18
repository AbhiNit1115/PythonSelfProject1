# if elif statement: To show a multi way decision based on several conditions we use if elif.
# e.g. if (condition1):
# statement1
#     elif (condition2):
# statement2
#     elif (condition3):
# statement3

# Here once the code executes it will first check the "if" condition and its respective statement in case if
# it's true the it will halt the execution in case if its false it will move to first elif condition and so on
# so, as soon as any condition gets satisfied the if elif statement execution halts. So basically in if elif
# case once any of the condition gets satisfies the rest of the code will never execute. In the end we are
# adding and else block which says if none of the if/elif statements are true then execute else
a = 5
if a == 10:
    print("first Line")
elif a == 20:
    print("Second Line")
elif a == 51:
    print("third line")
else:
    print("NOTA")
