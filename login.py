from tkinter import *
from tkinter import ttk
from tkinter.messagebox import *
import mysql.connector as mariadb


#--------------------test de la connexion

admin = mariadb.connect(host="localhost", user = 'linux',password = 'data',database = 'desktop')
#chef  = mariadb.connect(host="localhost", user = 'chef_groupe',password = '',database = 'desktop')


#********************** fonction pour la connexion et passage au next page

def log():
    
    #************************* appel variable locole
    
    global admin
    
    #*********************** gestion d'erreurs
    
    try:
        user        = enter_ask_input_user.get()
        pwd         = enter_ask_input_password.get()
        type_entry  = enter_ask_input_choix.get()
        
        #************************* eviter un champs vide 
        if user == '' or pwd == '' or type_entry == '':
            showwarning(""," pas de champs vide ".upper())
        
        #************FIN DE LA VERIFICATION     
            
        #*********** verification du type d'utilisateur est administrateur ET DU MOT DE PASSE
        elif type_entry == 'admin'.capitalize():
            if user == 'lagarxia' and pwd == '123':
                login.destroy()
                import main
                # showinfo("", " bonjour chef admin".capitalize())
        
        elif type_entry == 'chef de groupe'.capitalize():
            showinfo("", " bonjour chef ")  
            
        elif type_entry == 'admin centrale'.capitalize():
            showinfo("", " bonjour super admin  ")   
    except:
        showerror("" , "erreur du programmer ".capitalize())     
    
 
        



#------------------creation de la fenetre login 
login = Tk()
login.geometry("620x425")
login.resizable(0,0)
login.title("authentification".capitalize())
login.config(bg='#e9e9e9')


#----------------------------- parametrage  du 

txt = Label(login,text = " rjted".upper(),bg='#e9e9e9',border=5 ,underline= 1,font= ("arial" , 14))
txt.place(x = 25, y = 30)


text_ask = LabelFrame(login,bg= '#e9e9e9',font = ("arial",14),text="authentification".capitalize(),fg='#111')
text_ask.place(x = 25 , y= 90 , width=560,height= 300)

#------------------ user text

text_ask_text_user = Label(text_ask,text="nom d'utilisateur".title(),bg="#e9e9e9")
text_ask_text_password = Label(text_ask,text="mot de passe".title(),bg="#e9e9e9")
text_ask_text_type = Label(text_ask,text="type d'utilisateur".title(),bg="#e9e9e9")

#---------------parametrage  user text 

text_ask_text_user.place(x = 5,y = 50)
text_ask_text_password.place(x = 5,y = 100)
text_ask_text_type.place(x = 5,y = 150)

#------------------ user input 

enter_ask_input_user = Entry(text_ask)
enter_ask_input_password = Entry(text_ask,show='*')


#---------------parametrage  input entry

type_user = ['admin'.capitalize(),'admin centrale'.capitalize(),'chef de groupe'.capitalize(),]
enter_ask_input_choix = ttk.Combobox(text_ask,values=type_user,state='readonly')
enter_ask_input_choix.current(0)


enter_ask_input_user.place(x = 140 ,y= 50,width=370,height=29)
enter_ask_input_password.place(x = 140 ,y= 100,width=370,height=29)
enter_ask_input_choix.place(x = 140 ,y= 150,width=370,height=29)

#---------------- bouton login user 

btn1 = Button(text_ask,text = "connexion",border=1,bg="#111",fg='#f9f9f9',command=log)


#---------------- parametrage login user bouton

btn1.place(x = 358 , y = 200, width= 150) 
() 








login.mainloop()


"""
a faire apres :
    rien pour l'instant
    
    """
