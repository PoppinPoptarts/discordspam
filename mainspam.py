import pyautogui
import time
import num2words
import sys

#DISCORD SPAMMER

#Youtube - https://www.youtube.com/channel/UCYHJ7fQ6FtJyx3YxSWwOhHg
#Noobmaster69 Github - https://github.com/noobymaster69
#PoppinPoptarts GitHub - https://github.com/PoppinPoptarts

print("[1] - Normal Text\n[2] - Wave text\n[3] - 2 line spam") 
VersionSelect = input("Choose your version : ")

def NormalVersion():
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
        time.sleep(textdelay+0.3)
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
            return
            
if VersionSelect == ("1"):
    NormalVersion()

def Wave():
    zigtexttospam = input("Text To Spam : ")
    print("Before you enter an amout of times to spam, remeb er that this program(ZigZag) is still under development, and will lag a bit")
    time.sleep(1.5)
    choice = input("Times to spam : ")
    print("------------------------------------")
    zigzagcolor = input("[0] - No Color\n[1] - Blue\n[2] - Yellow\nChoose a Color.  : ")
    choice = int(choice)
    if choice >= (4):
        print("You cannot spam above 4 lines. This number will increase once we fix an issue")
        sys.exit(0)
    print("5 seconds before spam")

    time.sleep(5)

    variable = """{}
{}
 {}
  {}
   {}
     {}
       {}
         {}
            {}
               {}
                  {}
                     {}
                        {}
                           {}
                              {}
                                 {}
                                    {}
                                       {}
                                         {}
                                           {}
                                             {}
                                              {}
                                               {}
                                                {}
                                                {}
                                                {}
                                                {}
                                               {}
                                              {}
                                            {}
                                         {}
                                       {}
                                     {}
                                   {}
                                 {}
                              {}
                            {}
                          {}
                        {}
                      {}
                    {}
                 {}
               {}
            {}
         {}
      {}
   {}
 {}
{}""".format(zigtexttospam,zigtexttospam,zigtexttospam,zigtexttospam,zigtexttospam,zigtexttospam,zigtexttospam,zigtexttospam,zigtexttospam,zigtexttospam,zigtexttospam,zigtexttospam,zigtexttospam,zigtexttospam,zigtexttospam,zigtexttospam,zigtexttospam,zigtexttospam,zigtexttospam,zigtexttospam,zigtexttospam,zigtexttospam,zigtexttospam,zigtexttospam,zigtexttospam,zigtexttospam,zigtexttospam,zigtexttospam,zigtexttospam,zigtexttospam,zigtexttospam,zigtexttospam,zigtexttospam,zigtexttospam,zigtexttospam,zigtexttospam,zigtexttospam,zigtexttospam,zigtexttospam,zigtexttospam,zigtexttospam,zigtexttospam,zigtexttospam,zigtexttospam,zigtexttospam,zigtexttospam,zigtexttospam,zigtexttospam,zigtexttospam)

    if zigzagcolor == ("0"):
      for i in range(choice):
            pyautogui.typewrite('```\n' + variable + '```')
            pyautogui.press("enter")

    if zigzagcolor == ("1"):
      for i in range(choice):
            pyautogui.typewrite('```json\n"' + variable + '"```')
            pyautogui.press("enter")

    if zigzagcolor == ("2"):
      for i in range(choice):
            pyautogui.typewrite('```fix\n' + variable + '```')
            pyautogui.press("enter")
    return

if VersionSelect == ("2"):
    Wave()

def twolinespam():
    tl_line1 = input("Line 1 : ")
    tl_line2 = input("Line 2 : ")
    timestospam = input("Times to Spam : ")
    textdelay = input("Spam delay : ")
    
    timestospam = int(timestospam)
    textdelay = int(textdelay)
    
    print("Text/Settings aproved, 5 seconds before spam")
    time.sleep(5)

    for i in range(timestospam):
            pyautogui.typewrite(tl_line1)
            pyautogui.press("enter")
            time.sleep(textdelay)
            pyautogui.typewrite(tl_line2)
            pyautogui.press("enter")
            time.sleep(textdelay)

if VersionSelect == ("3"):
    twolinespam()
