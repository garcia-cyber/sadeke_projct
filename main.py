from tkinter import *
from tkinter import ttk
from tkinter.messagebox import *
import mysql.connector as mariadb





admin = mariadb.connect(host="localhost", user = 'linux',password = 'data',database = 'desktop')

#---------------------- fonction 

def deco():
    ask = showinfo('','voulez-vous quitter ?')
    
    if ask == 'ok':
        app.destroy()
   
#--------- add 
def add():
    #--------- appel de ma variable data
    global admin 
    
    
    nom = ent_nom.get()
    postnom = ent_postnom.get()
    prenom = ent_prenom.get()
    sexe = ent_sexe.get()
    adresse = ent_adresse.get()
    commune = ent_commune.get()
    formation = ent_formation.get()
    telephone = ent_telephone.get()
    
    #-------- PAS BESOIN D'UN CHAMPS VIDE 
    
    
    if nom == '' or postnom == '' or prenom == '' or sexe == '' or adresse == '' or commune == '' or formation == '' or telephone == '' :
        showwarning("","veillez remplire les formulaire")
        
    else:
        
            
        a = admin.cursor()
        t = str(telephone)
        a.execute("insert into formations(noms,postnoms,prenoms,sexes,adresses,communes,typeFormation,telephones)values('"+ nom +"','"+ postnom +"', '"+ prenom +"','"+ sexe +"', '"+ adresse +"', '" + commune+"','" + formation + "','"+ t+"')")
        admin.commit()
        a.close()
        
        ent_nom.delete(0,'end')
        ent_postnom.delete(0,'end')
        ent_prenom.delete(0,'end')
        # ent_sexe.delete(0,'end')
        ent_adresse.delete(0,'end')
        # ent_commune.delete(0,'end')
        # ent_formation.delete(0,'end')
        ent_telephone.delete(0,'end')
        
        showinfo("","inscription reussi ")
        
        
        
        admin.close()
        
       
            
                 

        
    
    
   
   
 
       
    

#------ modify
def modify():
    pass

#-------delete
def delete():
    pass


#-----------------------parametrage

app = Tk()
app.geometry("1900x900")
app.title("centrale")
app.attributes('-zoomed',True)
app.resizable(0,0)

#------------------------------ MENU



#**********sous menu 




#****************************** bout pour autres choses

link = Frame(app,bg = '#111')
link.place(x = 0 , y =0 ,height=85,width=1950)


#****** bouton pour cliquez


btn_click_one = Button(link,text='x'.capitalize(),command=deco,fg='#b22222')
btn_af = Button(link , )

#----------------parametr de mes boutons  
btn_click_one.place(x = 1850 , y = 25)


#******************* enregistrement pour la formation 

sig = LabelFrame(app,text='enre',bg='#e5e5e5')
sig.place(x = 2,y = 85,width=550,height=550)


#------text sign up 


inscription = Label(sig, text="inscription ...".upper(),font=("arial",20),bg='#e5e5e5')

nom = Label(sig , text="nom".capitalize(),font=("arial",12),bg='#e5e5e5')
postnom = Label(sig , text="postnom".capitalize(),font=("arial",12),bg='#e5e5e5')
prenom = Label(sig , text="prenom".capitalize(),font=("arial",12),bg='#e5e5e5')
sexe = Label(sig , text="sexe".capitalize(),font=("arial",12),bg='#e5e5e5')
adresse = Label(sig , text="adresse".capitalize(),font=("arial",12),bg='#e5e5e5')
commune = Label(sig , text="commune".capitalize(),font=("arial",12),bg='#e5e5e5')
formation = Label(sig , text="type de formation".capitalize(),font=("arial",12),bg='#e5e5e5')
telephone = Label(sig , text="telephone".capitalize(),font=("arial",12),bg='#e5e5e5')


#*************** AFFICHAGE TEXT 

inscription.place(x = 1, y = 30)

nom.place(x = 1, y = 115)
postnom.place(x = 1, y = 150)
prenom.place(x = 1, y = 190)
sexe.place(x = 1, y = 230)
adresse.place(x = 1, y = 270)
commune.place(x = 1, y = 310)
formation.place(x = 1, y = 350)
telephone.place(x = 1, y = 390)



#---------------- ENTREE DE DONNEE

sexes = ['masculin','feminin']
com = ["n djili","masina","kimbaseke"]
form = ['informatique','auto-ecole',"coupe et couture"]


ent_nom = Entry(sig)
ent_postnom = Entry(sig)
ent_prenom = Entry(sig)
ent_sexe = ttk.Combobox(sig,values=sexes,state='readonly')
ent_sexe.current(0)
ent_adresse = Entry(sig)
ent_commune = ttk.Combobox(sig,values=com,state='readonly')
ent_commune.current(0)
ent_formation = ttk.Combobox(sig,values=form,state='readonly')
ent_formation.current(0)
ent_telephone = Entry(sig)


#----------------------- AFFICHE ENTRY

ent_nom.place(x = 140 ,y= 115,width=370,height=29)
ent_postnom.place(x = 140 ,y= 150,width=370,height=29)
ent_prenom.place(x = 140 ,y= 190,width=370,height=29)
ent_sexe.place(x = 140 ,y= 230,width=370,height=29)
ent_adresse.place(x = 140 ,y= 270,width=370,height=29)
ent_commune.place(x = 140 ,y= 310,width=370,height=29)
ent_formation.place(x = 140 ,y= 350,width=370,height=29)
ent_telephone.place(x = 140 ,y= 390,width=370,height=29)


#---------------- BOUTON D'ENREGISTREMENT 

ajoute = Button(sig,text = "ajouter",border=1,fg='#111',command=add)
modifie = Button(sig,text = "modifier",border=1,fg='#111',command=modify)
supprimer = Button(sig,text = "supprimer",border=1,fg='#111',command=delete)


#---------------- AFFICHE BOUTON PATATI PATATA

ajoute.place(x = 150 , y = 450,height=50)
modifie.place(x = 270 , y = 450,height=50)
supprimer.place(x = 400 , y = 450,height=50)

















#----------------------- boucle du programme
app.config(bg='#e5e5e5')
# app.config(bg='#203d14')
# app.config(bg='#12333e')
# app.config(bg='#06324f')
app.mainloop()
