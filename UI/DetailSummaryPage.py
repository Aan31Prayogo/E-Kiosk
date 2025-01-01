import flet as ft
from typing import List

class RowData(ft.Row):
    def __init__(self, page: ft.Page, data:dict):
        super().__init__()
    

class DetailSummary(ft.Container):
    def __init__(self, page: ft.Page, summary_data:List[dict]):
        super().__init__()
        self.page = page
        self.list_data = summary_data
        
        print(self.list_data)
    
    def build(self):
        self.header = ft.Container(
            width= self.page.window.width,
            height= 40,
            alignment= ft.alignment.center,
            bgcolor= "#2b2b2a",
            content=ft.Row(
                width= self.page.window.width,
                height= 40,
                alignment= ft.MainAxisAlignment.START,
                spacing= 50,
                controls=[
                    ft.Text("   No", color="white", size=16, text_align=ft.TextAlign.START, weight= ft.FontWeight.W_600),
                    ft.Text("Item      ", color="white", size=16, text_align=ft.TextAlign.START, weight= ft.FontWeight.W_600),
                    ft.Text("Qty", color="white", size=16, text_align=ft.TextAlign.START, weight= ft.FontWeight.W_600),
                    ft.Text("Price", color="white", size=16, text_align=ft.TextAlign.START, weight= ft.FontWeight.W_600),
                    ft.Text("Sub Total", color="white", size=16, text_align=ft.TextAlign.START, weight= ft.FontWeight.W_600)
                ]
            )
        )
            
        
        self.container_view = ft.Container(
            width= 400,
            height= self.page.window.height,
            alignment= ft.alignment.top_center,
            content = ft.Column(
                width= 400,
                height= self.page.window.height,
                alignment= ft.MainAxisAlignment.CENTER,
                controls=[
                    self.header,
                ]
                
            )
            
        )
        
        return self.container_view