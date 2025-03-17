import flet as ft


def main(page : ft.Page):
    #un tasto "-" per decrementare
    #un textField per visualizzare il valore
    #un tasto "+" per incrementare

    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    def handleAdd(e):
        txtCounter.value += 1
        page.update()

    def handleMinus(e):
        txtCounter.value -= 1
        page.update()


    btnAdd = ft.IconButton(ft.Icons.ADD_CIRCLE, on_click= handleAdd)
    btnMinus = ft.IconButton(ft.Icons.REMOVE_CIRCLE, on_click= handleMinus)
    txtCounter = ft.TextField(value = 0,
                              width = 150,
                              color = "purple",
                              disabled = True,
                              text_align=ft.TextAlign.CENTER)

    row = ft.Row(controls =[btnMinus, txtCounter, btnAdd], alignment = ft.MainAxisAlignment.CENTER)
    page.add(row)



ft.app(target = main)