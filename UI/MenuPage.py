import flet as ft


class MenuPage(ft.Column):
    def __init__(self,page):
        super().__init__()
        self.page = page
        
    def build(self):
        row_tab_menu = ft.Row(
            width= self.page.window.width,
            alignment= ft.MainAxisAlignment.START,
            controls= [
                ft.Tabs(
                    selected_index=0,
                    divider_height=0,
                    animation_duration=300,
                    indicator_color= "#edb009",
                    label_color = "black",
                    unselected_label_color = "#b5b4b1",
                    tabs=[
                        ft.Tab(
                            text="Main Course"
                        ),
                        ft.Tab(
                            text="Side Dish"
                        ),   ft.Tab(
                            text="Beverages"
                        ),   ft.Tab(
                            text="Add-on"
                        ),

                    ],
                )
            ]
        )
        
        return row_tab_menu