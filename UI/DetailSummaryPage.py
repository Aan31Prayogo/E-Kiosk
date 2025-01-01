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
    def __init__(self, page: ft.Page, cust_name:str, flag:str):
        super().__init__()
        self.page = page
        self.cust_name = cust_name
        self.total_items = 0
        self.grand_total = 0
        self.control__ =[]
        self.flag = flag
        self.select_table_flag = False
        self.payment_option_flag = False
        
        result = utility.get_order_data_by_name({'customer_name': self.cust_name})        
        
        for idx,val in enumerate(result):
            self.grand_total+=val['total_price']
            self.total_items+=val['qty']
            self.control__ .append(RowData(self.page, idx+1, val))
        
    def __handle_table_number(self,e):
        self.select_table_flag = True
        
    def __handle_payment_option(self,e):
        self.payment_option = True
        
        if self.payment_option and self.select_table_flag:
            self.btn_order.disabled = False
            self.btn_order.style = ft.ButtonStyle(bgcolor="green")
        
        self.page.update()
            
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
        
        self.txt_flag = ft.Text(
            self.flag ,
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
                        self.txt_flag,
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
            height=400,
            controls= self.control__,
            scroll=ft.ScrollMode.ALWAYS,
        )
        
        self.table_number = ft.TextField(
            label="Your Table Number",
            border_color= "#403f3c",
            width=200,
            icon= ft.icons.TABLE_BAR,
            border_width = 2,
            keyboard_type= ft.KeyboardType.NUMBER,
            on_change= lambda e: self.__handle_table_number(e)
        )
        
        self.payment_option= ft.Dropdown(
            border_color="#403f3c",
            border_width=2,
            width=200,
            icon=ft.icons.PAYMENT,
            options=[
                ft.dropdown.Option("Cash"),
                ft.dropdown.Option("QR Code"),
                ft.dropdown.Option("Debit Card"),
            ],
            label="Paymennt Option",
            on_change=lambda e: self.__handle_payment_option(e)
        )
        
        self.row_table_and_payment = ft.Row(
            width = self.page.window.width,
            alignment= ft.MainAxisAlignment.CENTER,
            spacing= 40,
            controls=[
                self.table_number,
                self.payment_option,
            ]
        )
        
        self.btn_order =ft.ElevatedButton(
            width=166,
            height=40,
            text="MAKE ORDER",
            color="white",
            icon=ft.icons.SEND,
            disabled=True,
            on_click=lambda e: print(e),
            style=ft.ButtonStyle(
                bgcolor="gray"
            )
        )
        
        self.row_btn_order = ft.Row(
            alignment= ft.MainAxisAlignment.CENTER,
            width= self.page.window.width,
            controls=[self.btn_order]
        )
        
        self.container_view =  ft.Column(
                width= self.page.window.width - 20,
                spacing=10,
                height= self.page.window.height,
                alignment= ft.MainAxisAlignment.START,
                controls=[
                    self.row_txt_info,
                    ft.Divider(color="black",height=2, thickness=6),
                    spacer(20),
                    self.header_list,
                    self.column_item_list,
                    spacer(10),
                    self.row_table_and_payment,
                    spacer(10),
                    self.row_btn_order
                ]
                
            )
        
        return self.container_view