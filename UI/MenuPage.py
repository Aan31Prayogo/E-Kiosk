import flet as ft
import json
import os
from UI.CardMenuTemplate import CardMenuTemplate

PATH_JSON = os.path.join(os.getcwd(), "json_file")

with open(os.path.join(PATH_JSON, "food.json"), "r") as file_main_course:
    json_main_course = json.load(file_main_course)['data']
    
with open(os.path.join(PATH_JSON, "beverages.json"), "r") as file_beverages:
    json_beveragees = json.load(file_beverages)['data']
        
with open(os.path.join(PATH_JSON, "side_dish.json"), "r") as file_side_dish:
    json_side_dish = json.load(file_side_dish)['data']
        
with open(os.path.join(PATH_JSON, "add_on.json"), "r") as file_add_on:
    json_add_on = json.load(file_add_on)['data']

class MenuPage(ft.Column):
    def __init__(self, page):
        if page is None:
            raise ValueError("Page instance cannot be None.")
        super().__init__()
        self.page = page

    def get_content_tab(self, e):
        global content_menu_row
        index = int(e.data)        
        content_menu_row.content.controls.clear()
        if index == 0:        #Main course
            for data__ in json_main_course:
                content_menu_row.content.controls.append(
                    CardMenuTemplate(self.page, data__)
            )
        elif index == 1:  #beverages
            for data__ in json_beveragees:
                content_menu_row.content.controls.append(
                    CardMenuTemplate(self.page, data__)
            )
        elif index==2: #side dish
             for data__ in json_side_dish:
                content_menu_row.content.controls.append(
                    CardMenuTemplate(self.page, data__)
            )
            
        elif index==3: #add-on
             for data__ in json_add_on:
                content_menu_row.content.controls.append(
                    CardMenuTemplate(self.page, data__)
            )
            
            
        content_menu_row.update()

    def build(self):
        global content_menu_row
        
        tab_main_course = ft.Tab(
            text="Main Course",
        )

        tab_side_dish = ft.Tab(
            text="Side Dish",
        )

        tab_beverages = ft.Tab(
            text="Beverages",
        )

        tab_add_on = ft.Tab(
            text="Add - on",
        )

        #NOTE - ROw containt tab
        row_tab_menu = ft.Container(
            width=self.page.window.width,
            height=50,
            alignment= ft.alignment.center_left,
            content=ft.Tabs(
                selected_index=0,
                divider_height=0,
                animation_duration=300,
                indicator_color="#edb009",
                label_color="black",
                unselected_label_color="#b5b4b1",
                tabs=[tab_main_course,
                      tab_beverages,
                      tab_side_dish, 
                      tab_add_on],
                on_change=lambda e: self.get_content_tab(e),
            ),
        )
        
        content_menu_row = ft.Container(
            width=self.page.window.width,
            height=650,
            alignment= ft.alignment.top_left,
            content= ft.Row(
                alignment= ft.MainAxisAlignment.CENTER,
                run_spacing= 20,
                spacing= 20,
                height= 650,
                wrap= True,
                width= self.page.window.width,
                scroll=ft.ScrollMode.ADAPTIVE,
                controls=[]
            )
        )

        #NOTE - Summary row
        row_summary = ft.Container(
            alignment=ft.alignment.center_left,
            width=820,
            height=65,
            bgcolor="#383838",
            content=ft.Row(
                alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                vertical_alignment=ft.CrossAxisAlignment.CENTER,
                controls=[
                    ft.Column(
                        width=80,
                        alignment=ft.MainAxisAlignment.CENTER,
                        horizontal_alignment=ft.CrossAxisAlignment.END,
                        spacing=5,
                        controls=[
                            ft.Text("IDR : ", color="white", weight=ft.FontWeight.W_700),
                            ft.Text("Item(s) : ", color="white", weight=ft.FontWeight.W_700),
                        ],
                    ),
                    ft.TextButton(
                        text="NEXT",
                        icon=ft.icons.NAVIGATE_NEXT,
                        style=ft.ButtonStyle(color="white"),
                    ),
                ],
            ),
        )

        #NOTE - Main view
        view_menu_page = ft.Column(
            width=self.page.width,
            controls=[row_tab_menu, content_menu_row, row_summary],
            spacing=0,
        )
        
        for data__ in json_main_course:
            content_menu_row.content.controls.append(
                CardMenuTemplate(self.page, data__)
            )    

        return view_menu_page
