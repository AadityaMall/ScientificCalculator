#IMPORTING MODULES

from os import replace #REPLACE

from tkinter import * #GUI

from tkinter import messagebox #MESSAGE BOXES

import math as m #MATHS MODULE

import threading #THREADING

import pyttsx3#AUDIO

from audio_helper import PlayAudio #FUNCTION FROM MY MODULE
 
import speech_recognition as sr #SPEECH RECOGNITION

#Creating root window
root = Tk()
root.iconbitmap('IMAGES/favicon.ico')
root.title("Calculator")
root.geometry("462x520")

#CREATING FONTS
font = ('calibri',18, 'bold')
font1 = ('calibri',22, 'bold')


#DECLARING VARIABLES
degree =  True
radianmode = False
ob = PlayAudio()
audiocalc_system = False
normalcalc = True
scificalc_system =  False
voiceoperatedcalc = False

#CREATIING FUNCTIONS

#AUDIO CALCULATOR SWITCHER
def audiocalc():
    global normalcalc
    global audiocalc_system
    if normalcalc:
        audiocalc_system = True
        normalcalc = False
    else:
        audiocalc_system = False
        normalcalc = True

# SCIFI CALCULATOR SWITCHER
def scificalc():
    global normalcalc
    global scificalc_system
    global voiceoperatedcalc

    if voiceoperatedcalc == True:
        root.geometry("462x520")
        mainbox['width']= 30
        mybutton.grid_forget()
        voiceoperatedcalc = False


    if scificalc_system == False:
        scifi_frame.grid(row=1,column=1)
        root.geometry("688x502")
        mainbox['width']= 45
        scificalc_system =  True
        
    else:
        scifi_frame.grid_forget()
        root.geometry("463x505")
        mainbox['width']= 30
        scificalc_system =  False

# VOICE OPERATED CALCULATOR SWITCHER
def voiceoperated_calc():
    global voiceoperatedcalc
    global scificalc_system
    global audiocalc_system
    
    if scificalc_system == True:
        scifi_frame.grid_forget()
        root.geometry("463x505")
        mainbox['width']= 30
        scificalc_system =  False
    
    if voiceoperatedcalc == False:

        mybutton.grid(row=1,column=1)
        root.geometry("732x502")
        mainbox['width']= 48
        voiceoperatedcalc =  True    
        
    elif voiceoperatedcalc == True:
         root.geometry("462x520")
         mainbox['width']= 30
         mybutton.grid_forget()
         voiceoperatedcalc = False

# VOICE OPERATED CALC FUNCTIONING
def voiceoperated_calc_click():
    mainbox.delete(0,END)
    listener = sr.Recognizer()
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice',voices[1].id)
    try:
        with sr.Microphone() as source:
                print('Speak Noww!!!!')
                voice = listener.listen(source)
                command =  listener.recognize_google(voice)
                print(command)

                engine = pyttsx3.init()
                engine.say(command)
                engine.runAndWait()

                if 'what is' in command:
                    command = command.replace('what is','')

                if 'into'  in command:
                    command = command.replace('into','*')
                elif 'x'  in command:
                    command = command.replace('x','*')
                elif 'X'  in command:
                    command = command.replace('X','*')               
                
                
                if 'sin' in command:
                    command=command.replace('sin','')
                    torad = m.radians(float(command))
                    answer = m.sin(float(torad))
                    engine.say("is equal to, {0}".format(answer))
                    engine.runAndWait()
                    mainbox.delete(0, END)
                    mainbox.insert(END, answer)
                    return

                elif 'tan' in command:
                    command=command.replace('tan','')
                    torad = m.radians(float(command))
                    answer = m.tan(float(torad))
                    engine.say("is equal to, {0}".format(answer))
                    engine.runAndWait()
                    mainbox.delete(0, END)
                    mainbox.insert(END, answer)
                    return
                
                elif 'Cos' in command:
                    command=command.replace('Cos','')
                    torad = m.radians(float(command))
                    answer = m.cos(float(torad))
                    engine.say("is equal to, {0}".format(answer))
                    engine.runAndWait()
                    mainbox.delete(0, END)
                    mainbox.insert(END, answer)
                    return

                elif 'power' in command:
                    base,power = command.split('power')
                    answer = m.pow(int(base),int(power))
                    engine.say("is equal to, {0}".format(answer))
                    engine.runAndWait()
                    mainbox.delete(0, END)
                    mainbox.insert(END, answer)
                    return

                elif 'under root' in command:
                    command=command.replace('under root','')
                    answer = m.pow(float(command),0.5)
                    engine.say("is equal to, {0}".format(answer))
                    engine.runAndWait()
                    mainbox.delete(0, END)
                    mainbox.insert(END, answer)
                    return

                elif 'cube root' in command:
                    command=command.replace('cube root','')
                    answer = m.pow(float(command),(1/3))
                    engine.say("is equal to, {0}".format(answer))
                    engine.runAndWait()
                    mainbox.delete(0, END)
                    mainbox.insert(END, answer)
                    return
                
                elif 'factorial' in command:
                    command=command.replace('factorial','')
                    answer = m.factorial(int(command))
                    engine.say("is equal to, {0}".format(answer))
                    engine.runAndWait()
                    mainbox.delete(0, END)
                    mainbox.insert(END, answer)
                    return                

                elif 'combinations' in command:
                    n,r = command.split('combinations')
                    answer = m.comb(int(n),int(r))
                    engine.say("is equal to, {0}".format(answer))
                    engine.runAndWait()
                    mainbox.delete(0, END)
                    mainbox.insert(END, answer)
                    return

                elif 'p' in command:
                    n,r = command.split('p')
                    answer = m.perm(int(n),int(r))
                    engine.say("is equal to, {0}".format(answer))
                    engine.runAndWait()
                    mainbox.delete(0, END)
                    mainbox.insert(END, answer)
                    return

                elif '% of' in command:
                    percent,value = command.split('% of')
                    answer = (int(percent)/100)*float(value)
                    engine.say("is equal to, {0}".format(answer))
                    engine.runAndWait()
                    mainbox.delete(0, END)
                    mainbox.insert(END, answer)
                    return

                elif 'Radian to degree' in command:
                    command=command.replace('Radian to degree','')
                    answer = m.degrees(int(command))
                    engine.say("is equal to, {0}".format(answer))
                    engine.runAndWait()
                    mainbox.delete(0, END)
                    mainbox.insert(END, answer)
                    return                  

                elif 'degree to radian' in command:
                    command=command.replace('degree to radian','')
                    answer = m.radians(int(command))
                    engine.say("is equal to, {0}".format(answer))
                    engine.runAndWait()
                    mainbox.delete(0, END)
                    mainbox.insert(END, answer)
                    return                  
                
    except:
        pass

    mainbox.insert(0,command)
    try:
        answer = eval(mainbox.get())
        engine.say("is equal to, {0}".format(answer))
        engine.runAndWait()
        mainbox.delete(0, END)
        mainbox.insert(END, answer)
        
    except:
        messagebox.showerror('Calculator', 'Invalid Input')
        mainbox.delete(0, END)


    
# SWITCHING RADIAN TO DEGREE MODE
def torad_todeg(x):
    global degree
    global radianmode
    a = x.widget
    text = a['text']

    if text == "DEG":

        button_todeg.grid_forget()
        button_torad.grid(row=5,column=0)
        engine =  pyttsx3.init()
        engine.say('Radian Mode Calculator')
        engine.runAndWait()
        degree = False
        radianmode = True
        return
    elif text == "RAD":

        button_torad.grid_forget()
        button_todeg.grid(row=5,column=0)
        engine =  pyttsx3.init()
        engine.say('Degree Mode Calculator')
        engine.runAndWait()
        radianmode = False
        degree = True
        return
    mainbox.insert(0,text)

# FUNCTION OF NORMAL BUTTON CLICK
def button_clicked(x):
    #EXTRACTING THE BUTTOM TEXT
    b = x.widget
    text = b['text']

    if audiocalc_system == True:

        if text != '=':
            t= threading.Thread(target=ob.speak,args=(text))
            t.start()
        else:
            pass        

    #RUNNING THE OPERATION WHEN = CLICKED
    if text == "=": 

        #ERROR HANDLING
        try:
            #STROING EVALUATED ANSWER INSIDE VARIABLE 
            answer = eval(mainbox.get())
            mainbox.delete(0, END)
            mainbox.insert(END, answer)

            if audiocalc_system == True:
                engine =  pyttsx3.init()
                engine.say('equals, {0}'.format(answer))
                engine.runAndWait()
            else:
                pass

            return
        except:
            messagebox.showerror('Calculator', 'Invalid Input')
            mainbox.delete(0, END)
            return

    if text == "x":
        #INPUTING * INSTEAD OF X FOR MULTIPLICATION
        mainbox.insert(END,'*')
        return

    if text == "÷":
        #USING / INSTEAD OF ÷ FOR DIVISION
        mainbox.insert(END,'/')
        return
    
    if text == "DEL":
        ex = mainbox.get()
        ex = ex[0:len(ex)-1]
        mainbox.delete(0,END)
        mainbox.insert(END,ex)
        return

    else:
        pass
    mainbox.insert(END,text)

#FUNCTION  FOR SCIENTIFIC CALCULATIONS
def scifi_click(x):

    global degree
    a = x.widget
    text = a['text']
    ex = mainbox.get()
    answer = ''

    if ex == "":
        messagebox.showerror('Error','Field Blank')
        return
    else:
        pass

    if text == "√x":
        answer = str(m.sqrt(float(ex)))
        mainbox.delete(0,END)
        mainbox.insert(0,answer)
        if audiocalc_system == True:
            engine = pyttsx3.init()
            engine.say('Under root of {0} is equal to, {1}'.format(ex,answer))
            engine.runAndWait()    
        return

    elif text == "x^":
      try:
        base,power = ex.split(',')
        answer = str(m.pow(float(base),float(power)))
        mainbox.delete(0,END)
        mainbox.insert(0,answer)
        if audiocalc_system == True:
            engine = pyttsx3.init()
            engine.say(' {0} to the power {1} is {2}'.format(base,power,answer))  
            engine.runAndWait()    
        return  
      except:
        messagebox.showerror('Error','PUT IN "Base,Power" format')
        mainbox.delete(0,END-1)
        
    elif text == "nCr":
      try:
        n,r = ex.split(',')
        answer = str(m.comb(int(n),int(r)))
        mainbox.delete(0,END)
        mainbox.insert(0,answer)
        if audiocalc_system == True:
            engine = pyttsx3.init()
            engine.say(' {0}, C , {1} is {2}'.format(n,r,answer))  
            engine.runAndWait() 
        return   
      except:
            messagebox.showerror('Error','PUT IN "n,r" format')
            mainbox.delete(0,END-1)

    elif text == "nPr":
      try:
        n,r = ex.split(',')
        answer = str(m.perm(int(n),int(r)))
        mainbox.delete(0,END)
        mainbox.insert(0,answer)
        if audiocalc_system == True:
            engine = pyttsx3.init()
            engine.say(' {0}, P , {1} is {2}'.format(n,r,answer))  
            engine.runAndWait() 
        return  
      except:
        messagebox.showerror('Error','PUT IN "n,r" format')
        mainbox.delete(0,END-1)

    elif text=="x!":

            answer = str(m.factorial(int(ex)))
            mainbox.delete(0,END)
            mainbox.insert(0,answer)
            if audiocalc_system == True:
                engine = pyttsx3.init()
                engine.say('Factorial of {0} is equal to, {1}'.format(ex,answer))
                engine.runAndWait() 
            return

    elif text == "TANθ":
        try:
            if degree :
                torad = str(m.radians(float(ex)))
                answer = str(m.tan(float(torad)))
                mainbox.delete(0,END)
                mainbox.insert(0,answer)
                if audiocalc_system == True:
                    engine = pyttsx3.init()
                    engine.say('Tan {0} is equal to, {1}'.format(ex,answer))
                    engine.runAndWait()
                return

            elif radianmode:
                answer = str(m.tan(float(ex)))
                mainbox.delete(0,END)
                mainbox.insert(0,answer)
                if audiocalc_system == True:
                    engine = pyttsx3.init()
                    engine.say('Tan {0} is equal to, {1}'.format(ex,answer))
                    engine.runAndWait()
                return

            return
        except:
            pass

      
    elif text == "SINθ":
        try:
            if degree :
                torad = str(m.radians(float(ex)))
                answer = str(m.sin(float(torad)))
                mainbox.delete(0,END)
                mainbox.insert(0,answer)
                if audiocalc_system ==  True:
                    engine = pyttsx3.init()
                    engine.say('Sin {0} is equal to, {1}'.format(ex,answer))
                    engine.runAndWait()
                return

            elif radianmode:
                answer = str(m.sin(float(ex)))
                mainbox.delete(0,END)
                mainbox.insert(0,answer)
                if audiocalc_system ==  True:
                    engine = pyttsx3.init()
                    engine.say('Sin {0} is equal to, {1}'.format(ex,answer))
                    engine.runAndWait()
                return
            return
        except:
            pass

    elif text == "COSθ":
        try:
            if degree :
                torad = str(m.radians(float(ex)))
                answer = str(m.cos(float(torad)))
                mainbox.delete(0,END)
                mainbox.insert(0,answer)
                if audiocalc_system ==  True:
                    engine = pyttsx3.init()
                    engine.say('Cos {0} is equal to, {1}'.format(ex,answer))
                    engine.runAndWait()
                return

            elif radianmode:
                answer = str(m.cos(float(ex)))
                mainbox.delete(0,END)
                mainbox.insert(0,answer)
                if audiocalc_system ==  True:
                    engine = pyttsx3.init()
                    engine.say('cos {0} is equal to, {1}'.format(ex,answer))
                    engine.runAndWait()
                return
            return
        except:
            pass

    elif text== "3√":
        answer = str(m.pow(float(ex),(1/3)))
        mainbox.delete(0,END)
        mainbox.insert(0,answer)
        if audiocalc_system ==  True:
            engine = pyttsx3.init()
            engine.say('cube root of {0} is equal to, {1}'.format(ex,answer))
            engine.runAndWait()
        return
    if text == "%":
      try:
        ex = mainbox.get()
        percent,value = ex.split(',')
        answer = str((float(percent)/100)*float(value))
        mainbox.delete(0,END)
        mainbox.insert(0,answer)
        if audiocalc_system ==  True:
            engine = pyttsx3.init()
            engine.say('{0} percent of {1} is equal to {2}'.format(percent,value,answer))
            engine.runAndWait()
        return  
      except:
        messagebox.showerror('Error','PUT IN "percent,value" format')
        mainbox.delete(0,END-1)    


    else:
        pass
    
    mainbox.insert(END,text)

#FUNCTION FOR CLEAR BUTTON
def clear():
    mainbox.delete(0,END)

#CREATING FUNCTION TO EVALUATE ANSWER WHEN ENTER KEY IS PRESSED
def enterbutton(x):
    e = Event()
    e.widget = button_e
    button_clicked(e)

#CEATING MENU BAR
my_menu = Menu(root)
root.config(menu=my_menu)
mode = Menu(my_menu , tearoff= 0) 
my_menu.add_cascade(label= "Mode" , menu=mode)
mode.add_cascade(label="Scientific Calculator", command=scificalc , font=('', 16))
mode.add_checkbutton(label="Audio Calculator", command=audiocalc , font=('', 16))
mode.add_cascade(label="Voice Operated Calculator", command=voiceoperated_calc , font=('', 16))


#MAKING THE MAIN BOX   
mainbox = Entry(root,width=30, borderwidth= 5 , justify=RIGHT ,font=font1, bg="#F8F9F9")
mainbox.grid(row=0,column=0, pady= 20, ipady=5,columnspan=2 )

#CREATING FRAMES
buttonframe = Frame(root, bg="grey")
buttonframe.grid(row=1,column=0)

scifi_frame = Frame(root, bg="grey")

#CREATIN AND STYLING BUTTONS
button_1 = Button(buttonframe , text="1",width=8 , height=2, bg="#D7F4E8", relief='raised',font=font)
button_2 = Button(buttonframe , text="2",width=8 , height=2, bg="#D7F4E8", relief='raised',font=font)
button_3 = Button(buttonframe , text="3",width=8 , height=2, bg="#D7F4E8", relief='raised',font=font)
button_4 = Button(buttonframe , text="4",width=8 , height=2, bg="#D7F4E8", relief='raised',font=font)
button_5 = Button(buttonframe , text="5",width=8 , height=2, bg="#D7F4E8", relief='raised',font=font)
button_6 = Button(buttonframe , text="6",width=8 , height=2, bg="#D7F4E8", relief='raised',font=font)
button_7 = Button(buttonframe , text="7",width=8 , height=2, bg="#D7F4E8", relief='raised',font=font)
button_8 = Button(buttonframe , text="8",width=8 , height=2, bg="#D7F4E8", relief='raised',font=font)
button_9 = Button(buttonframe , text="9",width=8 , height=2, bg="#D7F4E8", relief='raised',font=font)
button_0 = Button(buttonframe , text="0",width=8 , height=2, bg="#D7F4E8", relief='raised',font=font)

button_comma = Button(buttonframe , text=",",width=8 , height=2, bg="#D7F4E8", relief='raised',font=font)
button_dot = Button(buttonframe , text=".",width=8 , height=2, bg="#D7F4E8", relief='raised',font=font)
button_d = Button(buttonframe , text="÷",width=8 , height=2, bg="#E6B0AA", relief='raised',font=font)
button_m = Button(buttonframe , text="x",width=8 , height=2, bg="#E6B0AA", relief='raised',font=font)
button_a = Button(buttonframe , text="+",width=8 , height=2, bg="#E6B0AA", relief='raised',font=font)
button_s = Button(buttonframe , text="-",width=8 , height=2, bg="#E6B0AA", relief='raised',font=font)
button_e = Button(buttonframe , text="=",width=8 , height=2, bg="#D7F4E8", relief='raised',font=font)
button_c = Button(buttonframe , text="C",width=8 , height=2, bg="#D7F4E8", relief='raised',command= clear,font=font)
button_percentage = Button(buttonframe , text="%",width=8 , height=2, bg="#E6B0AA", relief='raised',font=font)
button_del = Button(buttonframe , text="DEL",width=8, height=2, bg="#D7F4E8", relief='raised',font=font)

button_squareroot = Button(scifi_frame , text="√x",width=8 , height=2, bg="#E6B0AA", relief='raised',font=font) 
button_power = Button(scifi_frame , text="x^",width=8 , height=2, bg="#E6B0AA", relief='raised',font=font)
button_factorial = Button(scifi_frame , text="x!",width=8 , height=2, bg="#E6B0AA", relief='raised',font=font)
button_combination= Button(scifi_frame , text="nCr",width=8 , height=2, bg="#E6B0AA", relief='raised',font=font)
button_permutation= Button(scifi_frame , text="nPr",width=8 , height=2, bg="#E6B0AA", relief='raised',font=font)
button_sin= Button(scifi_frame , text="SINθ",width=8 , height=2, bg="#E6B0AA", relief='raised',font=font)
button_cos= Button(scifi_frame , text="COSθ",width=8 , height=2, bg="#E6B0AA", relief='raised',font=font)
button_tan= Button(scifi_frame , text="TANθ",width=8 , height=2, bg="#E6B0AA", relief='raised',font=font)
button_torad= Button(scifi_frame , text="RAD",width=8 , height=2, bg="#E6B0AA", relief='raised',font=font)
button_todeg= Button(scifi_frame , text="DEG",width=8 , height=2, bg="#E6B0AA", relief='raised',font=font)
button_cuberoot= Button(scifi_frame , text="3√",width=8 , height=2, bg="#E6B0AA", relief='raised',font=font) 

myimg = PhotoImage(file='IMAGES/Microphone-Transparent-Images.png')
mybutton = Button(root, image=myimg, borderwidth=10,command=voiceoperated_calc_click , bg="#E6B0AA")

#PLACING BUTTONS ON SCREEN
button_9.grid(row=1, column= 2)
button_8.grid(row=1, column= 1)
button_7.grid(row=1, column= 0)

button_6.grid(row=2, column= 2)
button_5.grid(row=2, column= 1)
button_4.grid(row=2, column= 0)

button_3.grid(row=3, column= 2)
button_2.grid(row=3, column= 1)
button_1.grid(row=3, column= 0)

button_0.grid(row=4, column= 1)

button_percentage.grid(row=1,column=4)
button_m.grid(row=2,column= 4)
button_a.grid(row=3,column= 4)
button_s.grid(row=4,column= 4)
button_dot.grid(row=4,column= 0)
button_c.grid(row=5,column= 0)
button_d.grid(row=5,column= 4)
button_e.grid(row=4,column=2)
button_del.grid(row=5,column=1)
button_comma.grid(row=5,column=2)


button_squareroot.grid(row=1,column=0)
button_power.grid(row=2,column=0)
button_factorial.grid(row=3,column=0)
button_combination.grid(row=4,column=0)
button_permutation.grid(row=4,column=1)
button_sin.grid(row=1,column=1)
button_cos.grid(row=2,column=1)
button_tan.grid(row=3,column=1)
button_todeg.grid(row=5,column=0)
button_cuberoot.grid(row=5,column=1)

#BINDING BUTTONS TO THEIR RESPECTIVE FUNCTIONS ON RIGHT CLICK
button_9.bind('<Button-1>' , button_clicked)
button_8.bind('<Button-1>' , button_clicked)
button_7.bind('<Button-1>' , button_clicked)
button_6.bind('<Button-1>' , button_clicked)
button_5.bind('<Button-1>' , button_clicked)
button_4.bind('<Button-1>' , button_clicked)
button_3.bind('<Button-1>' , button_clicked)
button_2.bind('<Button-1>' , button_clicked)
button_1.bind('<Button-1>' , button_clicked)
button_0.bind('<Button-1>' , button_clicked)
button_m.bind('<Button-1>' , button_clicked)
button_a.bind('<Button-1>' , button_clicked)
button_s.bind('<Button-1>' , button_clicked)
button_e.bind('<Button-1>' , button_clicked)
button_d.bind('<Button-1>' , button_clicked)
button_dot.bind('<Button-1>',button_clicked)
button_del.bind('<Button-1>',button_clicked)
button_comma.bind('<Button-1>',button_clicked)

button_percentage.bind('<Button-1>',scifi_click)
button_squareroot.bind('<Button-1>',scifi_click)
button_power.bind('<Button-1>' , scifi_click)
button_permutation.bind('<Button-1>', scifi_click)
button_tan.bind('<Button-1>',scifi_click)
button_cos.bind('<Button-1>',scifi_click)
button_sin.bind('<Button-1>' ,scifi_click)
button_factorial.bind('<Button-1>',scifi_click)
button_combination.bind('<Button-1>',scifi_click)
button_cuberoot.bind('<Button-1>',scifi_click)

button_todeg.bind('<Button-1>',torad_todeg)
button_torad.bind('<Button-1>',torad_todeg)

mainbox.bind('<Return>', enterbutton)

#RUNNING THE WINDOW
root.mainloop()

