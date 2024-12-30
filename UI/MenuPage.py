import flet as ft


class MenuPage(ft.Column):
    def __init__(self,page):
        super().__init__()
        self.page = page
        
    def build(self):
        
        #NOTE - TAB MENU
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
        
        #NOTE - TAB CONTENT
        
        #NOTE - ROW SUMMARY
        row_summary = ft.Container(
            alignment= ft.alignment.center_left,
            width= 820,
            height= 65,
            bgcolor= "#edb009",
            content= ft.Row(
                alignment = ft.MainAxisAlignment.SPACE_BETWEEN,
                vertical_alignment= ft.CrossAxisAlignment.CENTER,
                controls=[
                    ft.Column(
                        width = 80,
                        alignment = ft.MainAxisAlignment.CENTER,
                        horizontal_alignment = ft.CrossAxisAlignment.END,
                        spacing = 5,
                        controls=[
                            ft.Text("IDR : ", color="black", weight=ft.FontWeight.W_700),
                            ft.Text("Item(s) : ", color="black", weight=ft.FontWeight.W_700)
                        ]
                    ),
                    
                    ft.TextButton(
                        text= "NEXT",
                        icon= ft.icons.NAVIGATE_NEXT,
                        style= ft.ButtonStyle(
                            color= "black"
                        )
                    )
                    
                ]
            )
        )
        
        view_menu_page = ft.Column(
            width= self.page.window.width,
            controls=[
                row_tab_menu,
                row_summary
            ],
            spacing= 100
            
        )
        
        return view_menu_page