# Until You Type Stop : Bot

while True:
    question = input("You: ")
    
    if question.lower() == "stop":
        print("Bot: Bye")
        break
    else:
        print("Bot: I hear you!\n")


#Assignment Reminder System :

while True:
    alert = input("Have you submitted your assignment? ")
    
    if alert.lower() == "done":
        print("Bot: Great! You are all done!")
        break
    else:
        print("Bot: Still waiting... Please submit it!\n")


    #practice