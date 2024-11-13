'''
Programmeerimine I
2024/2025 sügissemester
#
Projekt
Teema: Ostukorvi planeerija
#
#
Autorid: Nora Liis Palm, Elisabet Koit
#
mõningane eeskuju:
#
Lisakommentaar (nt käivitusjuhend):
#
'''
from tkinter import *
from tkinter import messagebox

info = {}

root = Tk()
root.title("Ostukorvi planeerija")
root.geometry('600x400')

        
minu_pealkiri = Label(root, text="Valige oma dieedieelistus: ")
minu_pealkiri.grid(row=0, column=0, pady=20, sticky ="ew")

dieet_valik = StringVar(value="kõik") #annab dieetvalikule vaikimisi väärtuse kõik


with open("toiduained.txt", encoding="utf-8") as fail:
    for rida in fail:
        if rida.strip== "":
            continue
        andmed = rida.strip().split(", ")

        grupp = andmed[0]
        toit = andmed[1]
        dieedid = andmed[2:]
        
        if grupp not in info:
            info[grupp] = {}
        for dieet in dieedid:
            if dieet not in info[grupp]:
                info[grupp][dieet] = []
            if toit not in info[grupp][dieet]:
                info[grupp][dieet].append(toit)
                
def dieedile_vaskõikd_toiduained(info):
    valik = dieet_valik.get()
    dieedi_toit = {}
    toidu_hulk = []
    for toidutüüp in info.keys():# võtab võtmete väärtused
        dieedi_toit[toidutüüp] = None
    for i in info.values():
        if valik in i.keys():
            if valik == "vegan":
                 toidu_hulk += [i['vegan']]
            elif valik == "vegeterian":
                 toidu_hulk += [i['vegeterian']]
            elif valik == "kõik":
                 toidu_hulk += [i['kõik']]
    toidu_hulk_iter = iter(toidu_hulk)
    for võti in dieedi_toit.keys():
        dieedi_toit[võti] = next(toidu_hulk_iter)

    return dieedi_toit
#Kuvab raami check nuppudele

kuvasisu_frame = Frame(root)
kuvasisu_frame.grid(row=0, column=2, padx=100, pady=10)

def dieedi_toitude_kuvamine(võti):
    väärtused = dieedile_vaskõikd_toiduained(info)
    
    for widget in kuvasisu_frame.winfo_children():
        widget.destroy()
     
    for rida, toit in enumerate(väärtused[võti]):
        var = BooleanVar()#kontrollib checkbuttoni seisundit
        kuvasisu = Checkbutton(kuvasisu_frame, text=toit, variable=var)
        kuvasisu.grid(row=rida, column=0 ,sticky="w")
    

#Kast kuhu kuvatakse sisu 
def nuppude_loomine():
    nuppude_pealkirjad = dieedile_vaskõikd_toiduained(info)
    for rida, võti in enumerate(nuppude_pealkirjad.keys()):
        nupp = Button(root, text=võti, command=lambda v=võti: dieedi_toitude_kuvamine(v))
        #lambda - nupu vajutamisel funktsioonile dieedi_toitude_kuvamine võtme
        nupp.grid(row=rida, column=1, padx=10, pady=5, sticky="w")

    
def valitud():
    valik = dieet_valik.get() # Vaatab, mis väärtuse valis kasutaja
        
    if valik:
        #Pärast valiku tegemist kustutatakse dieedi valiku osa
        check1.grid_forget()
        check2.grid_forget()
        check3.grid_forget()
        minu_nupp.grid_forget()
        nuppude_loomine() 
    else:
        minu_pealkiri.config(text="Sa ei valinud midagi")

#kõigil on sama variable dieet_valik, sest tegemist on RAdiobuttoniga 
check1 = Radiobutton(root, text="Vegan", variable=dieet_valik, value="vegan")
check1.grid(row=0, column=1, columnspan=2, pady=(50, 10), sticky="ew")

check2 = Radiobutton(root, text="Vegetarian", variable=dieet_valik, value="vegeterian")
check2.grid(row=1, column=1, columnspan=2, pady=(50, 10), sticky="ew")

check3 = Radiobutton(root, text="kõik", variable=dieet_valik, value="kõik")
check3.grid(row=2, column=1, columnspan=2, pady=(50, 10), sticky="ew")

minu_nupp = Button(root, text= "Sisesta", command=valitud)
minu_nupp.grid(row=3, column=3,columnspan=2, pady=(10, 10), sticky="ew")

root.mainloop()






