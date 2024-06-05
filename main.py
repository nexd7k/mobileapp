from flet import *
from appdb.database import *
from telas.tela_login import Login
from telas.tela_cadastro import Cadastro
from telas.atualizar_cliente import AtualizarCliente
from telas.atualizar_advogado import AtualizarAdvogado
from telas.complemento_cliente import ComplementarCliente
from telas.complemento_advogado import ComplementarAdvogado
from telas.tela_advogado import Advogado
from telas.tela_cliente import Cliente
from telas.tela_penal import Penal
from telas.tela_civil import Civil
from telas.perfil_cliente import PerfilCliente
from telas.navcom import bar_item_cli, bar_item_adv
from telas.tela_cri import TelaCrime
from telas.tela_ind import TelaInden
from telas.tela_dam import TelaDanos
from telas.tela_hom import TelaHomicidios

def main(page: Page):
    page.title = "App Mobile Coding"
    page.vertical_alignment = MainAxisAlignment.CENTER
    page.horizontal_alignment = CrossAxisAlignment.CENTER

    tabela_user() #Iniciando o banco de dados

    menuadv = PopupMenuButton(
        items=[
            PopupMenuItem(
                content=Row(
                    [
                        Icon(icons.SETTINGS, colors.BLACK),
                        Text("Atualizar informações"),
                    ]
                ),  on_click=lambda _: page.go("/atualizaradvogado")
            ),
            PopupMenuItem(
                content=Row(
                    [
                        Icon(icons.LOGOUT, colors.BLACK),
                        Text("Logout"),
                    ]
                ),  on_click=lambda _: page.go("/")
            )
        ])
    
    menucli = PopupMenuButton(
        items=[
            PopupMenuItem(
                content=Row(
                    [
                        Icon(icons.SETTINGS, colors.BLACK),
                        Text("Atualizar informações"),
                    ]
                ),  on_click=lambda _: page.go("/atualizarcliente")
            ),
            PopupMenuItem(
                content=Row(
                    [
                        Icon(icons.LOGOUT, colors.BLACK),
                        Text("Logout"),
                    ]
                ),  on_click=lambda _: page.go("/")
            )
        ])
        
    def route_change(route): #Função para mudar de pagina
        page.views.clear()
    #Listando todas as paginas
        if page.route == "/":
            page.views.append(
                View(
                    '/',
                    [
                        AppBar(title=Text("Login"), bgcolor=colors.BLUE),
                        Login(page)
                    ], scroll = ScrollMode.AUTO
                )

            )

        if page.route == "/cadastro":
            page.views.append(
                View(
                    '/cadastro',
                    [
                        AppBar(title=Text("Cadastro"), bgcolor=colors.BLUE),
                        Cadastro(page),
                    ], scroll = ScrollMode.AUTO
                )
            )

        if page.route == "/atualizarcliente":
            page.views.append(
                View(
                    '/atualizarcliente',
                    [
                    AppBar(IconButton(icon = icons.ARROW_BACK, on_click=lambda _: page.go("/perfilcliente")), title=Text("Atualizar"), bgcolor=colors.BLUE),
                    AtualizarCliente(page)
                    ], scroll = ScrollMode.AUTO
                )
            )

        if page.route == "/atualizaradvogado":
            page.views.append(
                View(
                    '/atualizaradvogado',
                    [
                    AppBar(IconButton(icon = icons.ARROW_BACK, on_click=lambda _: page.go("/advogado")), title=Text("Atualizar"), bgcolor=colors.BLUE),
                    AtualizarAdvogado(page)
                    ], scroll = ScrollMode.AUTO
                )
            )

        if page.route == "/complementocliente":
            page.views.append(
                View(
                    '/complementocliente',
                    [
                    AppBar(title=Text("Cadastro"), bgcolor=colors.BLUE),
                    ComplementarCliente(page)
                    ], scroll = ScrollMode.AUTO
                )
            )

        if page.route == "/complementoadvogado":
            page.views.append(
                View(
                    '/complementoadvogado',
                    [
                    AppBar(title=Text("Cadastro"), bgcolor=colors.BLUE),
                    ComplementarAdvogado(page)
                    ], scroll = ScrollMode.AUTO
                )
            )

        if page.route == "/advogado":
            page.views.append(
                View(
                    '/advogado',
                    [
                        AppBar(title=Text("Home"), bgcolor=colors.BLUE, actions= [menuadv]),
                        Advogado(page),
                        bar_item_adv(page)
                    ], scroll = ScrollMode.AUTO
                )
            )

        if page.route == "/cliente":
            page.views.append(
                View(
                    '/cliente',
                    [
                        AppBar(title=Text("Home"), bgcolor=colors.BLUE),
                        Cliente(page),
                        bar_item_cli(page)
                    ], scroll = ScrollMode.AUTO
                )
            )

        if page.route == "/penal":
            page.views.append(
                View(
                    '/penal',
                    [
                        AppBar(IconButton(icon = icons.ARROW_BACK, icon_color = colors.BLACK, on_click=lambda _: page.go("/cliente")), bgcolor=colors.BLUE),
                        Penal(page),
                        bar_item_cli(page)
                    ], scroll = ScrollMode.AUTO
                )
            )

        if page.route == "/civil":
            page.views.append(
                View(
                    '/civil',
                    [
                        AppBar(IconButton(icon = icons.ARROW_BACK, icon_color = colors.BLACK, on_click=lambda _: page.go("/cliente")), bgcolor=colors.BLUE),
                        Civil(page),
                        bar_item_cli(page)
                    ], scroll = ScrollMode.AUTO
                )
            )

        if page.route == "/perfilcliente":
            page.views.append(
                View(
                    '/perfilcliente',
                    [
                    AppBar(title=Text("Perfil"), bgcolor=colors.BLUE, actions= [menucli]),
                    PerfilCliente(page),
                    bar_item_cli(page)
                    ], scroll = ScrollMode.AUTO
                )
            )
        
        if page.route == "/telacri":
            page.views.append(
                View(
                    '/telacri',
                    [
                        AppBar(bgcolor=colors.BLUE),
                        TelaCrime(page),
                        bar_item_cli(page)
                    ], scroll = ScrollMode.AUTO
                )
            )

        if page.route == "/telaind":
            page.views.append(
                View(
                    '/telaind',
                    [
                        AppBar(bgcolor=colors.BLUE),
                        TelaInden(page),
                        bar_item_cli(page)
                    ], scroll = ScrollMode.AUTO
                )
            )
        
        if page.route == "/teladam":
            page.views.append(
                View(
                    '/teladam',
                    [
                        AppBar(bgcolor=colors.BLUE),
                        TelaDanos(page),
                        bar_item_cli(page)
                    ], scroll = ScrollMode.AUTO
                )
            )
        
        if page.route == "/telahom":
            page.views.append(
                View(
                    '/telahom',
                    [
                        AppBar(bgcolor=colors.BLUE),
                        TelaHomicidios(page),
                        bar_item_cli(page)
                    ], scroll = ScrollMode.AUTO
                )
            )

        page.update()

    def view_pop(view):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)

    page.on_route_change = route_change
    page.on_view_pop = view_pop
    page.go(page.route)

app(target=main)