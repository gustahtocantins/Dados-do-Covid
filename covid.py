import requests
from bs4 import BeautifulSoup
from tkinter import *
from tkinter import PhotoImage
win = Tk()
win.maxsize(width=500, height=400)
win.minsize(width=500, height=400)
win.title("Dados sobre o Covid-19 no Brasil")
win.config(bg="#fc4630")

#titulo
titulo = Label(win, text="COVID-19 Brazil Tracker",padx=20,pady=20)
titulo["fg"], titulo["bg"] = "white", "#33242b"
titulo["font"] = ("arial", "30", "bold")
titulo.grid()
titulo.place(bordermode=OUTSIDE, x=0, y=0)

Posic = 120
#casos confirmados
confirmado = Label(win, text="Confirmados: ")
confirmado["fg"], confirmado["bg"] = "white", "#fc4630"
confirmado["font"] = ("arial", "25")
confirmado.grid()
confirmado.place(bordermode=OUTSIDE, x=20, y=Posic)

#mortes
mortes = Label(win, text="Mortes: ")
mortes["fg"], mortes["bg"] = "white", "#fc4630"
mortes["font"] = ("arial", "25")
mortes.grid()
mortes.place(bordermode=OUTSIDE, x=20, y=Posic+60)

#recuperados
recuperados = Label(win, text="Recuperados: ")
recuperados["fg"], recuperados["bg"] = "white", "#fc4630"
recuperados["font"] = ("arial", "25")
recuperados.grid()
recuperados.place(bordermode=OUTSIDE, x=20, y=Posic+120)

#pesquisar numeros
def editar():
    url = requests.get("https://www.worldometers.info/coronavirus/country/brazil/")
    html = BeautifulSoup(url.text,"html.parser")
    s = html.find_all("div", {"class":"maincounter-number"})
    confirmado["text"] = f"Confirmados: {s[0].text[1:-1]}"
    mortes["text"] = f"Mortes: {s[1].text[1:-1]}"
    recuperados["text"] = f"Recuperados: {s[2].text[1:-1]}"

#botão
atualizar = Button(win, text="Atualizar", command=editar, border=0)
atualizar["fg"], atualizar["bg"] = "white", "#e30842"
atualizar["font"] = ("arial", "20", "bold")
atualizar.grid()
atualizar.place(bordermode=OUTSIDE, x=170, y=324)

win.mainloop()
