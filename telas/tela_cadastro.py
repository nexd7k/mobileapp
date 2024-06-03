from flet import *
from appdb.database import *
from time import sleep

def Cadastro(page: Page):
    page.vertical_alignment = MainAxisAlignment.CENTER
    page.horizontal_alignment = CrossAxisAlignment.CENTER

    def oab_state(e): #Verificando se foi a seção advogado foi selecionada para mostrar o campo OAB
        decider_value = decider.value
        if decider_value == "advogado":
            txt_oab.visible = True            
            oab.visible = True
            page.update()
        else:
            txt_oab.visible = False 
            oab.visible = False
            page.update()

    def cadastrar(e): #Função de cadastro de usuário        
        decider_value = decider.value
        login_input = login.value
        senha_input = senha.value

        # Verificando se os campos de login e senha não estão vazios
        if login_input.strip() == "" or senha_input.strip() == "":
            txt_erro.visible = True
            page.update()
            return
        
        # Verificando se uma opção foi selecionada
        if decider_value is None:
            txt_erro.visible = True
            txt_erro.content.value = "Por favor, selecione se você é cliente ou advogado"
            page.update()
            return
        
        try: 
            if decider_value == "cliente": #Cadastrando cliente
                cursor.execute("INSERT INTO Usuario (login, senha, cpf) VALUES (?, ?, ?)", (login.value, senha.value, cpf.value))
            else: #Cadastrando advogado
                cursor.execute("INSERT INTO Usuario (login, senha, cpf, oab) VALUES (?, ?, ?, ?)", [login.value, senha.value, cpf.value, oab.value])
            conn.commit()

            usuario1 = cursor.execute("SELECT * FROM Usuario WHERE login = ? AND cpf = ?", (login.value, cpf.value)) #Buscando o usuário no banco
            usuario1 = cursor.fetchone()

            page.session.set("user", usuario1)

            txt_acerto.visible = True
            login.value= ''
            cpf.value = ''
            senha.value = ''
            oab.value = ''
            page.update()

            sleep(1) #Esperar 1 segundo antes de ir pra proxima tela

            if decider_value == "cliente":
                page.go("/complementocliente")
            else:
                page.go("/complementoadvogado")
                
        except sqlite3.IntegrityError:
            txt_erro.visible = True
            txt_erro.content.value = "Login já está em uso"
            page.update()
            

    #Definindo todas as variáveis e aplicando routing no botao voltar
    btn_voltar = Container(ElevatedButton('Voltar', on_click=lambda _: page.go("/"), height=50, width=110))
    txt_registro = Container(Text('Cadastro de Novo Usuário', size=20), alignment=alignment.center, padding=20)
    txt_login = Container(Text('Login: '))
    login = TextField(label='Insira seu login...', text_align=TextAlign.LEFT)
    txt_cpf = Container(Text('CPF: '))
    cpf = TextField(label='Insira seu CPF...', text_align=TextAlign.LEFT)
    txt_senha = Container(Text('Senha: '))
    senha = TextField(label='Insira sua senha...', text_align=TextAlign.LEFT, password=True, can_reveal_password=True)
    btn_enviar = Container(ElevatedButton('Enviar', height=50, width=110, on_click = cadastrar), alignment= alignment.center)
    decider = RadioGroup(content=Row([Radio(value="cliente", label="Cliente"), Radio(value="advogado", label="Advogado")], 
                                      alignment = MainAxisAlignment.CENTER, spacing = 10), on_change= oab_state) #Variavel que da a opção de escolher entre cliente e advogado
    txt_oab = Container(Text('OAB: '), visible=False)
    oab = TextField(label='Insira o número da sua OAB...', text_align=TextAlign.LEFT, visible=False)
    txt_acerto = Container(Text('Cadastro concluído com sucesso!'), visible=False, bgcolor=colors.GREEN, padding=10, alignment=alignment.center)
    txt_erro = Container(Text('Login ou senha inválidos'), visible=False, bgcolor=colors.RED, padding=10, alignment=alignment.center)

    return Column(
        [
            btn_voltar,
            txt_registro,
            txt_login,
            login,
            txt_cpf,
            cpf,
            txt_senha,
            senha,
            btn_enviar,
            decider,
            txt_oab,
            oab,
            txt_acerto,
            txt_erro
        ]
    )
