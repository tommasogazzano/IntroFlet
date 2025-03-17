from time import sleep

import flet as ft

def main(page: ft.Page):

    myCounter = ft.Text(value="")
    page.controls.append(myCounter)

    #1) Scrivere del testo -- OUT
    myText = ft.Text( value = "Buongiorno!", color = "blue", size =30)

    #page.controls --> lista [] vuota che contiene tutti i controlli della pagina -> possiamo aggiungere myText
    page.controls.append(myText) #--> non printa niente se non aggiorno la pagina
    page.update()

    #2) Creare un campo in cui l'utente può scrivere del testo -- IN / OUT

    txtIn = ft.TextField(label = "Name",
                         value = "Tommaso",
                         color = "green",
                         disabled = False) # se True non si può cambiare il value
    #page.controls.append(txtIn)
    #page.update()
    page.add(txtIn) #--> assieme l'append e l'update



    #3) Creare dei button -> alla pressione di un bottone eseguo del codice -- IN

    def handleBtnSaluta(e): #e -> oggetto di tipo evento che contiene tutte le info dell'interazione dell'utente con il button
        txtOut.value = f"Ciao {txtIn.value}!"
        page.update()

    btn = ft.Button(text = "Saluta", on_click=handleBtnSaluta, bgcolor="Green", color = "white") #text è la stringa indicata nel bottone
    txtOut = ft.Text(value = "Come ti chiami?")

    row3 = ft.Row(controls = [btn, txtOut])

    page.add(row3)

    #4) Creare un menù a tendina -- IN

    dd = ft.Dropdown(label = "Opzioni",
                     hint_text="Seleziona un Opzione",
                     options= [ft.dropdown.Option("Opzione 1"), ft.dropdown.Option("Opzione 2"), ft.dropdown.Option("Opzione 3")])
    for i in range(3, 20):
        dd.options.append(ft.dropdown.Option(f"Opzione {i}"))
    page.add(dd)


    #5) Visualizzare lunghi elenchi di testo -- OUT
    def handleAddLV(e):
        if txtIn2.value == "":
            lv.controls.append(ft.Text("Errore, aggiungi una stringa valida nel campo", color = "red"))
            page.update()
        else:
            lv.controls.append(ft.Text(txtIn2.value))
            page.update()


    txtIn2 = ft.TextField(label ="Stringa Input")
    btn1 = ft.CupertinoButton(text = "Aggiungi a ListView", on_click=handleAddLV, bgcolor="Purple", color = "white")

    row5 = ft.Row(controls = [txtIn2, btn1], alignment= ft.MainAxisAlignment.CENTER)
    lv = ft.ListView(expand = 1,  spacing = 10, padding = 20, auto_scroll = False)
    page.add(row5, lv)


    for i in range(100):
        myCounter.value = f"Counter: {i}"
       # myCounter.color = ft.colors.random()
        page.update()
        sleep(0.5)  # aspetta 1 sec tra un valore e l'altro -> così si stampa in app

    # finché non finisce il ciclo non va avanti!!

ft.app(target = main, view = ft.AppView.FLET_APP) #default setting
#ft.app(target = main, view = ft.AppView.WEB_BROWSER)