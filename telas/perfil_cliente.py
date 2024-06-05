from flet import *
from appdb.database import *

def PerfilCliente(page: Page):
    usuario1 = page.session.get("user") #Buscando dados do usuario
    page.vertical_alignment = MainAxisAlignment.CENTER
    page.horizontal_alignment = CrossAxisAlignment.CENTER

    txt_perf = Container(Text("Este é o seu perfil", text_align = alignment.center, size = 25))
    img = Container(Image(src=f"../assets/profilepic_cli.jpg", width=120, height=120, fit=ImageFit.CONTAIN, border_radius= border_radius.all(50)), alignment=alignment.center, padding=25)
    txt_dados = Container(Text(f"{usuario1[2]}, {usuario1[3]} anos", text_align = alignment.center, size=25), alignment= alignment.center)
    

    return Column(
        [
            txt_perf,
            img,
            txt_dados
        ],
    )