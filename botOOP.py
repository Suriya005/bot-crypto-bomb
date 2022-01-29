from tkinter import *
import pyautogui
import time

root = Tk()
root.title("Bot BombCrypto")
root.geometry("300x400")

# region=(1920, 0, 800, 700)
# myScreen = 450, 150, 950, 650

class BombCryptoBot:
    def __init__(self, x, y , width, height):
        # self.screen = (x, y, width, height)
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        # self.imageLocation = None
        self.resetLoop = 99 
        self.resetTime = 240000
        self.workTime = 5 * 60 * 1000
        self.restTime = 10 * 60 * 1000
        
    def setBotTime(self, workTime, restTime, resetTime):
        self.workTime = workTime * 60 * 1000
        self.restTime = restTime * 60 * 1000
        self.resetTime = resetTime * 60 * 1000
    
    def setScreen(x, y, width, height):
        self.__screen = (x, y, width, height)
        
    def searchPositoinImage(self, imageLocation, count=99):
        search_count = 0
        while True:
            indexPage = pyautogui.locateCenterOnScreen(
                imageLocation, region=(self.x, self.y, self.width, self.height))
            if indexPage != None:
                print("I can see", indexPage)
                return indexPage
            elif search_count > count:
                print("Over count, Some thing is wrong")
                return None
            else:
                print("I can't see {} round {}".format(imageLocation, search_count))
                search_count += 1
                
    def checkError(self):
        pass
    
    def connectWallet(self):
        pass
                
    def botIsWork(self):
        print("5 seconds later, work all!!!")
        time.sleep(5)
        indexPage = self.searchPositoinImage('img/index.png', 30)
        if indexPage != None:
            pyautogui.moveTo(indexPage, duration=0.5)
            pyautogui.click(indexPage)
            print("Click to index page")
            time.sleep(2)
            
        up_icon = self.searchPositoinImage('img/up_icon.png', 99)
        if up_icon != None:
            pyautogui.moveTo(up_icon, duration=0.5)
            pyautogui.click(up_icon)
            print("Click to up_icon")
            pyautogui.moveTo(x=500, y=0, duration=0.5)
            time.sleep(2)
            
        knight_icon = self.searchPositoinImage('img/knight_icon.png')
        if knight_icon != None:
            pyautogui.moveTo(knight_icon, duration=0.5)
            pyautogui.click(knight_icon)
            print("Click to knight_icon")
            time.sleep(2)
            
        work_all = self.searchPositoinImage('img/work_all.png', 10)
        if work_all != None:
            pyautogui.moveTo(work_all, duration=0.5)
            pyautogui.click(work_all)
            print("Click to work_all")
            time.sleep(2)
            
        close_icon = self.searchPositoinImage('img/close_icon.png')
        if close_icon != None:
            pyautogui.moveTo(close_icon, duration=0.5)
            pyautogui.click(close_icon)
            print("Click to close_icon")
            time.sleep(5)
            pyautogui.click(close_icon)
            time.sleep(2)
        reset_time = 0
        for i in range(self.resetLoop):
            reset_time = reset_time + 240000
            if reset_time > self.workTime:
                break
            root.after(reset_time, self.botIsResetScreen)
        root.after(self.workTime, self.botIsRest)
        
    def botIsResetScreen(self):
        print("5 seconds later, reset screen!!!")
        time.sleep(5)
        back_icon = self.searchPositoinImage('img/back_icon.png')
        if back_icon != None:
            pyautogui.moveTo(back_icon, duration=0.5)
            pyautogui.click(back_icon)
            print("Click to back_icon")
            time.sleep(2)
            
        indexPage = self.searchPositoinImage('img/index.png')
        if indexPage != None:
            pyautogui.moveTo(indexPage, duration=0.5)
            pyautogui.click(indexPage)
            print("Click to index page")
            time.sleep(2)

        
        
    def botIsRest(self):
        print("5 seconds later, rest all!!!")
        time.sleep(5)
        up_icon = self.searchPositoinImage('img/up_icon.png')
        if up_icon != None:
            pyautogui.moveTo(up_icon, duration=0.5)
            pyautogui.click(up_icon)
            print("Click to up_icon")
            pyautogui.moveTo(x=500, y=0, duration=0.5)
            time.sleep(2)
        knight_icon = self.searchPositoinImage('img/knight_icon.png')
        if knight_icon != None:
            pyautogui.moveTo(knight_icon, duration=0.5)
            pyautogui.click(knight_icon)
            print("Click to knight_icon")
            time.sleep(5)
            
        rest_all = self.searchPositoinImage('img/rest_all.png', 10)
        if rest_all != None:
            pyautogui.moveTo(rest_all, duration=0.5)
            pyautogui.click(rest_all)
            print("Click to rest_all")
            time.sleep(2)
        
        close_icon = self.searchPositoinImage('img/close_icon.png')
        if close_icon != None:
            pyautogui.moveTo(close_icon, duration=0.5)
            pyautogui.click(close_icon)
            print("Click to close_icon")
            time.sleep(2)
            
        back_icon = self.searchPositoinImage('img/back_icon.png')
        if back_icon != None:
            pyautogui.moveTo(back_icon, duration=0.5)
            pyautogui.click(back_icon)
            print("Click to back_icon")
            time.sleep(2)
            
        root.after(self.restTime, self.botIsWork)
        
def testStr():
    bot2 = BombCryptoBot(xScreen.get(), yScreen.get(), widthScreen.get(), heightScreen.get())  
    bot2.setBotTime(workAll.get(), restAll.get(), resetAll.get())
    bot2.botIsWork()  

  
bot1 = BombCryptoBot(0, 0, 800, 500)
widthScreen=IntVar()
heightScreen=IntVar()
xScreen=IntVar()
yScreen=IntVar()
workAll=IntVar()
restAll=IntVar()
resetAll=IntVar()

Label(root, text="X:").pack()
setX=Entry(root, textvariable=xScreen).pack() 
xScreen.set(0)
Label(root, text="Y:").pack()
sety=Entry(root, textvariable=yScreen).pack()  
yScreen.set(0)
Label(root, text="Width:").pack()
setWidth = Entry(root,textvariable=widthScreen).pack()  
widthScreen.set(800)
Label(root, text="Height:").pack()
setHeight = Entry(root,textvariable=heightScreen).pack()  
heightScreen.set(800)

Label(root, text="Work").pack()
setWorkAll = Entry(root,textvariable=workAll).pack()  
workAll.set(5)
Label(root, text="Rest:").pack()
setRestAll = Entry(root,textvariable=restAll).pack()  
restAll.set(10)
Label(root, text="Reset:").pack()
setResetAll = Entry(root,textvariable=resetAll).pack()  
resetAll.set(4)




testBtn = Button(root, text="Test", command=testStr).pack()
startButton = Button(root, text="Start", command=bot1.botIsWork,
                     width=10, fg="green", bg="black").pack()
root.mainloop()




# def workAll():
#     print("work!!")
#     while True:
#         indexPage = pyautogui.locateCenterOnScreen(
#             'img/index.png', region=(450, 150, 950, 650))
#         if indexPage != None:
#             pyautogui.moveTo(indexPage, duration=0.5)
#             pyautogui.click(indexPage)
#             print("come to index page")
#             time.sleep(2)
#             break
#         else:
#             print("I can't see index page")

#     while True:
#         up_icon = pyautogui.locateCenterOnScreen(
#             'img/up_icon.png', region=(450, 150, 950, 650))
#         if up_icon != None:
#             pyautogui.moveTo(up_icon, duration=0.5)
#             pyautogui.click(up_icon)
#             print("come to up_icon")
#             # time.sleep(5)
#             # pyautogui.click(up_icon)
#             pyautogui.moveTo(x=500, y=0, duration=0.5)
#             time.sleep(2)
#             break
#         else:
#             print("I can't see up_icon")

#     while True:
#         knight_icon = pyautogui.locateCenterOnScreen('img/knight_icon.png', region=(450, 150, 950, 650))
#         if knight_icon != None:
#             pyautogui.moveTo(knight_icon, duration=0.5)
#             pyautogui.click(knight_icon)
#             print("come to knight_icon")
#             time.sleep(2)
#             break
#         else:
#             print("I can't see knight_icon")
#     work_count = 0
#     while True:
#         work_all = pyautogui.locateCenterOnScreen(
#             'img/work_all.png', region=(450, 150, 950, 650))
#         if work_all != None:
#             pyautogui.moveTo(work_all, duration=0.5)
#             pyautogui.click(work_all)
#             print("come to work_all")
#             time.sleep(2)
#             break
        
#         elif work_count > 10:
#             break
        
#         else:
#             print("I can't see work_all")
#             work_count += 1

#     while True:
#         close_icon = pyautogui.locateCenterOnScreen(
#             'img/close_icon.png', region=(450, 150, 950, 650))
#         if close_icon != None:
#             pyautogui.moveTo(close_icon, duration=0.5)
#             pyautogui.click(close_icon)
#             print("come to close_icon")
#             time.sleep(5)
#             pyautogui.click(close_icon)
#             break
#         else:
#             print("I can't see close_icon")
#     root.after(240000, resetScreen)
#     root.after(300000, restAll)


# def resetScreen():
#     print("start resetScreen")
#     while True:
#         back_icon = pyautogui.locateCenterOnScreen(
#             'img/back_icon.png', region=(450, 150, 950, 650))
#         if back_icon != None:
#             pyautogui.moveTo(back_icon, duration=0.5)
#             pyautogui.click(back_icon)
#             print("come to back_icon")
#             time.sleep(2)
#             break
#         else:
#             print("I can't see back_icon")

#     while True:
#         indexPage = pyautogui.locateCenterOnScreen(
#             'img/index.png', region=(450, 150, 950, 650))
#         if indexPage != None:
#             pyautogui.moveTo(indexPage, duration=0.5)
#             pyautogui.click(indexPage)
#             print("come to index page")
#             time.sleep(2)
#             break
#         else:
#             print("I can't see index page")
#     # root.after(240000, resetScreen)


# def restAll():
#     print("sleep")
    
#     while True:
#         up_icon = pyautogui.locateCenterOnScreen(
#             'img/up_icon.png', region=(450, 150, 950, 650))
#         if up_icon != None:
#             pyautogui.moveTo(up_icon, duration=0.5)
#             pyautogui.click(up_icon)
#             print("come to up_icon")
#             time.sleep(2)
#             break
#         else:
#             print("I can't see up_icon")
            
#     pyautogui.moveTo(x=500, y=0, duration=0.5)
#     while True:
#         knight_icon = pyautogui.locateCenterOnScreen('img/knight_icon.png', region=(450, 150, 950, 650))
#         if knight_icon != None:
#             pyautogui.moveTo(knight_icon, duration=0.5)
#             pyautogui.click(knight_icon)
#             print("come to knight_icon")
#             time.sleep(2)
#             break
#         else:
#             print("I can't see knight_icon")
    
#     rest_count = 0
#     while True:
#         rest_all = pyautogui.locateCenterOnScreen(
#             'img/rest_all.png', region=(450, 150, 950, 650))
#         if rest_all != None:
#             pyautogui.moveTo(rest_all, duration=0.5)
#             pyautogui.click(rest_all)
#             print("come to rest_all")
#             time.sleep(2)
#             break
        
#         elif rest_count > 10:
#             break
        
#         else:
#             print("I can't see rest_all")
#             rest_count += 1      
            
#     while True:
#         close_icon = pyautogui.locateCenterOnScreen(
#             'img/close_icon.png', region=(450, 150, 950, 650))
#         if close_icon != None:
#             pyautogui.moveTo(close_icon, duration=0.5)
#             pyautogui.click(close_icon)
#             print("come to close_icon")
#             time.sleep(5)
#             pyautogui.click(close_icon)
#             break
#         else:
#             print("I can't see close_icon")
    
#     while True:
#         back_icon = pyautogui.locateCenterOnScreen(
#             'img/back_icon.png', region=(450, 150, 950, 650))
#         if back_icon != None:
#             pyautogui.moveTo(back_icon, duration=0.5)
#             pyautogui.click(back_icon)
#             print("come to back_icon")
#             time.sleep(2)
#             break
#         else:
#             print("I can't see back_icon")
#     root.after(600000, workAll)



