import flet as ft

def main(page: ft.Page):
    txtIn = ft.TextField(label = "Aggiungi un elemento qui...",
                         width = 300, color = "blue")

    def handleAdd(e):
        if txtIn.value == "":
            print(f"Il textFiled è vuota!!")
            return
        newCheckBox = ft.Checkbox(label = txtIn.value)
        txtIn.value = ""
        page.add(newCheckBox)

    btnAdd = ft.ElevatedButton(text = "Add", on_click=handleAdd)
    row1 = ft.Row(controls = [txtIn, btnAdd], alignment = ft.MainAxisAlignment.CENTER)
    page.add(row1)


ft.app(target=main)