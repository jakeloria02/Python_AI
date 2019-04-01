import requests, json





leave = {"exit", "leave", "end", "bye"}
GREETINGS = {"hello", "hey", "yo", "boi", 'hey man', 'hey boi', 'hey 117', 'hey [117]', "heyo", "heyy"}
GREETING_RESP = {"Hello", "Hey", "Hello, Sir!"}
WEATHER = {'whats the weather today?', "weather", 'whats the weather?', 'whats the weather today', 'whats the weather'}

resp = None




print("[117] Welcome back!")
print("[117] How may I help you?")

while True:
    try:
        resp = raw_input(">>")

    except :
        print("Sorry, I didnt understand that.")

        continue



    if  resp in leave:
        print("[117] Bye!")
        break

    elif resp in GREETINGS:
        print("[117] Hello Sir!")




    elif resp in WEATHER:
            print("....")
            import weather


    else:
            print("[117] sorry I dont have an answer to that question yet please try a different one!")
