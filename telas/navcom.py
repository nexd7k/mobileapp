from flet import *

#Criando a função para criar a navbar e ser chamada em main.py para mostrar a navbar
def bar_item_cli(page):
    #Criando uma função para mudar a pagina pelo index, sendo 0 para cliente e 1 para a pagina de perfil
    def change_page(e, page):
        if e.control.selected_index == 0:
            page.go("/cliente")
            page.update()
        if e.control.selected_index == 1:
            page.go("/perfilcliente")
            page.update()
        page.update()

    #Fazendo a navbar 
    navitem = NavigationBar(on_change = lambda e:change_page(e,page),
                            destinations=[
                                NavigationDestination(icon = icons.HOME, label="Home"),
                                NavigationDestination(icon = icons.PERSON, label="Perfil")
                            ]
                            ) 
    return navitem

def bar_item_adv(page):
    #Criando uma função para mudar a pagina pelo index, sendo 0 para cliente e 1 para a pagina de perfil
    def change_page(e, page):
        if e.control.selected_index == 0:
            page.go("/advogado")
            page.update()
        page.update()
        
    #Fazendo a navbar 
    navitem = NavigationBar(on_change = lambda e:change_page(e,page),
                            destinations=[
                                NavigationDestination(icon = icons.HOME, label="Home"),
                                NavigationDestination(icon = icons.PERSON, label="Perfil")
                            ]
                            ) 
    return navitem