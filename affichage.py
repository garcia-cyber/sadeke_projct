from tkinter import *
from tkinter import ttk
from tkinter.messagebox import *
import mysql.connector as mariadb


admin = mariadb.connect(host="localhost", user = 'linux',password = 'data',database = 'desktop')

af = Tk()
af.geometry('2000x900')
af.config(bg = '#f2f2f2')


# TABLEAU DEPUIS LA DATA

sig2 = LabelFrame(af,text='affichage'.upper(),bg='#e5e5e5',font=("arial",14))
sig2.place(x = 0,y = 0,width=1799,height=330)


tb = ttk.Treeview(sig2,columns=(1,2,3,4,5,6,7,8,9),show='headings' , height=50)
tb.place(x = 0 , y =5)

tb.heading(1,text = 'reference')
tb.heading(2,text = 'noms')
tb.heading(3,text = 'postnoms')
tb.heading(4,text = 'prenoms')
tb.heading(5,text = 'sexes')
tb.heading(6,text = 'adresse')
tb.heading(7,text = 'communes')
tb.heading(8,text = 'type des formations')
tb.heading(9,text = "date d 'inscription ")

see = admin.cursor()
rq = 'select * from formations'
see.execute(rq)
to_see = see.fetchall()
inc = 0
for i in to_see:
    tb.insert('',inc,text ="",values=(i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8],i[9]))
    inc+=1







af.mainloop()