import flet as ft
from UI.MenuPage import MenuPage


class HomePage(ft.Column):
    COLOR_BTN = "#403f3c"
    COLOR_TEXT = "#ffffff"
    
    def __init__(self, page):
        super().__init__() 
        self.page = page

        
    def to_menu_page(self,e, flag):
        print(f"clicked {flag}")
        self.page.controls.clear()
        menu_page = MenuPage(self.page, flag)
        self.page.add(menu_page)
        # self.page.update()
        
    def build(self):    
        btn_dine_in = ft.ElevatedButton(
            width=166,
            height=40,
            text="Dine In",
            bgcolor=self.COLOR_BTN,
            color=self.COLOR_TEXT,
            icon=ft.icons.RESTAURANT_MENU,
            on_click= lambda e: self.to_menu_page(e, flag="DINE IN")
        )

        btn_take_away = ft.ElevatedButton(
            text="Take Away",
            width=166,
            height=40,
            bgcolor=self.COLOR_BTN,
            color=self.COLOR_TEXT,
            icon=ft.icons.LOGOUT_SHARP,
            on_click= lambda e: self.to_menu_page(e, flag="TAKE AWAY")
        )

        column = ft.Column(
            spacing= 20,
            width = self.page.window.width,
            height= self.page.window.height, 
            controls=[btn_dine_in, 
                      btn_take_away],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment= ft.CrossAxisAlignment.CENTER
        )
        
        return column