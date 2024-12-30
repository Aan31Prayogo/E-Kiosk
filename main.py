import flet as ft
from Utility import utility
from UI.HomePage import HomePage

WINDOW_COLOR = "#fefefe"

def main(page: ft.Page):
    screen_res = utility.get_screen_resolution() 
    page.window.width = 480
    page.window.height = 820
    page.window.top = 0
    page.window.left = screen_res[0] - page.window.width
    page.window.title_bar_hidden = False
    page.window.always_on_top = False    
    page.window.frameless = True
    page.window.bgcolor = WINDOW_COLOR
    page.bgcolor = WINDOW_COLOR
    page.vertical_alignment = ft.alignment.center
    page.padding = 0
    
    page.appbar = ft.AppBar(
        leading = ft.Icon(ft.icons.STACKED_BAR_CHART_ROUNDED, color="gray"),
        leading_width = 20,
        bgcolor = "#2b2b2a",
        title = ft.Text("E-Kiosk Systems", color
                        = "white"),
        elevation= 5,
        actions= [
            ft.IconButton(ft.icons.PERSON_ROUNDED, icon_color="white"),
            ft.Text("By Aan Prayogo", size=10)
        ]
    )
  
    page.add(HomePage(page))

ft.app(target=main)
