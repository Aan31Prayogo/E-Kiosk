import flet as ft
from typing import List
from Utility import utility


def spacer(height__):
    return ft.Container(
        height= height__,
        width=400
    )
class RowData(ft.Column):
    def __init__(self, page: ft.Page, index:int, data:dict):
        super().__init__()
        self.page = page
        self.data = data
        self.index = index
        
    
    def build(self):
        return ft.Column(
            width = self.page.window.width,
            height= 50,
            controls= [
                ft.Row(
                    width= self.page.window.width,
                    height= 60,
                    alignment=ft.MainAxisAlignment.START,
                    spacing = 50,
                    controls=[
                        ft.Text(f"     {self.index}", color="#403f3c", size=16, text_align=ft.TextAlign.START, weight= ft.FontWeight.W_400),
                        ft.Text(f"{self.data['item_name']}", color="#403f3c", size=16, text_align=ft.TextAlign.START, weight= ft.FontWeight.W_400, width=90, max_lines=2),
                        ft.Text(f"{self.data['qty']}", color="#403f3c", size=16, text_align=ft.TextAlign.START, weight= ft.FontWeight.W_400),
                        ft.Text(f" {self.data['price']/1000}00",color="#403f3c", size=16, text_align=ft.TextAlign.START, weight= ft.FontWeight.W_400),
                        ft.Text(f" {self.data['total_price']/1000}00", color="#403f3c", size=16, text_align=ft.TextAlign.START, weight= ft.FontWeight.W_400)
                    ]
                ),
                ft.Divider(
                    height=2,
                    color= "black"
                )
            ]
        )
        

class DetailSummary(ft.Column):
    def __init__(self, page: ft.Page, cust_name:str):
        super().__init__()
        self.page = page
        self.cust_name = cust_name
        self.total_items = 0
        self.grand_total = 0
        self.control__ =[]
        
        result = utility.get_order_data_by_name({'customer_name': self.cust_name})        
        
        for idx,val in enumerate(result):
            self.grand_total+=val['total_price']
            self.total_items+=val['qty']
            self.control__ .append(RowData(self.page, idx+1, val))
        
    def build(self):
        self.txt_cust_name = ft.Text(
            f"Cust. Name: {self.cust_name}",
            color="#403f3c", 
            size=16, 
            text_align=ft.TextAlign.START,
            weight= ft.FontWeight.W_400
        )
        
        self.txt_items = ft.Text(
            f"Item(s): {self.total_items}",
            color="#403f3c", 
            size=16, 
            text_align=ft.TextAlign.START,
            weight= ft.FontWeight.W_400
        )
        
        self.txt_grand_total = ft.Text(
            f"Grand Total (IDR) : {self.grand_total/1000}00" ,
            color="#403f3c", 
            size=16, 
            text_align=ft.TextAlign.START,
            weight= ft.FontWeight.W_400
        )
        
        self.row_txt_info = ft.Row(
            alignment= ft.MainAxisAlignment.START,
            width= self.page.window.width,
            spacing= 60,
            controls=[
                ft.Column(
                    width= 200,
                    alignment= ft.MainAxisAlignment.START,
                    controls= [
                        self.txt_cust_name,
                        self.txt_items
                    ]
                ),
                ft.Column(
                    width= 200,
                    alignment= ft.MainAxisAlignment.START,
                    controls=[
                        ft.Text(""),
                        self.txt_grand_total
                    ]
                )
            ]
        )
        
        
        self.header_list = ft.Container(
            width= self.page.window.width,
            height= 40,
            alignment= ft.alignment.center,
            bgcolor= "#202242",
            padding= 0,
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
        
        self.column_item_list = ft.Column(
            height=300,
            controls= self.control__,
            scroll=ft.ScrollMode.ALWAYS,
        )
            
        
        self.container_view =  ft.Column(
                width= self.page.window.width - 20,
                spacing=10,
                height= 400,
                alignment= ft.MainAxisAlignment.START,
                controls=[
                    self.row_txt_info,
                    ft.Divider(color="black",height=2, thickness=6),
                    spacer(20),
                    self.header_list,
                    self.column_item_list
                ]
                
            )
        
        return self.container_view