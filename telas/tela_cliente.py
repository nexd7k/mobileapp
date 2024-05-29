from flet import *
from appdb.database import *

def Cliente(page: Page):
    page.vertical_alignment = MainAxisAlignment.CENTER
    page.horizontal_alignment = CrossAxisAlignment.CENTER

    #Definindo variáveis e aplicando routing nos botoes
    text_cli = Container(Text("Olá, Cliente!", text_align = alignment.center, size = 30))
    text_problema = Container(Text("Com qual área você está tendo problemas?", text_align = alignment.center, size=20), margin.only(top = 50), alignment = alignment.center)
    btn_penal = Container(ElevatedButton(text="Direito Penal", on_click=lambda _: page.go("/penal"), height=50, width=400), margin.only(top = 60), alignment = alignment.center)
    btn_civil = Container(ElevatedButton(text="Direito Civil", on_click=lambda _: page.go("/civil"), height=50, width=400), alignment = alignment.center)

    return Column(
        [
            text_cli,
            text_problema,
            btn_penal,
            btn_civil
        ],
    )