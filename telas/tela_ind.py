from flet import *
from appdb.database import *

def TelaInden(page: Page):
    usuario1 = page.session.get("user")
    page.vertical_alignment = MainAxisAlignment.CENTER
    page.horizontal_alignment = CrossAxisAlignment.CENTER

    #Definindo as variaveis
    txt_perf = Container(Text("Com base no seu problema, \n estes são os profissionais mais qualificados", text_align = TextAlign.CENTER, size = 25),
                          margin.only(top=50), alignment= alignment.center) 
    #Imagem genérica para o advogado
    img = Container(Image(src=f"../assets/profilepic_adv.jpg", width=100, height=100, fit=ImageFit.CONTAIN,
                           border_radius= border_radius.all(50)), alignment=alignment.center, padding=25, margin= margin.only(top=20))
    #Descrição do advogado
    txt_dados = Container(Text("Dr. Otávio é um advogado especializado em Danos Morais, porém também trabalha com Indenização. \n"
                               "Conhecido por sua expertise legal e empatia excepcional com os clientes.", 
                               text_align = TextAlign.CENTER), alignment= alignment.center)

    return Column(
        [
            txt_perf,
            img,
            txt_dados
        ]
    )