#import lines
from tkinter import *
from tkinter.ttk import *
from turtle import *
import turtlefigures
from tkinter import ttk 
from tkinter import font



#create an empty frame and setup its geometry
root = Tk()
root.geometry("980x650+200+200")
root.title("Turtle Interface")
root.configure(bg='Light Blue')


#set interface style
style = ttk.Style()
style.theme_use('classic')

#create canvas
canvasFrame= LabelFrame(root, text = "Turtle Canvas", borderwidth=15)
canvas = Canvas(canvasFrame, width = 500, height = 500)
canvas.pack()

canvasFrame.grid(row = 0, column = 4, columnspan = 4, padx = 20, pady = 20)
canvasFrame.place(x=390, y=50)


#make screen
screen = TurtleScreen(canvas)
screen.bgcolor("pink")
w, h = screen.screensize()

#make pen & set default value
pen = RawTurtle(screen)
pen.color("purple")


# make a control panel and grid it
controlFrame = LabelFrame(root, text = "Control Panel", borderwidth=15)
controlFrame.grid(row = 0, column = 0, padx = 40, pady =40)
controlFrame.place(x=50, y=50)


orderLabel = Label(controlFrame, text = "Figure")
orderLabel.grid(row = 0, column = 0)

orderLabel = Label(controlFrame, text = "Order")
orderLabel.grid(row = 1, column = 0)

orderStr = StringVar()
orderEntry = Entry(controlFrame, textvariable = orderStr)
orderEntry.grid(row = 1 , column = 1, columnspan = 2)

lengthLabel = Label(controlFrame, text = "Length")
lengthLabel.grid(row =2, column = 0)

lengthStr = StringVar()
lengthEntry = Entry(controlFrame, textvariable = lengthStr)
lengthEntry.grid(row = 2, column = 1, columnspan = 2)

label = Label(controlFrame, text = "Pen Color")
label.grid(row = 3, column = 0)

label = Label(controlFrame, text = "Pen Speed")
label.grid(row = 4, column = 0)

label = Label(controlFrame, text = "Pen Width")
label.grid(row =5, column = 0)


#create slider
penSize = Scale(controlFrame, from_=1, to=6, orient=HORIZONTAL, length = 200)
penSize.set(3.3)
penSize.grid(row =5, column =1)

penSpeed = Scale(controlFrame, from_=1, to=12, orient=HORIZONTAL, length = 200)
penSpeed.set(6)
penSpeed.grid(row =4, column =1)

# Add nested panels to the Control panel
innerFrame =LabelFrame(controlFrame, text = "Initiate Drawing")
innerFrame.grid(row = 6, column = 0, rowspan =1, columnspan = 3)


#make description panel
desFrame = LabelFrame(root, text ="Description", borderwidth=15)
desFrame.place(x=50, y=340)
msg= "GUIDELINES:\n\nStep 1: Select figure to draw.\n\nStep 2: Input Order & Length values.\n\nStep 3: Adjust pen settings as desired.\n\nStep 4: Press 'Draw' to initate drawing & 'Stop' to cancel it.\n\nStep 5: Press 'Clear' to reset canvas."
text=Text(desFrame, height =14, width = 33, bg="lavender",foreground="purple", wrap="word", font="arial")
text.insert('end', msg)
text.pack()

#Create Clear button
def onClearF():
        #clear the entries
        orderStr.set("")
        lengthStr.set("")

        

        #also clear the screen
        screen.resetscreen()
        screen.bgcolor("pink")
        pen.color("purple")
        #tracer()
        #reset dropdown
        figureStr.set("Tree")
        #reset text
        text.delete("1.0","end")
        

        
#end onClear
clearButton = Button(innerFrame, text = "Clear", command = onClearF)
clearButton.grid(row = 6, column = 2 )
'''clearButton.color("red")'''
 


def onResetF():
        #stop the drawing 
        screen.tracer(0)
        pen.up()
        pen.goto(0,50)
#on reset
resetButton = Button(innerFrame, text = "Stop", command = onResetF)
resetButton.grid(row = 6, column =1)



#make the Optionmenu dropdown list
figureList = ["Tree", "Dandeloin", "Fern", "Snowflake",  "Antisnowflake", "Gasket",  "Square  Gasket", "Andrew's Coss", "Flower", "Linear Circle" ]
figureStr = StringVar()
figureOptionMenu = OptionMenu(controlFrame, figureStr, figureList[0], *figureList)
figureOptionMenu.grid(row = 0, column =  1)
 

#make the Colormenu dropdown list
penList = ['Purple', "Blue", "Green", "Yellow", "Orange", "Pink", "Red", "Black", "White"]
penStr = StringVar()
penOptionMenu = OptionMenu(controlFrame, penStr, penList[0], *penList)
penOptionMenu.grid(row = 3, column =  1)



def onDrawF():
        screen.tracer(1)
        #get the order and length
        order =   int(orderStr.get())
        length = int(lengthStr.get())

        #what is the figure to draw
        figure = figureStr.get()
        figureID = figureList.index(figure)
       # tracer()
        #what is pen speed / thickness
        pen.pensize(penSize.get())
        pen.speed(penSpeed.get())

        
         #what is pen color
        '''changePenColor():'''
        print(penStr.get())
        pen.color(penStr.get())
        

        #check what to draw
        if figureID == 0: #draw the binary tree
                pen.up()
                pen.goto(80,45)
                pen.backward(w/2)
                pen.down()
                turtlefigures.tree(order, length, pen)
                text.insert(END, "You have sucessfully drawn the binary tree")
        elif figureID == 1: #draw the dandeloin
                pen.up()
                pen.goto(80,80)
                pen.backward(w/2)
                pen.down()
                turtlefigures.tree4(order, length, pen)
                text.insert(END, "You have sucessfully drawn the Dandeloin")
        elif figureID == 2: #draw the fern
                pen.up()
                pen.goto(80,80)
                pen.backward(w/2)
                pen.down()
                turtlefigures.fern(order, length, pen)
                text.insert(END, "You have sucessfully drawn the fern")
        elif figureID == 3: #draw the flake
                pen.up()
                pen.goto(80,80)
                pen.backward(w/2)
                pen.down()
                turtlefigures.flake(order, length, pen)
                text.insert(END, "You have sucessfully drawn the Flake")
        elif figureID == 4: #draw the Antiflake
                pen.up()
                pen.goto(80,80)
                pen.backward(w/2)
                pen.down()
                turtlefigures.flake2(order, length, pen)
                text.insert("You have sucessfully drawn the AntiFlake")
        elif figureID == 5: #draw the gasket
                pen.up()
                pen.goto(80,80)
                pen.backward(w/2)
                pen.down()
                turtlefigures.gasket(order, length, pen)
                text.insert("You have sucessfully drawn the Gasket")
        elif figureID == 5: #draw the square gasket
                pen.up()
                pen.backward(w/2)
                pen.down()
                turtlefigures.sqgasket(order, length, pen)
                text.insert(END, "You have sucessfully drawn the Square Gasket")
        elif figureID == 7: #draw Andrews Cross
                pen.up()
                pen.goto(80,80)
                pen.backward(w/2)
                pen.down()
                turtlefigures.cross(order, length, pen)
                text.insert(END, "You have sucessfully drawn Andrews Cross")
        elif figureID == 8: #draw flower
                pen.up()
                pen.goto(80, 100)
                pen.backward(w/2)
                pen.down()
                turtlefigures.flower(order, length, pen)
                text.insert(END, "You have sucessfully drawn a Flower")
   
            

#end onDrawF
drawButton = Button(innerFrame, text = "Draw", command = onDrawF)
drawButton.grid(row = 6, column = 0)

       
root.mainloop()



