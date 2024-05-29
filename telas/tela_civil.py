from flet import *
from appdb.database import *

def Civil(page: Page):
    page.vertical_alignment = MainAxisAlignment.CENTER
    page.horizontal_alignment = CrossAxisAlignment.CENTER
    
    #Definindo variáveis e aplicando routing nos botoes
    text_civ = Container(Text("Direito Civil", text_align = alignment.center, size = 40), alignment = alignment.center)
    text_problema = Container(Text("Selecione a categoria específica do problema", text_align = alignment.center, size=20), margin.only(top = 50), alignment = alignment.center)
    btn_cri = Container(ElevatedButton(text="Crime", on_click=lambda _: page.go("/telacri"), height=50, width=400), margin.only(top = 60), alignment = alignment.center)
    btn_hom = Container(ElevatedButton(text="Homicídio", on_click=lambda _: page.go("/telahom"), height=50, width=400), alignment = alignment.center)

    return Column(
        [
            text_civ,
            text_problema,
            btn_cri,
            btn_hom
        ],
    )