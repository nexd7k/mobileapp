from flet import *
from appdb.database import *

def Penal(page: Page):
    page.vertical_alignment = MainAxisAlignment.CENTER
    page.horizontal_alignment = CrossAxisAlignment.CENTER

    #Definindo variáveis e aplicando routing nos botoes
    text_pen = Container(Text("Direito Penal", text_align = alignment.center, size = 40), alignment = alignment.center)
    text_problema = Container(Text("Selecione a categoria específica do problema", text_align = alignment.center, size=20), margin.only(top = 50), alignment = alignment.center)
    btn_ind = Container(ElevatedButton(text="Indenização", on_click=lambda _: page.go("/telaind"), height=50, width=400), margin.only(top = 60), alignment = alignment.center)
    btn_dam = Container(ElevatedButton(text="Danos Morais", on_click=lambda _: page.go("/teladam"), height=50, width=400), alignment = alignment.center)

    return Column(
        [
            text_pen,
            text_problema,
            btn_ind,
            btn_dam
        ],
    )