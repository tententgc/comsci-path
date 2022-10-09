from tkinter import *

mywin=Tk()
mywin.title("จำหน่ายอาหารสัตว์")
mywin.minsize(500,500)
lb=Label(mywin,text='Menu')
lb.pack(pady=5)

products={"101":{"title":"Dog Food","price":20},
          "102":{"title":"Cat Food","price":20},
          "103":{"title":"Rarrit Food","price":15},
          "104":{"title":"Hamster Food","price":10},
          "105":{"title":"Bird Food","price":20},
          "106":{"title":"House Food","price":25},
          "107":{"title":"Goat Food","price":25},
          "108":{"title":"Fish Food","price":20},
          "109":{"title":"Snake Food","price":40},
          "110":{"title":"Squirrel Food","price":10},
          "111":{"title":"Chicken Food","price":15},
          "112":{"title":"Pig Food","price":20},
          "113":{"title":"Cow Food","price":20},
          "114":{"title":"Duck Food","price":20},
          "115":{"title":"Frog Food","price":30},
        }

for key in products:
    title=products[key]["title"]
    price=products[key]["price"]
    lb2=Label(mywin,text=("{:3} {:20} {:2}".format(key,title,price)))
    lb2.pack()

#page2   
def openwindow2():
    def convert(myinput,myinput2):
        input_a = str(myinput2)
        key = myinput
        #print(myinput2.get())

        if  key=="101":
            price=20
            total=price*input_a
            display.set('จำนวน{}ถุง ราคาทั้งหมด{}บาท'.format(input_a,total))
        elif key==102:
            price=20
            total=price*input_a
            display.set('จำนวน{}ถุง ราคาทั้งหมด{}บาท'.format(input_a,total))
        elif key==103:
            price=15
            total=price*input_a
            display.set('จำนวน{}ถุง ราคาทั้งหมด{}บาท'.format(input_a,total))
        elif key==104:
            price=10
            total=price*input_a
            display.set('จำนวน{}ถุง ราคาทั้งหมด{}บาท'.format(input_a,total))
        elif key==105:
            price=20
            total=price*input_a
            display.set('จำนวน{}ถุง ราคาทั้งหมด{}บาท'.format(input_a,total))
        elif key==106:
            price=25
            total=price*input_a
            display.set('จำนวน{}ถุง ราคาทั้งหมด{}บาท'.format(input_a,total))
        elif key==107:
            price=25
            total=price*input_a
            display.set('จำนวน{}ถุง ราคาทั้งหมด{}บาท'.format(input_a,total))
        elif key==108:
            price=20
            total=price*input_a
            display.set('จำนวน{}ถุง ราคาทั้งหมด{}บาท'.format(input_a,total))
        elif key==109:
            price=40
            total=price*input_a
            display.set('จำนวน{}ถุง ราคาทั้งหมด{}บาท'.format(input_a,total))
        elif key==110:
            price=10
            total=price*input_a
            display.set('จำนวน{}ถุง ราคาทั้งหมด{}บาท'.format(input_a,total))
        elif key==111:
            price=15
            total=price*input_a
            display.set('จำนวน{}ถุง ราคาทั้งหมด{}บาท'.format(input_a,total))
        elif key==112:
            price=20
            total=price*input_a
            display.set('จำนวน{}ถุง ราคาทั้งหมด{}บาท'.format(input_a,total))
        elif key==113:
            price=20
            total=price*input_a
            display.set('จำนวน{}ถุง ราคาทั้งหมด{}บาท'.format(input_a,total))
        elif key==114:
            price=20
            total=price*input_a
            display.set('จำนวน{}ถุง ราคาทั้งหมด{}บาท'.format(input_a,total))
        elif key==115:
            price=30
            total=price*input_a
            display.set('จำนวน{}ถุง ราคาทั้งหมด{}บาท'.format(input_a,total))

    mywindow=Tk()
    mywindow.title("คำนวนราคา")
    mywindow.minsize(500,500)


    myinput=StringVar()
    lb3=Label(mywindow,text="รหัสสินค้า").pack(pady=10)
    ent=Entry(mywindow,textvariable=myinput)
    myinput.get()
    ent.pack()
    ent.focus()
    
    myinput2=StringVar()
    lb4=Label(mywindow,text="จำนวนสินค้า").pack(pady=10)
    ent2=Entry(mywindow,textvariable=myinput2)
    myinput2.get()
    ent2.pack()
    ent2.focus()
    display=StringVar()

    

    btok=Button(mywindow,text="OK",width=10,command=lambda: convert('101',2))
    btok.pack(pady=10)  

    lb5=Label(mywindow,textvariable=display)
    lb5.pack()


btnext=Button(mywin,text="Next",width=10,command=openwindow2,fg='white',bg='yellow',pady=2)
btnext.pack(pady=10)
label = mywin.Label(
    text="Hello, Tkinter",
    foreground="white",  # Set the text color to white
    background="black"  # Set the background color to black)
    )
mywin.mainloop()