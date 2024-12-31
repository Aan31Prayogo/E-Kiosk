import flet as ft
from Utility import utility
from UI.HomePage import HomePage
from UI.CardMenuTemplate import CardMenuTemplate
from UI.MenuPage import MenuPage
import UI.CustomAppBar as CustomAppBar


WINDOW_COLOR = "#fefefe"
def main(page: ft.Page):
    screen_res = utility.get_screen_resolution() 
    page.window.width = 480
    page.window.height = 820
    page.window.top = 0
    page.window.left = screen_res[0] - page.window.width
    page.window.title_bar_hidden = True
    page.window.always_on_top = True    
    page.window.frameless = True
    page.window.bgcolor = WINDOW_COLOR
    page.bgcolor = WINDOW_COLOR
    page.vertical_alignment = ft.alignment.center
    page.padding = 0
    page.theme_mode = ft.ThemeMode.LIGHT
    
    def route_change(route):
        page.views.clear()
        route = page.route

        if route =="/":
            current_route = route
        else:
            current_route = "/" + route.split("/")[1]
                
        if current_route =="/":
            page.views.append( ft.View("/",[
                        CustomAppBar.HeaderAppBar(),
                        HomePage(page)
                    ],
                )
            )
        elif current_route=="/MenuPage":   
            page.views.append( ft.View( "/MenuPage", [
                        CustomAppBar.HeaderAppBar(),
                        MenuPage(page,route.split("/")[2]),
                    ]
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

if __name__ == '__main__':
    ft.app(target=main)
