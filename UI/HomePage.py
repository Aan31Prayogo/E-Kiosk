import flet as ft
from UI.MenuPage import MenuPage

class HomePage(ft.Column):
    COLOR_BTN_ENABLED = "#403f3c"
    COLOR_BTN_DISABLED = "#e4e4e4"
    COLOR_TEXT = "#ffffff"
    
    def __init__(self, page):
        super().__init__() 
        self.page = page
        self.flag = ""
        self.customer_name = ""

    def to_menu_page(self,e, flag, cust_name):
        self.page.go(f"/MenuPage/{flag}/{cust_name}")
        # self.page.update()

    def build(self):   
        def handle_field_cust_name(e):
            cust_name = field_customer_name.value
            # print(len(cust_name))
            if len(cust_name)>0:
                btn_dine_in.disabled = False
                btn_take_away.disabled = False
                btn_dine_in.style = ft.ButtonStyle(bgcolor=self.COLOR_BTN_ENABLED)
                btn_take_away.style = ft.ButtonStyle(bgcolor=self.COLOR_BTN_ENABLED)
            else:
                btn_dine_in.disabled = True
                btn_take_away.disabled = True
                btn_dine_in.style = ft.ButtonStyle(bgcolor=self.COLOR_BTN_DISABLED)
                btn_take_away.style = ft.ButtonStyle(bgcolor=self.COLOR_BTN_DISABLED)
                
            self.page.update()
        
        field_customer_name = ft.TextField(
            label= "Enter Your Name",
            width= 200,
            height= 60,
            border_color= self.COLOR_BTN_ENABLED,
            border_radius=4,
            border_width=2,
            on_change= lambda e: handle_field_cust_name(e),
            capitalization=ft.TextCapitalization.CHARACTERS
        )
         
        btn_dine_in = ft.ElevatedButton(
            width=166,
            height=40,
            text="Dine In",
            color=self.COLOR_TEXT,
            icon=ft.icons.RESTAURANT_MENU,
            disabled=True,
            on_click=lambda e: self.to_menu_page(e, flag="DINE IN", cust_name = field_customer_name.value),
            style=ft.ButtonStyle(
                bgcolor=self.COLOR_BTN_DISABLED 
            )
        )

        btn_take_away = ft.ElevatedButton(
            text="Take Away",
            width=166,
            height=40,
            color=self.COLOR_TEXT,
            icon=ft.icons.LOGOUT_SHARP,
            disabled=True,
            on_click=lambda e: self.to_menu_page(e, flag="DINE IN", cust_name = field_customer_name.value),
            style=ft.ButtonStyle(
                bgcolor=self.COLOR_BTN_DISABLED 
            )
        )


        column = ft.Column(
            spacing= 30,
            width = self.page.window.width,
            height= self.page.window.height, 
            controls=[field_customer_name,
                      btn_dine_in, 
                      btn_take_away],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment= ft.CrossAxisAlignment.CENTER
        )
        
        return column