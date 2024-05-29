from flet import *
from appdb.database import *
from time import sleep

def ComplementarCliente(page: Page):    
    page.vertical_alignment = MainAxisAlignment.CENTER
    page.horizontal_alignment = CrossAxisAlignment.CENTER

    def complementar(e):
        usuario1 = page.session.get("user") #Recebendo os dados do usuario 

        if nome.value and idade.value:
            # Atualizar os dados do usuário no banco de dados
            cursor.execute("UPDATE Usuario SET nome = ?, idade = ? WHERE id = ?", 
                        (nome.value, idade.value, usuario1[0]))
            conn.commit() #Aplicando as mudanças
            txt_acerto.visible = True
            nome.value = ''
            idade.value = ''
            page.update()

            # Buscando o usuário atualizado no banco de dados

            usuario1 = cursor.execute("SELECT * FROM Usuario WHERE id = ?", (usuario1[0],)) #Buscando o usuário no banco
            usuario1 = cursor.fetchone()

            sleep(1) #Esperar 1 segundo antes de ir pra proxima tela

            page.session.set("user", usuario1)
            page.go("/cliente")
        else:
            # Se algum campo estiver vazio, exiba uma mensagem de erro
            txt_erro.visible = True

    #Definindo as variaveis
    txt_atualizar = Container(Text('Complementar informações', size=20), alignment=alignment.center, padding=20)
    txt_nome = Container(Text('Nome: '))
    nome = TextField(label='Insira seu nome...', text_align=TextAlign.LEFT)
    txt_idade = Container(Text('Idade: '))
    idade = TextField(label='Insira seu idade...', text_align=TextAlign.LEFT)
    btn_enviar = Container(ElevatedButton('Enviar', height=50, width=110, on_click = complementar), alignment= alignment.center)
    txt_acerto = Container(Text('Cadastro atualizado com sucesso!'), visible = False, bgcolor=colors.GREEN, padding=10, alignment=alignment.center)
    txt_erro = Container(Text('Por favor, preencha todos os campos.'), visible=False, bgcolor=colors.RED, padding=10, alignment=alignment.center)
    

    return Column(
        [
            txt_atualizar,
            txt_nome,
            nome,
            txt_idade,
            idade, 
            btn_enviar,
            txt_acerto,
            txt_erro
        ]
    )