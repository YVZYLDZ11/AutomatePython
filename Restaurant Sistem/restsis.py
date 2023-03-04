import time
import datetime
import random
from tkinter import *
from tkinter import messagebox


root = Tk()
root.geometry("1366x768")
root.title("Restaurant Management System")
root.configure(background = "#212F3C")

Tops = Frame(root, bg="#212F3C", bd=20, pady=5, relief=FLAT)
Tops.pack(side=TOP)
lblTitle = Label(Tops,font=("times", 60, "bold"), text="Restaurant Management System", bd=20, bg="#212F3C", fg="white", justify=CENTER)
lblTitle.grid(row=0, column=0)


ReceiptCal_F = Frame(root, bg="#212F3C", bd=10, relief=RIDGE)
ReceiptCal_F.pack(side=LEFT)
Buttons_F = Frame(ReceiptCal_F, bg="#212F3C", bd=2, relief=RIDGE)
Buttons_F.pack(side=TOP)
Cal_F = Frame(ReceiptCal_F, bg="#212F3C", bd=4, relief=RIDGE)
Cal_F.pack(side=BOTTOM)
Receipt_F = Frame(ReceiptCal_F, bg="#212F3C", bd=3, relief=RIDGE)
Receipt_F.pack(side=TOP)

MenuFrame = Frame(root, bg="#212F3C", bd=10, relief=RIDGE)
MenuFrame.pack(side=RIGHT)
Cost_F = Frame(MenuFrame, bg="#212F3C", bd=4)
Cost_F.pack(side=BOTTOM)

Drinks_F = Frame(MenuFrame, bg="#212F3C", bd=10, relief=RIDGE)
Drinks_F.pack(side=LEFT)
Snacks_F = Frame(MenuFrame, bg="#212F3C", bd=10, relief=RIDGE)
Snacks_F.pack(side=LEFT)
Food_F = Frame(MenuFrame, bg="#212F3C", bd=10, relief=RIDGE)
Food_F.pack(side=RIGHT)

"""Variables"""
var1=IntVar()
var2=IntVar()
var3=IntVar()
var4=IntVar()
var5=IntVar()
var6=IntVar()
var7=IntVar()
var8=IntVar()
var9=IntVar()
var10=IntVar()
var11=IntVar()
var12=IntVar()
var13=IntVar()
var14=IntVar()
var15=IntVar()
var16=IntVar()
var17=IntVar()
var18=IntVar()
var19=IntVar()
var20=IntVar()
var21=IntVar()
var22=IntVar()
var23=IntVar()
var24=IntVar()

DateOfOrder=StringVar()
Receipt_Ref=StringVar()
PaidTax=StringVar()
SubTotal=StringVar()
TotalCost=StringVar()
CostofFoods=StringVar()
CostofDrinks=StringVar()
CostofSnacks=StringVar()
ServiceCharge =StringVar()

text_Input=StringVar()
operator=""

E_Tea=StringVar()
E_Coke=StringVar()
E_Water=StringVar()
E_Ayran=StringVar()
E_Lemonade=StringVar()
E_Soda_Water=StringVar()
E_Orange_Juice=StringVar()
E_Turkish_Coffee=StringVar()

E_Roll=StringVar()
E_Soup=StringVar()
E_Rice=StringVar()
E_Fries=StringVar()
E_Salad=StringVar()
E_Noodle=StringVar()
E_Yogurt=StringVar()
E_Chesee_Chips=StringVar()

E_Hamburger=StringVar()
E_Spaghetti=StringVar()
E_Chef_Salad=StringVar()
E_Beef_Steak=StringVar()
E_Onion_Rings=StringVar()
E_CheeseBurger=StringVar()
E_ChickenSteak=StringVar()
E_Old_Italia_Pizza=StringVar()

E_Tea.set("0")
E_Coke.set("0")
E_Water.set("0")
E_Ayran.set("0")
E_Lemonade.set("0")
E_Soda_Water.set("0")
E_Orange_Juice.set("0")
E_Turkish_Coffee.set("0")

E_Roll.set("0")
E_Soup.set("0")
E_Rice.set("0")
E_Fries.set("0")
E_Salad.set("0")
E_Noodle.set("0")
E_Yogurt.set("0")
E_Chesee_Chips.set("0")

E_Hamburger.set("0")
E_Spaghetti.set("0")
E_Chef_Salad.set("0")
E_Beef_Steak.set("0")
E_Onion_Rings.set("0")
E_CheeseBurger.set("0")
E_ChickenSteak.set("0")
E_Old_Italia_Pizza.set("0")

DateOfOrder.set(time.strftime("%d/%m/%Y"))


"""Function Declarations"""
def iExit():
    iExit=messagebox.askyesno("Exit Restaurant System", "Confirm if you want to exit")
    if iExit >0:
        root.destroy()
        return

def Reset():
    PaidTax.set("")
    SubTotal.set("")
    TotalCost.set("")
    CostofFoods.set("")
    CostofDrinks.set("")
    CostofSnacks.set("")
    ServiceCharge.set("")
    txtReceipt.delete("1.0", END)

    E_Tea.set("0")
    E_Coke.set("0")
    E_Water.set("0")
    E_Ayran.set("0")
    E_Lemonade.set("0")
    E_Soda_Water.set("0")
    E_Orange_Juice.set("0")
    E_Turkish_Coffee.set("0")
    
    E_Roll.set("0")
    E_Soup.set("0")
    E_Rice.set("0")
    E_Fries.set("0")
    E_Salad.set("0")
    E_Noodle.set("0")
    E_Yogurt.set("0")
    E_Chesee_Chips.set("0")

    E_Hamburger.set("0")
    E_Spaghetti.set("0")
    E_Chef_Salad.set("0")
    E_Beef_Steak.set("0")
    E_Onion_Rings.set("0")
    E_CheeseBurger.set("0")
    E_ChickenSteak.set("0")
    E_Old_Italia_Pizza.set("0")

    var1.set(0)
    var2.set(0)
    var3.set(0)
    var4.set(0)
    var5.set(0)
    var6.set(0)
    var7.set(0)
    var8.set(0)
    var9.set(0)
    var10.set(0)
    var11.set(0)
    var12.set(0)
    var13.set(0)
    var14.set(0)
    var15.set(0)
    var16.set(0)
    var17.set(0)
    var18.set(0)
    var19.set(0)
    var20.set(0)
    var21.set(0)
    var22.set(0)
    var23.set(0)
    var24.set(0)

    txtTea.configure(state=DISABLED)
    txtCoke.configure(state=DISABLED)
    txtWater.configure(state=DISABLED)
    txtAyran.configure(state=DISABLED)
    txtLemonade.configure(state=DISABLED)
    txtSoda_Water.configure(state=DISABLED)
    txtOrangeJuice.configure(state=DISABLED)
    txtTurkish_Coffee.configure(state=DISABLED)
    txtRoll.configure(state=DISABLED)
    txtSoup.configure(state=DISABLED)
    txtRice.configure(state=DISABLED)
    txtFries.configure(state=DISABLED)
    txtSalad.configure(state=DISABLED)
    txtNoodle.configure(state=DISABLED)
    txtYogurt.configure(state=DISABLED)
    txtChesee_Chips.configure(state=DISABLED)
    txtHamburger.configure(state=DISABLED)
    txtSpaghetti.configure(state=DISABLED)
    txtChef_Salad.configure(state=DISABLED)
    txtBeef_Steak.configure(state=DISABLED)
    txtOnion_Rings.configure(state=DISABLED)
    txtCheeseburger.configure(state=DISABLED)
    txtChicken_Steak.configure(state=DISABLED)
    txtOld_Italia_Pizza.configure(state=DISABLED)

def CostofItem():
    Item1 = float(E_Tea.get())
    Item2 = float(E_Coke.get())
    Item3 = float(E_Water.get())
    Item4 = float(E_Ayran.get())
    Item5 = float(E_Lemonade.get())
    Item6 = float(E_Soda_Water.get())
    Item7 = float(E_Orange_Juice.get())
    Item8 = float(E_Turkish_Coffee.get())
    Item9 = float(E_Roll.get())
    Item10 = float(E_Soup.get())
    Item11 = float(E_Rice.get())
    Item12 = float(E_Fries.get())
    Item13 = float(E_Salad.get())
    Item14 = float(E_Noodle.get())
    Item15 = float(E_Yogurt.get())
    Item16 = float(E_Chesee_Chips.get())
    Item17 = float(E_Hamburger.get())
    Item18 = float(E_Spaghetti.get())
    Item19 = float(E_Chef_Salad.get())
    Item20 = float(E_Beef_Steak.get())
    Item21 = float(E_Onion_Rings.get())
    Item22 = float(E_CheeseBurger.get())
    Item23 = float(E_ChickenSteak.get())
    Item24 = float(E_Old_Italia_Pizza.get())

    PriceofDrinks=(Item1*4.00)+(Item2*6.50)+(Item3*2.99)+(Item4*6.50)+(Item5*6.50)+(Item6*3.99)+(Item7*8.99)+(Item8*9.99)
    PriceofSnacks=(Item9*5.99)+(Item10*9.80)+(Item11*11.95)+(Item12*15.75)+(Item13*10.90)+(Item14*6.00)+(Item15*8.90)+(Item16*7.99)
    PriceofFoods = (Item17*10.00)+(Item18*15.50)+(Item19*17.99)+(Item20*35.50)+(Item21*9.95)+(Item22*10.00)+(Item23*25.50)+(Item24*20.99)

    DrinksPrice = str("%.2f"%(PriceofDrinks)), "TL"
    SnacksPrice = str("%.2f" %(PriceofSnacks)), "TL" 
    FoodsPrice = str("%.2f" %(PriceofFoods)), "TL"
    CostofDrinks.set(DrinksPrice)
    CostofSnacks.set(SnacksPrice)
    CostofFoods.set(FoodsPrice)
    SC=str("%.2f"%(2.59)), "TL"
    ServiceCharge.set(SC)

    SubTotalofITEMS=str("%.2f"%(PriceofDrinks+PriceofSnacks+PriceofFoods+1.59)), "TL"
    SubTotal.set(SubTotalofITEMS)

    Tax=str("%.2f"%((PriceofDrinks+PriceofSnacks+PriceofFoods+1.59)*0.15)), "TL"
    PaidTax.set(Tax)
    TT=((PriceofDrinks+PriceofSnacks+PriceofFoods+1.59)*0.15)
    TC=str("%.2f"%(PriceofDrinks+PriceofSnacks+PriceofFoods+1.59+TT)), "TL"
    TotalCost.set(TC)

def chkTea():
    if(var1.get()==1):
        txtTea.configure(state=NORMAL)
        txtTea.focus()
        txtTea.delete("0",END)
        E_Tea.set("")
    elif(var1.get()==0):
        txtTea.configure(state=DISABLED)
        E_Tea.set("0")
        
def chkCoke():
    if (var2.get() == 1):
        txtCoke.configure(state=NORMAL)
        txtCoke.focus()
        txtCoke.delete("0", END)
        E_Coke.set("")
    elif (var2.get() == 0):
        txtCoke.configure(state=DISABLED)
        E_Coke.set("0")

def chkWater():
    if (var3.get() == 1):
        txtWater.configure(state=NORMAL)
        txtWater.focus()
        txtWater.delete("0", END)
        E_Water.set("")
    elif (var3.get() == 0):
        txtWater.configure(state=DISABLED)
        E_Water.set("0")

def chkAyran():
    if (var4.get() == 1):
        txtAyran.configure(state=NORMAL)
        txtAyran.focus()
        txtAyran.delete("0", END)
        E_Ayran.set("")
    elif (var4.get() == 0):
        txtAyran.configure(state=DISABLED)
        E_Ayran.set("0")

def chkLemonade():
    if (var5.get() == 1):
        txtLemonade.configure(state=NORMAL)
        txtLemonade.focus()
        txtLemonade.delete("0", END)
        E_Lemonade.set("")
    elif (var5.get() == 0):
        txtLemonade.configure(state=DISABLED)
        E_Lemonade.set("0")

def chkSoda_Water():
    if (var6.get() == 1):
        txtSoda_Water.configure(state=NORMAL)
        txtSoda_Water.focus()
        txtSoda_Water.delete("0", END)
        E_Soda_Water.set("")
    elif (var6.get() == 0):
        txtSoda_Water.configure(state=DISABLED)
        E_Soda_Water.set("0")

def chkOrange_Juice():
    if (var7.get() == 1):
        txtOrangeJuice.configure(state=NORMAL)
        txtOrangeJuice.focus()
        txtOrangeJuice.delete("0", END)
        E_Orange_Juice.set("")
    elif (var7.get() == 0):
        txtOrangeJuice.configure(state=DISABLED)
        E_Orange_Juice.set("0")

def chkTurkish_Coffee():
    if (var8.get() == 1):
        txtTurkish_Coffee.configure(state=NORMAL)
        txtTurkish_Coffee.focus()
        txtTurkish_Coffee.delete("0", END)
        E_Turkish_Coffee.set("")
    elif (var8.get() == 0):
        txtTurkish_Coffee.configure(state=DISABLED)
        E_Turkish_Coffee.set("0")
        
def chkRoll():
    if(var9.get()==1):
        txtRoll.configure(state=NORMAL)
        txtRoll.focus()
        txtRoll.delete("0",END)
        E_Roll.set("")
    elif(var9.get()==0):
        txtRoll.configure(state=DISABLED)
        E_Roll.set("0")
        
def chkSoup():
    if (var10.get() == 1):
        txtSoup.configure(state=NORMAL)
        txtSoup.focus()
        txtSoup.delete("0", END)
        E_Soup.set("")
    elif (var10.get() == 0):
        txtSoup.configure(state=DISABLED)
        E_Soup.set("0")

def chkRice():
    if (var11.get() == 1):
        txtRice.configure(state=NORMAL)
        txtRice.focus()
        txtRice.delete("0", END)
        E_Rice.set("")
    elif (var11.get() == 0):
        txtRice.configure(state=DISABLED)
        E_Rice.set("0")

def chkFries():
    if (var12.get() == 1):
        txtFries.configure(state=NORMAL)
        txtFries.focus()
        txtFries.delete("0", END)
        E_Fries.set("")
    elif (var12.get() == 0):
        txtFries.configure(state=DISABLED)
        E_Fries.set("0")

def chkSalad():
    if (var13.get() == 1):
        txtSalad.configure(state=NORMAL)
        txtSalad.focus()
        txtSalad.delete("0", END)
        E_Salad.set("")
    elif (var13.get() == 0):
        txtSalad.configure(state=DISABLED)
        E_Salad.set("0")

def chkNoodle():
    if (var14.get() == 1):
        txtNoodle.configure(state=NORMAL)
        txtNoodle.focus()
        txtNoodle.delete("0", END)
        E_Noodle.set("")
    elif (var14.get() == 0):
        txtNoodle.configure(state=DISABLED)
        E_Noodle.set("0")

def chkYogurt():
    if (var15.get() == 1):
        txtYogurt.configure(state=NORMAL)
        txtYogurt.focus()
        txtYogurt.delete("0", END)
        E_Yogurt.set("")
    elif (var15.get() == 0):
        txtYogurt.configure(state=DISABLED)
        E_Yogurt.set("0")

def chkChesee_Chips():
    if (var16.get() == 1):
        txtChesee_Chips.configure(state=NORMAL)
        txtChesee_Chips.focus()
        txtChesee_Chips.delete("0", END)
        E_Chesee_Chips.set("")
    elif (var16.get() == 0):
        txtChesee_Chips.configure(state=DISABLED)
        E_Chesee_Chips.set("0")

def chkHamburger():
    if (var17.get() == 1):
        txtHamburger.configure(state=NORMAL)
        txtHamburger.focus()
        txtHamburger.delete("0", END)
        E_Hamburger.set("")
    elif (var17.get() == 0):
        txtHamburger.configure(state=DISABLED)
        E_Hamburger.set("0")

def chkSpaghetti():
    if (var18.get() == 1):
        txtSpaghetti.configure(state=NORMAL)
        txtSpaghetti.focus()
        txtSpaghetti.delete("0", END)
        E_Spaghetti.set("")
    elif (var18.get() == 0):
        txtSpaghetti.configure(state=DISABLED)
        E_Spaghetti.set("0")

def chkChef_Salad():
    if (var19.get() == 1):
        txtChef_Salad.configure(state=NORMAL)
        txtChef_Salad.focus()
        txtChef_Salad.delete("0", END)
        E_Chef_Salad.set("")
    elif (var19.get() == 0):
        txtChef_Salad.configure(state=DISABLED)
        E_Chef_Salad.set("0")

def chkBeef_Steak():
    if (var20.get() == 1):
        txtBeef_Steak.configure(state=NORMAL)
        txtBeef_Steak.focus()
        txtBeef_Steak.delete("0", END)
        E_Beef_Steak.set("")
    elif (var20.get() == 0):
        txtBeef_Steak.configure(state=DISABLED)
        E_Beef_Steak.set("0")

def chkOnion_Rings():
    if (var21.get() == 1):
        txtOnion_Rings.configure(state=NORMAL)
        txtOnion_Rings.focus()
        txtOnion_Rings.delete("0", END)
        E_Onion_Rings.set("")
    elif (var21.get() == 0):
        txtOnion_Rings.configure(state=DISABLED)
        E_Onion_Rings.set("0")

def chkCheeseburger():
    if (var22.get() == 1):
        txtCheeseburger.configure(state=NORMAL)
        txtCheeseburger.focus()
        txtCheeseburger.delete("0", END)
        E_CheeseBurger.set("")
    elif (var22.get() == 0):
        txtCheeseburger.configure(state=DISABLED)
        E_CheeseBurger.set("0")

def chkChicken_Steak():
    if (var23.get() == 1):
        txtChicken_Steak.configure(state=NORMAL)
        txtChicken_Steak.focus()
        txtChicken_Steak.delete("0", END)
        E_ChickenSteak.set("")
    elif (var23.get() == 0):
        txtChicken_Steak.configure(state=DISABLED)
        E_ChickenSteak.set("0")

def chkOld_Italia_Pizza():
    if (var24.get() == 1):
        txtOld_Italia_Pizza.configure(state=NORMAL)
        txtOld_Italia_Pizza.focus()
        txtOld_Italia_Pizza.delete("0", END)
        E_Old_Italia_Pizza.set("")
    elif (var24.get() == 0):
        txtOld_Italia_Pizza.configure(state=DISABLED)
        E_Old_Italia_Pizza.set("0")

def Receipt():
    txtReceipt.delete("1.0",END)
    x=random.randint(10903,60923)
    randdomRef=str(x)
    Receipt_Ref.set("BILL"+ randdomRef)

    txtReceipt.insert(END,"Receipt Ref:\t\t"+ Receipt_Ref.get()+"\t\t"+DateOfOrder.get()+"\n")
    txtReceipt.insert(END, "Item:\t\t\t\t" + "Cost of Items" + "\n")
    txtReceipt.insert(END, "Tea:\t\t\t\t\t" + E_Tea.get() + "\n")
    txtReceipt.insert(END, "Coke:\t\t\t\t\t" + E_Coke.get() + "\n")
    txtReceipt.insert(END, "Water:\t\t\t\t\t" + E_Water.get() + "\n")
    txtReceipt.insert(END, "Ayran:\t\t\t\t\t" + E_Ayran.get() + "\n")
    txtReceipt.insert(END, "Lemonade:\t\t\t\t\t" + E_Lemonade.get() + "\n")
    txtReceipt.insert(END, "Soda Water:\t\t\t\t\t" + E_Soda_Water.get() + "\n")
    txtReceipt.insert(END, "Orange Juice:\t\t\t\t\t" + E_Orange_Juice.get() + "\n")
    txtReceipt.insert(END, "Turkish Coffee:\t\t\t\t\t" + E_Turkish_Coffee.get() + "\n")
    txtReceipt.insert(END, "Roll:\t\t\t\t\t" + E_Roll.get() + "\n")
    txtReceipt.insert(END, "Soup:\t\t\t\t\t" + E_Soup.get() + "\n")
    txtReceipt.insert(END, "Rice:\t\t\t\t\t" + E_Rice.get() + "\n")
    txtReceipt.insert(END, "Fries:\t\t\t\t\t" + E_Fries.get() + "\n")
    txtReceipt.insert(END, "Salad:\t\t\t\t\t" + E_Salad.get() + "\n")
    txtReceipt.insert(END, "Noodle:\t\t\t\t\t" + E_Noodle.get() + "\n")
    txtReceipt.insert(END, "Yogurt:\t\t\t\t\t" + E_Yogurt.get() + "\n")
    txtReceipt.insert(END, "Chesee Chips:\t\t\t\t\t" + E_Chesee_Chips.get() + "\n")
    txtReceipt.insert(END, "Hamburger:\t\t\t\t\t" + E_Hamburger.get() + "\n")
    txtReceipt.insert(END, "Spaghetti:\t\t\t\t\t" + E_Spaghetti.get() + "\n")
    txtReceipt.insert(END, "Chef Salad:\t\t\t\t\t" + E_Chef_Salad.get() + "\n")
    txtReceipt.insert(END, "Beef Steak:\t\t\t\t\t" + E_Beef_Steak.get() + "\n")
    txtReceipt.insert(END, "Onion Rings:\t\t\t\t\t" + E_Onion_Rings.get() + "\n")
    txtReceipt.insert(END, "Cheeseburger:\t\t\t\t\t" + E_CheeseBurger.get() + "\n")
    txtReceipt.insert(END, "Chicken Steak:\t\t\t\t\t" + E_ChickenSteak.get() + "\n")
    txtReceipt.insert(END, "Old Italia Pizza:\t\t\t\t\t" + E_Old_Italia_Pizza.get() + "\n")
    txtReceipt.insert(END, "Cost of Drinks:\t\t\t\t" + CostofDrinks.get() +"\nTax Paid:\t\t\t\t"+PaidTax.get()+ "\n")
    txtReceipt.insert(END, "Cost of Snacks:\t\t\t\t" + CostofSnacks.get() +"\nTax Paid:\t\t\t\t"+PaidTax.get()+ "\n")
    txtReceipt.insert(END, "Cost of Foods:\t\t\t\t" + CostofFoods.get() + "\nSub Total:\t\t\t\t"+str(SubTotal.get())+ "\n")
    txtReceipt.insert(END, "Service Charge:\t\t\t\t" + ServiceCharge.get() + "\nTotal Cost:\t\t\t\t"+str(TotalCost.get())+ "\n")


"""Drinks"""
Tea = Checkbutton(Drinks_F, text="Tea", variable=var1, onvalue = 1, offvalue=0,font=("times", 18, "bold"), bg="#212F3C", fg="#AEB6BF", command=chkTea).grid(row=0, sticky=W)
Coke = Checkbutton(Drinks_F, text="Coke", variable=var2, onvalue = 1, offvalue=0,font=("times", 18, "bold"), bg="#212F3C", fg="#AEB6BF", command=chkCoke).grid(row=1, sticky=W)
Water = Checkbutton(Drinks_F, text="Water", variable=var3, onvalue = 1, offvalue=0,font=("times", 18, "bold"), bg="#212F3C", fg="#AEB6BF", command=chkWater).grid(row=2, sticky=W)
Ayran = Checkbutton(Drinks_F, text="Ayran", variable=var4, onvalue = 1, offvalue=0,font=("times", 18, "bold"), bg="#212F3C", fg="#AEB6BF", command=chkAyran).grid(row=3, sticky=W)
Lemonade = Checkbutton(Drinks_F, text="Lemonade", variable=var5, onvalue = 1, offvalue=0,font=("times", 18, "bold"), bg="#212F3C", fg="#AEB6BF", command=chkLemonade).grid(row=4, sticky=W)
Soda_Water = Checkbutton(Drinks_F, text="Soda Water", variable=var6, onvalue = 1, offvalue=0,font=("times", 18, "bold"), bg="#212F3C", fg="#AEB6BF", command=chkSoda_Water).grid(row=5, sticky=W)
Orange_Juice = Checkbutton(Drinks_F, text="Orange Juice", variable=var7, onvalue = 1, offvalue=0,font=("times", 18, "bold"), bg="#212F3C", fg="#AEB6BF", command=chkOrange_Juice).grid(row=6, sticky=W)
Turkish_Coffee = Checkbutton(Drinks_F, text="Turkish Coffee", variable=var8, onvalue = 1, offvalue=0,font=("times", 18, "bold"), bg="#212F3C", fg="#AEB6BF", command=chkTurkish_Coffee).grid(row=7, sticky=W)

"""Entry Box for Drinks"""
txtTea = Entry(Drinks_F,font=("times", 16, "bold"),bd=9, width=7, justify=LEFT, state = DISABLED,textvariable=E_Tea)
txtTea.grid(row=0,column=1)
txtCoke = Entry(Drinks_F,font=("times", 16, "bold"),bd=9, width=7, justify=LEFT, state = DISABLED,textvariable=E_Coke)
txtCoke.grid(row=1,column=1)
txtWater = Entry(Drinks_F,font=("times", 16, "bold"),bd=9, width=7, justify=LEFT, state = DISABLED,textvariable=E_Water)
txtWater.grid(row=2,column=1)
txtAyran = Entry(Drinks_F,font=("times", 16, "bold"),bd=9, width=7, justify=LEFT, state = DISABLED,textvariable=E_Ayran)
txtAyran.grid(row=3,column=1)
txtLemonade = Entry(Drinks_F,font=("times", 16, "bold"),bd=9, width=7, justify=LEFT, state = DISABLED,textvariable=E_Lemonade)
txtLemonade.grid(row=4,column=1)
txtSoda_Water = Entry(Drinks_F,font=("times", 16, "bold"),bd=9, width=7, justify=LEFT, state = DISABLED,textvariable=E_Soda_Water)
txtSoda_Water.grid(row=5,column=1)
txtOrangeJuice = Entry(Drinks_F,font=("times", 16, "bold"),bd=9, width=7, justify=LEFT, state = DISABLED,textvariable=E_Orange_Juice)
txtOrangeJuice.grid(row=6,column=1)
txtTurkish_Coffee = Entry(Drinks_F,font=("times", 16, "bold"),bd=9, width=7, justify=LEFT, state = DISABLED,textvariable=E_Turkish_Coffee)
txtTurkish_Coffee.grid(row=7,column=1)

"""Snacks"""
Roll = Checkbutton(Snacks_F, text="Roll", variable=var9, onvalue = 1, offvalue=0,font=("times", 18, "bold"), bg="#212F3C", fg="#AEB6BF", command=chkRoll).grid(row=0, sticky=W)
Soup = Checkbutton(Snacks_F, text="Soup", variable=var10, onvalue = 1, offvalue=0,font=("times", 18, "bold"), bg="#212F3C", fg="#AEB6BF", command=chkSoup).grid(row=1, sticky=W)
Rice = Checkbutton(Snacks_F, text="Rice", variable=var11, onvalue = 1, offvalue=0,font=("times", 18, "bold"), bg="#212F3C", fg="#AEB6BF", command=chkRice).grid(row=2, sticky=W)
Fries = Checkbutton(Snacks_F, text="Fries", variable=var12, onvalue = 1, offvalue=0,font=("times", 18, "bold"), bg="#212F3C", fg="#AEB6BF", command=chkFries).grid(row=3, sticky=W)
Salad = Checkbutton(Snacks_F, text="Salad", variable=var13, onvalue = 1, offvalue=0,font=("times", 18, "bold"), bg="#212F3C", fg="#AEB6BF", command=chkSalad).grid(row=4, sticky=W)
Noodle = Checkbutton(Snacks_F, text="Noodle", variable=var14, onvalue = 1, offvalue=0,font=("times", 18, "bold"), bg="#212F3C", fg="#AEB6BF", command=chkNoodle).grid(row=5, sticky=W)
Yogurt = Checkbutton(Snacks_F, text="Yogurt", variable=var15, onvalue = 1, offvalue=0,font=("times", 18, "bold"), bg="#212F3C", fg="#AEB6BF", command=chkYogurt).grid(row=6, sticky=W)
Chesee_Chips = Checkbutton(Snacks_F, text="Chesee Chips", variable=var16, onvalue = 1, offvalue=0,font=("times", 18, "bold"), bg="#212F3C", fg="#AEB6BF", command=chkChesee_Chips).grid(row=7, sticky=W)

"""Entry Box for Snacks"""
txtRoll = Entry(Snacks_F,font=("times", 16, "bold"),bd=9, width=7, justify=LEFT, state = DISABLED,textvariable=E_Roll)
txtRoll.grid(row=0,column=1)
txtSoup = Entry(Snacks_F,font=("times", 16, "bold"),bd=9, width=7, justify=LEFT, state = DISABLED,textvariable=E_Soup)
txtSoup.grid(row=1,column=1)
txtRice = Entry(Snacks_F,font=("times", 16, "bold"),bd=9, width=7, justify=LEFT, state = DISABLED,textvariable=E_Rice)
txtRice.grid(row=2,column=1)
txtFries = Entry(Snacks_F,font=("times", 16, "bold"),bd=9, width=7, justify=LEFT, state = DISABLED,textvariable=E_Fries)
txtFries.grid(row=3,column=1)
txtSalad = Entry(Snacks_F,font=("times", 16, "bold"),bd=9, width=7, justify=LEFT, state = DISABLED,textvariable=E_Salad)
txtSalad.grid(row=4,column=1)
txtNoodle = Entry(Snacks_F,font=("times", 16, "bold"),bd=9, width=7, justify=LEFT, state = DISABLED,textvariable=E_Noodle)
txtNoodle.grid(row=5,column=1)
txtYogurt = Entry(Snacks_F,font=("times", 16, "bold"),bd=9, width=7, justify=LEFT, state = DISABLED,textvariable=E_Yogurt)
txtYogurt.grid(row=6,column=1)
txtChesee_Chips = Entry(Snacks_F,font=("times", 16, "bold"),bd=9, width=7, justify=LEFT, state = DISABLED,textvariable=E_Chesee_Chips)
txtChesee_Chips.grid(row=7,column=1)

"""Foods"""
Hamburger = Checkbutton(Food_F, text="Hamburger", variable=var17, onvalue = 1, offvalue=0,font=("times", 18, "bold"), bg="#212F3C", fg="#AEB6BF", command=chkHamburger).grid(row=0, sticky=W)
Spaghetti = Checkbutton(Food_F, text="Spaghetti", variable=var18, onvalue = 1, offvalue=0,font=("times", 18, "bold"), bg="#212F3C", fg="#AEB6BF", command=chkSpaghetti).grid(row=1, sticky=W)
Chef_Salad = Checkbutton(Food_F, text="Chef Salad", variable=var19, onvalue = 1, offvalue=0,font=("times", 18, "bold"), bg="#212F3C", fg="#AEB6BF", command=chkChef_Salad).grid(row=2, sticky=W)
Beef_Steak = Checkbutton(Food_F, text="Beef Steak", variable=var20, onvalue = 1, offvalue=0,font=("times", 18, "bold"), bg="#212F3C", fg="#AEB6BF", command=chkBeef_Steak).grid(row=3, sticky=W)
Onion_Rings = Checkbutton(Food_F, text="Onion Rings", variable=var21, onvalue = 1, offvalue=0,font=("times", 18, "bold"), bg="#212F3C", fg="#AEB6BF", command=chkOnion_Rings).grid(row=4, sticky=W)
Cheeseburger = Checkbutton(Food_F, text="Cheeseburger", variable=var22, onvalue = 1, offvalue=0,font=("times", 18, "bold"), bg="#212F3C", fg="#AEB6BF", command=chkCheeseburger).grid(row=5, sticky=W)
Chicken_Steak = Checkbutton(Food_F, text="Chicken Steak", variable=var23, onvalue = 1, offvalue=0,font=("times", 18, "bold"), bg="#212F3C", fg="#AEB6BF", command=chkChicken_Steak).grid(row=6, sticky=W)
Old_Italia_Pizza = Checkbutton(Food_F, text="Old Italia Pizza", variable=var24, onvalue = 1, offvalue=0,font=("times", 18, "bold"), bg="#212F3C", fg="#AEB6BF", command=chkOld_Italia_Pizza).grid(row=7, sticky=W)

"""Entry Box for Foods"""
txtHamburger = Entry(Food_F,font=("times", 16, "bold"),bd=9, width=7, justify=LEFT, state = DISABLED, textvariable=E_Hamburger)
txtHamburger.grid(row=0,column=1)
txtSpaghetti = Entry(Food_F,font=("times", 16, "bold"),bd=9, width=7, justify=LEFT, state = DISABLED,textvariable=E_Spaghetti)
txtSpaghetti.grid(row=1,column=1)
txtChef_Salad = Entry(Food_F,font=("times", 16, "bold"),bd=9, width=7, justify=LEFT, state = DISABLED,textvariable=E_Chef_Salad)
txtChef_Salad.grid(row=2,column=1)
txtBeef_Steak = Entry(Food_F,font=("times", 16, "bold"),bd=9, width=7, justify=LEFT, state = DISABLED,textvariable=E_Beef_Steak)
txtBeef_Steak.grid(row=3,column=1)
txtOnion_Rings = Entry(Food_F,font=("times", 16, "bold"),bd=9, width=7, justify=LEFT, state = DISABLED,textvariable=E_Onion_Rings)
txtOnion_Rings.grid(row=4,column=1)
txtCheeseburger = Entry(Food_F,font=("times", 16, "bold"),bd=9, width=7, justify=LEFT, state = DISABLED,textvariable=E_CheeseBurger)
txtCheeseburger.grid(row=5,column=1)
txtChicken_Steak = Entry(Food_F,font=("times", 16, "bold"),bd=9, width=7, justify=LEFT, state = DISABLED,textvariable=E_ChickenSteak)
txtChicken_Steak.grid(row=6,column=1)
txtOld_Italia_Pizza = Entry(Food_F,font=("times", 16, "bold"),bd=9, width=7, justify=LEFT, state = DISABLED,textvariable=E_Old_Italia_Pizza)
txtOld_Italia_Pizza.grid(row=7,column=1)


"""Total Cost"""
lblCostofDrinks = Label(Cost_F,font=("times", 14, "bold"),text="Cost of Drinks\t   ",bd=7, bg="#212F3C", fg="#AEB6BF")
lblCostofDrinks.grid(row=0, column=0, sticky=W)
txtCostofDrinks = Entry(Cost_F, font=("times", 14, "bold"),textvariable=CostofDrinks,bd=7,bg="#AEB6BF",insertwidth=2, justify=RIGHT)
txtCostofDrinks.grid(row=0, column=1)

lblCostofSnacks = Label(Cost_F,font=("times", 14, "bold"),text="Cost of Snacks\t   ",bd=7, bg="#212F3C", fg="#AEB6BF")
lblCostofSnacks.grid(row=0, column=0, sticky=W)
txtCostofSnacks = Entry(Cost_F, font=("times", 14, "bold"),textvariable=CostofSnacks,bd=7,bg="#AEB6BF",insertwidth=2, justify=RIGHT)
txtCostofSnacks.grid(row=0, column=1)

lblCostofFoods = Label(Cost_F,font=("times", 14, "bold"),text="Cost of Foods\t   ",bd=7, bg="#212F3C", fg="#AEB6BF")
lblCostofFoods.grid(row=1, column=0, sticky=W)
txtCostofFoods = Entry(Cost_F, font=("times", 14, "bold"),textvariable=CostofFoods,bd=7,bg="#AEB6BF",insertwidth=2, justify=RIGHT)
txtCostofFoods.grid(row=1, column=1)

lblServiceCharge = Label(Cost_F,font=("times", 14, "bold"),text="Service Charge\t   ",bd=7, bg="#212F3C", fg="#AEB6BF")
lblServiceCharge.grid(row=2, column=0, sticky=W)
txtServiceCharge = Entry(Cost_F, font=("times", 14, "bold"),textvariable=ServiceCharge,bd=7,bg="#AEB6BF",insertwidth=2, justify=RIGHT)
txtServiceCharge.grid(row=2, column=1)

"""Payment Information"""
lblPaidTax = Label(Cost_F,font=("times", 14, "bold"),text="\tPaid Tax   ", bd=7, bg="#212F3C", fg="#AEB6BF")
lblPaidTax.grid(row=0, column=2, sticky=W)
txtPaidTax = Entry(Cost_F, font=("times", 14, "bold"),textvariable=PaidTax,bd=7,bg="#AEB6BF",insertwidth=2, justify=RIGHT)
txtPaidTax.grid(row=0, column=3)

lblSubTotal = Label(Cost_F,font=("times", 14, "bold"),text="\tSub Total ", bd=7, bg="#212F3C", fg="#AEB6BF")
lblSubTotal .grid(row=1, column=2, sticky=W)
txtSubTotal= Entry(Cost_F, font=("times", 14, "bold"),textvariable=SubTotal,bd=7,bg="#AEB6BF",insertwidth=2, justify=RIGHT)
txtSubTotal .grid(row=1, column=3)

lblTotalCost = Label(Cost_F,font=("times", 14, "bold"),text=" \tTotal Cost",bd=7, bg="#212F3C", fg="#AEB6BF")
lblTotalCost .grid(row=2, column=2, sticky=W)
txtTotalCost= Entry(Cost_F, font=("times", 14, "bold"),textvariable=TotalCost,bd=7,bg="#AEB6BF",insertwidth=2, justify=RIGHT)
txtTotalCost .grid(row=2, column=3)

"""Receipt"""
txtReceipt = Text(Receipt_F, width=50, height=9, bg="#AEB6BF",bd=4,font=("times", 12, "bold"))
txtReceipt.grid(row=0, column=0)

"""Buttons"""
btnTotal= Button(Buttons_F,padx=16, pady=1, bd=7, fg="#AEB6BF", font=("times", 16, "bold"), width=4, text="Total", bg="#212F3C", command=CostofItem).grid(row=0, column=0)
btnReceipt= Button(Buttons_F,padx=16, pady=1, bd=7, fg="#AEB6BF", font=("times", 16, "bold"), width=5, text="Receipt", bg="#212F3C", command=Receipt).grid(row=0, column=1)
btnReset= Button(Buttons_F,padx=16, pady=1, bd=7, fg="#AEB6BF", font=("times", 16, "bold"), width=5, text="Reset", bg="#212F3C", command=Reset).grid(row=0, column=2)
btnExit= Button(Buttons_F,padx=16, pady=1, bd=7, fg="#AEB6BF", font=("times", 16, "bold"), width=4, text="Exit", bg="#212F3C", command=iExit).grid(row=0, column=3)

"""Calculator Display"""
def btnClick(numbers):
    global operator
    operator=operator+str(numbers)
    text_Input.set(operator)

def btnClear():
    global operator
    operator=""
    text_Input.set("")

def btnEquals():
    global operator
    sumup=str(eval(operator))
    text_Input.set(sumup)
    operator=""


txtDisplay = Entry(Cal_F, width=50, bg="#AEB6BF",bd=4,font=("times", 12, "bold"), justify=RIGHT, textvariable=text_Input)
txtDisplay.grid(row=0, column=0, columnspan=4, pady=1)
txtDisplay.insert(0,"0")

"""Calculator Buttons"""
btn7= Button(Cal_F,padx=16, pady=1, bd=7, fg="#AEB6BF", font=("times", 16, "bold"), width=4, text="7", bg="#212F3C", command=lambda:btnClick(7)).grid(row=2, column=0)
btn8= Button(Cal_F,padx=16, pady=1, bd=7, fg="#AEB6BF", font=("times", 16, "bold"), width=4, text="8", bg="#212F3C", command=lambda:btnClick(8)).grid(row=2, column=1)
btn9= Button(Cal_F,padx=16, pady=1, bd=7, fg="#AEB6BF", font=("times", 16, "bold"), width=4, text="9", bg="#212F3C", command=lambda:btnClick(9)).grid(row=2, column=2)
btnAdd= Button(Cal_F,padx=16, pady=1, bd=7, fg="#AEB6BF", font=("times", 16, "bold"), width=4, text="+", bg="#212F3C", command=lambda:btnClick("+")).grid(row=2, column=3)

btn4= Button(Cal_F,padx=16, pady=1, bd=7, fg="#AEB6BF", font=("times", 16, "bold"), width=4, text="4", bg="#212F3C", command=lambda:btnClick(4)).grid(row=3, column=0)
btn5= Button(Cal_F,padx=16, pady=1, bd=7, fg="#AEB6BF", font=("times", 16, "bold"), width=4, text="5", bg="#212F3C", command=lambda:btnClick(5)).grid(row=3, column=1)
btn6= Button(Cal_F,padx=16, pady=1, bd=7, fg="#AEB6BF", font=("times", 16, "bold"), width=4, text="6", bg="#212F3C", command=lambda:btnClick(6)).grid(row=3, column=2)
btnSub= Button(Cal_F,padx=16, pady=1, bd=7, fg="#AEB6BF", font=("times", 16, "bold"), width=4, text="-", bg="#212F3C", command=lambda:btnClick("-")).grid(row=3, column=3)

btn1= Button(Cal_F,padx=16, pady=1, bd=7, fg="#AEB6BF", font=("times", 16, "bold"), width=4, text="1", bg="#212F3C", command=lambda:btnClick(1)).grid(row=4, column=0)
btn2= Button(Cal_F,padx=16, pady=1, bd=7, fg="#AEB6BF", font=("times", 16, "bold"), width=4, text="2", bg="#212F3C", command=lambda:btnClick(2)).grid(row=4, column=1)
btn3= Button(Cal_F,padx=16, pady=1, bd=7, fg="#AEB6BF", font=("times", 16, "bold"), width=4, text="3", bg="#212F3C", command=lambda:btnClick(3)).grid(row=4, column=2)
btnMult= Button(Cal_F,padx=16, pady=1, bd=7, fg="#AEB6BF", font=("times", 16, "bold"), width=4, text="*", bg="#212F3C", command=lambda:btnClick("*")).grid(row=4, column=3)

btn0= Button(Cal_F,padx=16, pady=1, bd=7, fg="#AEB6BF", font=("times", 16, "bold"), width=4, text="0", bg="#212F3C", command=lambda:btnClick(0)).grid(row=5, column=0)
btnClear= Button(Cal_F,padx=16, pady=1, bd=7, fg="#AEB6BF", font=("times", 16, "bold"), width=4, text="C", bg="#212F3C", command=btnClear).grid(row=5, column=1)
btnEquals= Button(Cal_F,padx=16, pady=1, bd=7, fg="#AEB6BF", font=("times", 16, "bold"), width=4, text="=", bg="#212F3C", command=btnEquals).grid(row=5, column=2)
btnDivision= Button(Cal_F,padx=16, pady=1, bd=7, fg="#AEB6BF", font=("times", 16, "bold"), width=4, text="/", bg="#212F3C", command=lambda:btnClick("/")).grid(row=5, column=3)

root.mainloop()