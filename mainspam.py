#DISCORD SPAMMER

#Youtube - https://www.youtube.com/channel/UCYHJ7fQ6FtJyx3YxSWwOhHg
#Noobmaster69 Github - https://github.com/noobymaster69
#PoppinPoptarts GitHub - https://github.com/PoppinPoptarts


import pyautogui, time, num2words, sys
string = input("Text To Spam : ")
timestospam = input("Times to Spam : ")
textdelay = input("Spam delay : ")
Logging = input("Do you want to Enable Logging? 1 for Yes and 2 for no: ")
timestospam = int(timestospam)
textdelay = int(textdelay)

if timestospam >= (10000):
    print("You cannot spam above 10000 lines")
    sys.exit(0)
print("Text/Settings Approved, 5 seconds before spam")

time.sleep(5)

print("-------------------------------")
print("Beganning Terminal Logging")
print("-------------------------------")

for word in range(timestospam):
    temp = word + 1
    temp = num2words.num2words(temp)
    time.sleep(textdelay)
    pyautogui.typewrite(string + " ")

    if Logging == ("1"):
        pyautogui.typewrite(temp + " " + "/" + " " + num2words.num2words(timestospam))
    if Logging == ("2"):
            print(temp + " " + "/" + " " + num2words.num2words(timestospam))

    if string[0]=='@':
        time.sleep(1)
        pyautogui.press("enter")
    pyautogui.press("enter")
else:
    if Logging == ("1"):
        pyautogui.typewrite("Finished Spamming")
        pyautogui.press("enter")

    elif Logging == "2":
        pyautogui.typewrite("")
        print("Finished Spamming")
