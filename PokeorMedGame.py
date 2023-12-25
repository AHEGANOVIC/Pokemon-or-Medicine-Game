import tkinter as tk
import random

a0 = ""
a1 = ""
a2 = ""
a3 = ""
a4 = ""
a5 = ""
a6 = ""
a7 = ""
a8 = ""
a9 = ""
a10 = ""
b0 = ""
b1 = ""
b2 = ""
b3 = ""
b4 = ""
b5 = ""
b6 = ""
b7 = ""
b8 = ""
b9 = ""
b10 = ""

root = tk.Tk()
root.title("Pokemon Or Medicine")
root.geometry("1200x1200")

global generated_var
generated_var = tk.StringVar()

global pokemedict
pokemedict = {
    "Fennekin": "Finasteride",
    "Bibarel": "Zemdri",
    "Staravia": "Prevymis",
    "Giratina": "Nuzyra",
    "Luxio": "Mavyret",
    "Solosis": "Delstrigo",
    "Nidoran": "Xofluza",
    "Cryogonal": "Vabomere",
    "Raticate": "Firazyr",
    "Zygarde": "Kalbitor",
    "Gyarados": "Kynamro"
}

def generate():
    global pokemedict
    go = random.randint(0, 10)
    
    if go < 5: 
        x = random.randint(0, 10)
        generated_var.set(list(pokemedict.values())[x])
    else:
        y = random.randint(0, 10)
        generated_var.set(list(pokemedict.keys())[y])

def pokeguess():
    user_guess = "pokemon"
    generated_value = generated_var.get()
    if generated_value in pokemedict.keys() and user_guess == "pokemon":
        answer = tk.Message(text="Correct!", width=200)     
        answer.after(1000, answer.place_forget)
        answer.place(x=500, y=300)
    else:
        answer = tk.Message(text="Wrong!", width=200)     
        answer.after(1000, answer.place_forget)
        answer.place(x=500, y=300)
    
    generated_var.set("")


def medguess():
    user_guess = "medicine"
    generated_value = generated_var.get()
    if generated_value in pokemedict.values() and user_guess == "medicine":
        answer = tk.Message(text="Correct!", width=200)     
        answer.after(1000, answer.place_forget)
        answer.place(x=500, y=300)
    else:
        answer = tk.Message(text="Wrong!", width=200)     
        answer.after(1000, answer.place_forget)
        answer.place(x=500, y=300)
    
    generated_var.set("")
    

button = tk.Button(root, text="Generate medicine name or pokemon name", command=generate)
button.place(x=450, y=50)

pokebutton = tk.Button(root, text="Guess Pokemon", command=pokeguess)
pokebutton.place(x=400, y=200)

medbutton = tk.Button(root, text="Guess Medicine", command=medguess)
medbutton.place(x=600, y=200)

gmessage = tk.Message(root, textvariable=generated_var, width=100)
gmessage.place(x=550, y=150)

generatelabel = tk.Label(root, text="Generated Term:")
generatelabel.place(x=440, y=150)

root.resizable(False, False)

root.mainloop()
