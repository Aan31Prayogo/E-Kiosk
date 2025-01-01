import flet as ft
import time
from Utility import utility
from UI.HomePage import HomePage
from UI.MenuPage import MenuPage
from UI.DetailSummaryPage import DetailSummary
from UI.DetailSummaryPage import DetailSummary
import UI.CustomAppBar as CustomAppBar
from UI.SplashScreen import SplashView

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
                        MenuPage(page,route.split("/")[2],route.split("/")[3]),
                    ]
                )
            )
            
        elif current_route=="/DetailPage":   
            page.views.append( ft.View( "/DetailPage", [
                        CustomAppBar.HeaderAppBar(),
                        DetailSummary(page,route.split("/")[2],route.split("/")[3])
                    ]
                )
            )
        page.update()

    #NOTE - SplashSCreen
    page.add(SplashView(page))
    time.sleep(5)
    page.views.clear()

    def view_pop(view):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)


    page.on_route_change = route_change
    page.on_view_pop = view_pop
    page.go(page.route)
    
if __name__ == '__main__':
    # ft.app(target=main)
    utility.print_receip("adwad")
