from flet import *
from appdb.database import *

def Login(page: Page):

    def autenticar(e):
        login_input = login.value
        senha_input = senha.value

        # Verificando se os campos de login e senha não estão vazios
        if login_input.strip() == "" or senha_input.strip() == "":
            txt_erro.visible = True
            page.update()
            return
           
        #Executando a Consulta no banco
        usuario1 = cursor.execute("SELECT * FROM Usuario WHERE login = ? AND senha = ?", (login.value, senha.value))

        # Obtenha a primeira linha de resultado
        usuario1 = cursor.fetchone()

        #Verificando se o campo oab na tabela Usuario está vazio ou nao para aplicar o routing corretamente
        if usuario1 != None:
            page.session.set("user", usuario1)
            if usuario1[6] != None:
                page.go("/advogado")
            else:
                page.go("/cliente")
        else:
            txt_erro.visible = True
            page.update()
        
    #Definindo variaveis e aplicando routing no botao de registrar
    img = Container(Image(src=f"../assets/64572.png", width=120, height=120, fit=ImageFit.CONTAIN), alignment=alignment.center, padding=25)
    btn_register = Container(ElevatedButton(text="Registrar", on_click=lambda _: page.go("/cadastro"), height=50, width=110))
    txt_login = Container(Text('Login:'))
    login = TextField(label='Insira o login...', text_align=TextAlign.LEFT)
    txt_senha = Container(Text('Senha:'))
    senha = TextField(label='Insira sua senha...', text_align=TextAlign.LEFT, password=True, can_reveal_password=True)
    btn_entrar = Container(ElevatedButton('Entrar', height=50, width=110, on_click = autenticar), alignment=alignment.center)
    txt_erro = Container(Text('Login ou senha inválidos'), visible=False, bgcolor=colors.RED, padding=10, alignment=alignment.center)


    return Column(
        [
            btn_register,
            img,
            txt_login,
            login,
            txt_senha,
            senha,
            btn_entrar,
            txt_erro
        ],
    )