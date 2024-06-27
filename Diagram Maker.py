from tkinter import *
import matplotlib.pyplot as plt

prozor = Tk()
prozor.config(bg="gold")
prozor.geometry("500x300")
prozor.title("Charts Maker")

lista_imena_redova = []
final_values = []



def stub():
    plt.figure(figsize=(10, 6))
    plt.bar(lista_imena_redova, final_values, color='blue')
    plt.xlabel('Species')
    plt.ylabel('Values')
    plt.title('Bar Chart')
    plt.show()

def linija():
    plt.figure(figsize=(10, 6))
    plt.plot(lista_imena_redova, final_values, marker='o', color='red')
    plt.xlabel('Species')
    plt.ylabel('Values')
    plt.title('Line Chart')
    plt.show()

def krug():
    plt.figure(figsize=(10, 6))
    plt.pie(final_values, labels=lista_imena_redova, autopct='%1.1f%%')
    plt.title('Pie Chart')
    plt.show()

def columns():
    global koliko_kolona, koliko_kolonaE, oke, koliko_podvrsta, koliko_podvrstaE, oke1, broj_kolona
    broj_kolona = int(koliko_kolonaE.get())
    koliko_kolona.destroy()
    koliko_kolonaE.destroy()
    oke.destroy()
    
    koliko_podvrsta = Label(prozor, text="How many subspecies would you like to have?", bg="gold3")
    koliko_podvrsta.place(x=175, y=65)
    
    koliko_podvrstaE = Entry(prozor)
    koliko_podvrstaE.place(x=200, y=150)
    
    oke1 = Button(prozor, text="OK", fg="White", bg="Black", command=imena_redova)
    oke1.place(x=300, y=150)

def imena_redova():
    global koliko_podvrsta, koliko_podvrstaE, oke1, broj_kolona, entry_list, label_list, oke2
    koliko_podvrsta.destroy()
    koliko_podvrstaE.destroy()
    oke1.destroy()
    
    entry_list = []
    label_list = []
    
    y1 = 65
    for i in range(broj_kolona):
        if broj_kolona > 4:
            prozor.geometry("400x600")
        if broj_kolona > 13:
            prozor.geometry("400x800")
        if broj_kolona > 20:
            prozor.geometry("400x1000")
        imena_kolona = Label(prozor, text=f"Type the name of column {i + 1}", bg="gold3")
        imena_kolona.place(x=20, y=y1 + 50 * (i + 1))
        imena_kolonaE = Entry(prozor)
        imena_kolonaE.place(x=200, y=y1 + 50 * (i + 1))
        
        label_list.append(imena_kolona)
        entry_list.append(imena_kolonaE)
        
    oke2 = Button(prozor, text="OK", fg="White", bg="Black", command=podvrste)
    oke2.place(x=350, y=150)
    label_list.append(oke2)

def podvrste():
    global label_list, entry_list, broj_kolona, lista_imena_redova, vrednosti_list, vrednostiE_list, oke3
    for widget in label_list + entry_list:
        if isinstance(widget, Entry):
            lista_imena_redova.append(widget.get())
        widget.destroy()
    
    label_list = []
    entry_list = []
    
    for x in range(broj_kolona):
        vrednosti = Label(prozor, text=f"Enter the value for subspecies {x + 1}", bg="gold3")
        vrednosti.place(x=20, y=65 + x * 50)
        vrednostiE = Entry(prozor)
        vrednostiE.place(x=250, y=65 + x * 50)
        
        label_list.append(vrednosti)
        entry_list.append(vrednostiE)
    
    oke3 = Button(prozor, text="OK", fg="White", bg="Black", command=final_step)
    oke3.place(x=350, y=65 + (broj_kolona * 50))
    label_list.append(oke3)

def final_step():
    global label_list, entry_list, lista_imena_redova, final_values
    try:
        final_values = [float(entry.get()) for entry in entry_list]
    except ValueError:
        print("Please enter valid numbers in all fields.")
        return
    
    for widget in label_list + entry_list:
        widget.destroy()
    
    tekstic = Label(prozor, text="Choose the type of chart you want", bg="gold3")  
    tekstic.place(x=150, y=65)
    
    stubicast_diagram = Button(prozor, text="Bar Chart", fg="White", bg="lightblue", command=stub)
    stubicast_diagram.place(x=200, y=100)

    linijski_dijagram = Button(prozor, text="Line Chart", fg="White", bg="Red2", command=linija)
    linijski_dijagram.place(x=200, y=150)
    
    kruzni_dijagram = Button(prozor, text="Pie Chart", fg="White", bg="Orange3", command=krug)
    kruzni_dijagram.place(x=200, y=200)

pocetni_Tekst = Label(prozor, text="Charts Maker", bg="gold2", fg="Black", font=("Arial", 15))
pocetni_Tekst.place(x=200, y=20)

koliko_kolona = Label(prozor, text="Select how many species you have", bg="gold3")
koliko_kolona.place(x=175, y=65)

koliko_kolonaE = Entry(prozor)
koliko_kolonaE.place(x=200, y=150)

oke = Button(prozor, text="OK", bg="Black", fg="White", command=columns)
oke.place(x=300, y=150)

prozor.mainloop()
