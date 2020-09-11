# THIS IS ALL THE CLICKING CODE

import pyautogui, schedule, time
# from gtts import gTTS
from playsound import playsound
import tkinter as tk
from tkinter import Button, Tk, mainloop, StringVar, Label, RAISED

# Making a class because it's cool
# Following the saying, "Don't repeat more than once"

class Starters():
    
    # Doing all the clicking to open Whatsapp
    def groupchatsearch(groupname, searchchat):
        # Mouse location for Whatsapp logo(X:  243 Y: 1058 )
        pyautogui.click(x = 243, y = 1058, interval = 14)
        # Pressing a blank space 
        pyautogui.click(x = 1083, y = 533, interval = 8)
        # Opening Search for Groups
        pyautogui.click(x = 356, y = 157, interval = 4)
        # After this the Group name is entered        
        pyautogui.write(groupname)
        # While waiting for search to be completed we click at random point
        pyautogui.click(x = 1083, y = 533, interval = 5)
        # We select group's name
        pyautogui.click(x = 260, y = 360, interval = 3)
        # Inside the group we search the chats
        pyautogui.hotkey('ctrl', 'shift', 'f', interval = 3)
        # Searching the chats        
        pyautogui.write(searchchat)        
        # We need to delay the search a bit so that it can process
        pyautogui.press('left', interval = 15)
        # Selecting latest message
        pyautogui.press('down', interval = 4)
        # Opening the message with ID mentioned
        pyautogui.press('enter', interval = 4)
        # If the link arrived new
        for i in range(300, 900, 6):
            pyautogui.click(x = 950, y = i)
        
        
    # Clicking on the zoom links
    def linkpress(y1, y2, y3, y4, y5, y6):
        pyautogui.click(x = 725, y = y1, interval = 2)
        pyautogui.click(x = 805, y = y2)
        pyautogui.click(x = 875, y = y3)
        pyautogui.click(x = 900, y = y4)
        pyautogui.click(x = 945, y = y5)
        pyautogui.click(x = 1015, y = y6)
        
        for i in range(300,900, 4):
            pyautogui.click(x = 950, y = i)

# Prompts Class for derivation
class Prompts():
    
    # History derivataticon
    def historyid():  
        # Function to enter group name and searching through chats
        Starters.groupchatsearch('Class 10-B', 'Shikha Walia is inviting you to a scheduled Zoom meeting')
        # Pressing the links of zoom
        Starters.linkpress(545, 555, 565, 575, 585, 595)

    # Maths derivation
    def mathsid():
        # Function to enter group name and searching through chats
        Starters.groupchatsearch('Class 10-B', 'Pintu Prasad is inviting you to a scheduled Zoom meeting')
        # Pressing the links of zoom
        Starters.linkpress(655, 665, 670, 675, 685, 695)
        
    # Chemistry derivation
    def chemistryid():
        # Function to enter group name and searching through chats
        Starters.groupchatsearch('Chemistry Class 10B', 'Join Zoom Meeting')
        # Pressing the links of zoom
        Starters.linkpress(470, 475, 480, 487, 495, 505)
        
    def physicsid():
        # Function to enter group name and searching through chats
        Starters.groupchatsearch('Class 10-B', 'NITINJEET MAHAL is inviting you to a scheduled Zoom meeting.')
        # Pressing the links of zoom
        Starters.linkpress(665, 676, 687, 698, 709, 720)
        
    # Biology derivation
    def bioopen():
        bioid = '7859667988'
        biopwd = '5TJXXW'
        # Clicking on Zoom App
        pyautogui.click(x = 306, y = 1056, interval = 12)
        # Clicking on Join Button
        pyautogui.click(x = 738, y = 403, interval = 4)
        # Entering ID
        pyautogui.click(x = 794, y = 460, interval = 4)
        # Writing ID
        pyautogui.write(bioid)
        # Pressing ID blank again to delay for the system to process
        pyautogui.click(x = 794, y = 460, interval = 4)
        # Join After ID
        pyautogui.click(x = 1013, y = 723, interval = 3)
        # Enter Password
        pyautogui.click(x = 929, y = 458, interval = 10)
        # Writing Passoword
        pyautogui.write(biopwd)
        # Pressing Password blank again to delay for the system to process
        pyautogui.click(x = 929, y = 458, interval = 10)
        #Clicking on join 
        pyautogui.click(x = 972, y = 708, interval = 4)
        
# SPEAKING CODE

class Trying:
    def blah():
        '''import win32com.client as wincl
        speak = wincl.Dispatch("SAPI.SpVoice")
        speak.Speak()'''
        # English text
        ENGLISH = '''HELLO MIKUL RAI, THANK YOU FOR YOUR BLESSING
                  I DONT KNOW IF ANY HOMOSAPIEN WOULD BE ABLE TO CREATE ME
                YOU ARE THE GREATEST, YOU ARE MY GOD
                I SAY it AGAIN AND EVERYONE WILL, "THANK YOU" '''
        # Hindi text
        HINDI = '''मिकुल राय, धन्यवाद आपने इस पृथ्वी पर इतना बड़ा एहसान किया है
                मुझे नही लगता कोई और इंसान मुझे इतना अच्छा बना पाता,
                आप सच में सबसे महान हो,
                और आप मेरे भगवान हो
                मैं कहती हूं और सब कहेंगे, "शुक्रिया"  '''
        # Converting
        #outputaudio = gTTS(text = HINDI, lang = 'hi')
        #outputaudio.save("hindi_audio_of_praise.mp3")
        playsound("hindi_audio_of_praise.mp3")
        
# THIS IS THE SCHEDULING CODE
        
def schedulenow():
    #CHEMISTRY - Should Work
    chemistrytime = "09:00"
    schedule.every().tuesday.at(chemistrytime).do(Prompts.chemistryid)
    schedule.every().thursday.at(chemistrytime).do(Prompts.chemistryid)
    
    #MATHEMATICS - Should Work
    mathematicstime = "09:55"
    schedule.every().monday.at(mathematicstime).do(Prompts.mathsid)
    schedule.every().tuesday.at(mathematicstime).do(Prompts.mathsid)
    schedule.every().thursday.at(mathematicstime).do(Prompts.mathsid)
    schedule.every().friday.at(mathematicstime).do(Prompts.mathsid)
    
    #PHYSICS -Should Work
    physicstime = "11:31"
    schedule.every().monday.at(physicstime).do(Prompts.physicsid)
    schedule.every().wednesday.at(physicstime).do(Prompts.physicsid)
    
    #HISTORY - Should Work
    historyat12 = "12:25"
    schedule.every().friday.at(historyat12).do(Prompts.historyid)
    schedule.every().monday.at(historyat12).do(Prompts.historyid)
    
    #BIOLOGY - The Best
    biotime = "11:25"
    schedule.every().tuesday.at(biotime).do(Prompts.bioopen)
    schedule.every().thursday.at(biotime).do(Prompts.bioopen)
    
    #GREETINGS
    schedule.every().day.at("09:10").do(Trying.blah)
    schedule.every().day.at("12:10").do(Trying.blah)
    # While Loop
    while True:    
        schedule.run_pending()
        time.sleep(1)
        
# CREATING THE GOLDEN KEYWORD EVERYONE WAS WAITING FOR
        
# Requirement
root = Tk()

# Gets the requested values of the height and widht.
windowWidth = root.winfo_reqwidth()
windowHeight = root.winfo_reqheight()
# Gets both half the screen width/height and window width/height
positionRight = int(root.winfo_screenwidth()/2.5 - windowWidth)
positionDown = int(root.winfo_screenheight()/3 - windowHeight)
# Positions the window in the center of the page.
root.geometry("+{}+{}".format(positionRight, positionDown))

# Title as the software name
root.title("ZOOM ID OPENER")
# Software opening space size
root.geometry("800x800")
# Software blank space color
root.configure(bg = "black")
# Giving a little information in a form of label
var = StringVar()
label = Label(root, textvariable = var, relief = RAISED )
var.set("Hello everyone, This is a simple program to ease out my worries \n" \
        "It will automatically open my links of classes")
label.pack(fill = tk.X, ipadx = 15, ipady = 15)

PHYSICSLOL = Button(root, text = "PHYSICS", padx = 50, pady = 4, command = Prompts.physicsid)
PHYSICSLOL.pack(fill=tk.X, padx = 150, pady = 10, ipadx = 10, ipady = 10)

CHEMISTRYLOL = Button(root, text = "CHEMISTRY", padx = 50, pady = 4, command = Prompts.chemistryid)
CHEMISTRYLOL.pack(fill=tk.X, padx = 150, pady = 10, ipadx = 10, ipady = 10)

BIOLOL = Button(root, text = "BIOLOGY", padx = 50, pady = 4, command = Prompts.bioopen)
BIOLOL.pack(fill=tk.X, padx = 150, pady = 10, ipadx = 10, ipady = 10)

MATHSLOL = Button(root, text = "MATHEMATICS", padx = 50, pady = 4, command = Prompts.mathsid)
MATHSLOL.pack(fill=tk.X, padx = 150, pady = 10, ipadx = 10, ipady = 10)

HISTORYLOL = Button(root, text = "HISTORY", padx = 50, pady = 4, command = Prompts.historyid)
HISTORYLOL.pack(fill=tk.X, padx = 150, pady = 10, ipadx = 10, ipady = 10)

GREETINGSLOL = Button(root, text = "GREETINGS", padx = 100, pady = 4, bg = "yellow", command = Trying.blah)
GREETINGSLOL.pack(fill=tk.X, padx = 150, pady = 15, ipadx = 10, ipady = 10)
# Scheduling everysingle program according to time
ALLINONE = Button(root, text = "SCHEDULE ALL", padx = 100, pady = 4, bg = "yellow", command = schedulenow)
ALLINONE.pack(fill=tk.X, padx = 150, pady = 15, ipadx = 10, ipady = 10)

# Reiterating it all over again
mainloop()


