# while loop
secret_answer = "cairo"
answer= ""
count = 0
limit = 3
lose= False
while secret_answer != answer and not lose:
    if count < limit:
        answer = input("what is capital of Egypt? ")
        count += 1
    else:
        lose= True
if lose:
    print("you are loser")
else:
    print("you win")