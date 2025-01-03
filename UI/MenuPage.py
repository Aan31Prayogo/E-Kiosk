import flet as ft
import json
import os
from UI.CardMenuTemplate import CardMenuTemplate
from Utility import utility



PATH_JSON = os.path.join(os.getcwd(), "json_file")

with open(os.path.join(PATH_JSON, "food.json"), "r") as file_main_course:
    json_main_course = json.load(file_main_course)['data']
    
with open(os.path.join(PATH_JSON, "beverages.json"), "r") as file_beverages:
    json_beveragees = json.load(file_beverages)['data']
        
with open(os.path.join(PATH_JSON, "side_dish.json"), "r") as file_side_dish:
    json_side_dish = json.load(file_side_dish)['data']
        
with open(os.path.join(PATH_JSON, "add_on.json"), "r") as file_add_on:
    json_add_on = json.load(file_add_on)['data']
    
amount_selected_item = 0
selected_item = []

class MenuPage(ft.Column):
    def __init__(self, page:ft.Page, flag:str, cust_name:str):
        if page is None:
            raise ValueError("Page instance cannot be None.")
        super().__init__()
        self.page = page
        self.flag = flag
        self.cust_name = cust_name                

    def get_content_tab(self, e):
        global content_menu_row
        index = int(e.data)
        
        # get query result after change tab
        # aim to update the ui view
        ordered_data = utility.get_order_data_by_name({'customer_name':self.cust_name})
                
        content_menu_row.content.controls.clear()
        if index == 0:        #Main course
            for data__ in json_main_course:
                content_menu_row.content.controls.append(
                    CardMenuTemplate(self.page, data__, self.cust_name, ordered_data)
            )
        elif index == 1:  #beverages
            for data__ in json_beveragees:
                content_menu_row.content.controls.append(
                    CardMenuTemplate(self.page, data__, self.cust_name, ordered_data)
            )
        elif index==2: #side dish
             for data__ in json_side_dish:
                content_menu_row.content.controls.append(
                    CardMenuTemplate(self.page, data__,self.cust_name, ordered_data)
            )
            
        elif index==3: #add-on
             for data__ in json_add_on:
                content_menu_row.content.controls.append(
                    CardMenuTemplate(self.page, data__, self.cust_name)
            )


        content_menu_row.update()
        
    #NOTE - CAllback btn
    def func_btn_back(self,e):
        utility.delete_data_order()
        self.page.go("/")
    
    def to_detail_page(self,e):
        self.page.go(f"/DetailPage/{self.cust_name}/{self.flag}")

    def build(self):
        global content_menu_row
        global row_btn_and_summary
        
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
            alignment= ft.alignment.center_left,
            padding= 0,
            content= ft.Row(
                alignment= ft.MainAxisAlignment.CENTER,
                run_spacing= 5,
                spacing= 20,
                height= 650,
                wrap= True,
                width= self.page.window.width,
                scroll=ft.ScrollMode.AUTO,
                controls=[]
            )
        )

        #NOTE - Summary row
        row_btn_and_summary = ft.Container(
            alignment=ft.alignment.center_left,
            width=self.page.window.width,
            height=65,
            padding= 0,
            bgcolor="#383838",
            content=ft.Row(
                alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                vertical_alignment=ft.CrossAxisAlignment.CENTER,
                controls=[
                    ft.TextButton(
                        text="BACK",
                        icon=ft.icons.NAVIGATE_BEFORE,
                        style=ft.ButtonStyle(color="white"),
                        on_click= lambda e: self.func_btn_back(e)
                    ),
                    ft.Row(
                        controls = [
                            ft.Text(self.flag + " | " + self.cust_name , color="white", size = 18, weight=ft.FontWeight.W_400),
                            # ft.Column(
                            #     width=80,
                            #     alignment=ft.MainAxisAlignment.CENTER,
                            #     horizontal_alignment=ft.CrossAxisAlignment.START,
                            #     spacing=5,
                            #     controls=[
                            #         ft.Text("IDR : " + str(amount_selected_item), color="white", weight=ft.FontWeight.W_400),
                            #         ft.Text("Item(s) : " + str(len(selected_item)), color="white", weight=ft.FontWeight.W_400),
                            #     ],
                            # ),
                        ]
                    ),
                    ft.TextButton(
                        text="NEXT",
                        icon=ft.icons.NAVIGATE_NEXT,
                        style=ft.ButtonStyle(color="white"),
                        on_click= lambda e: self.to_detail_page(e)
                    ),
                ],
            ),
        )

        #NOTE - Main view
        view_menu_page = ft.Column(
            width=self.page.window.width,
            controls=[ row_tab_menu, content_menu_row, row_btn_and_summary],
            spacing=0,
            alignment= ft.MainAxisAlignment.START
        )
                
        for data__ in json_main_course:
            content_menu_row.content.controls.append(
                CardMenuTemplate(self.page, data__, self.cust_name)
            )    

        return view_menu_page
