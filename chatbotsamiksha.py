print("Campus Assistant Chatbot")
print("Type 'bye' to exit")

while True:
    user = input("You:").lower()

    if user == "hello":
        print("Bot: Hello! Welcome to Campus Assistant Bot.")

    elif "timing" in user:
        print("Bot: College timings are 11 AM to 6 PM.")

    elif "course" in user:
        print("Bot: We offer BCA, BBA and B.Com courses.")

    elif "admission" in user:
        print("Bot: Visit the admission office or apply online.")

    elif "library" in user:
        print("Bot: The library is on the first floor.")

    elif user == "bye":
        print("Bot: Thank you! Have a nice day.")
        break

    else:
        print("Bot: Sorry, I don't understand.")