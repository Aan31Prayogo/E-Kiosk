import flet as ft
from typing import List, Optional


class CardMenuTemplate(ft.Card):
    def __init__(self, page: ft.Page, json_data: dict, selected_data: Optional[List[dict]] = None):
        super().__init__()
        self.page = page
        self.parameter = json_data
        self.title = json_data['name']
        self.origin = json_data['origin']
        self.description = json_data['description']
        self.image_url = json_data['image_url']
        self.amount_total_price = 0
        self.total_qty = 0
        self.order_data = {}
        
        self.price = json_data.get('price', 1000)
        self.display_price = json_data.get('display_price', "IDR 1.000")
        
        
        if selected_data is not None and len(selected_data) > 0:
            for data in selected_data:
                if data['item_name'] == self.title and data['qty']>0:
                    self.total_qty = data['qty']    
                    self.amount_total_price = data['total_price']     

    @property
    def ordered_data(self) -> dict:
        if self.order_data: 
            return self.order_data
        else:
            print("empty ordered data", self.title)
            return {}

# =============================================================================================================================#

    #SECTION - UI
    #NOTE - MainView                
    def build(self):
        self.order_qty = ft.Container(
            width=30,
            height=30,
            border_radius=15,
            visible= False,
            bgcolor = "#403f3d",
            alignment= ft.alignment.center,
            content = ft.Text(
                "",
                color="#ffffff",
                size=18,
                text_align=ft.TextAlign.CENTER,
                weight= ft.FontWeight.W_400
            )
        )
        
        if self.total_qty > 0:
            self.order_qty.visible = True
            self.order_qty.content.value = str(self.total_qty)
        
        self.content = ft.Container(
            width=210,
            height=160,
            padding=10,
            border_radius=ft.border_radius.all(10),
            border=ft.border.all(2, "#e4e4e4"),
            ink=False,
            on_hover=self.on_hover,
            on_click=self.on_click,
            bgcolor="#e4e4e4",
            content = ft.Column(
                spacing=0,
                height=180, 
                controls=[
                    ft.Image(
                        src=self.image_url,
                        width=200,
                        height=100,
                        border_radius=ft.border_radius.all(20),

                    ),
                    ft.Text(self.origin, color="#403f3c", size=12, text_align=ft.TextAlign.START, italic=True),
                    ft.Row(
                        width = 200,
                        controls = [
                            ft.Text(self.title, color="#403f3c", size=18, text_align=ft.TextAlign.START),
                            self.order_qty
                        ],
                        spacing= 50,
                        alignment= ft.MainAxisAlignment.SPACE_BETWEEN
                    )
                ],
                alignment=ft.MainAxisAlignment.START
            ),
        )

        # print(self.title)
        self.elevation = 60
        return self.content
    
    # NOTE - Content Dialog Detail Menu
    def content_detail(self):
        self.qty = ft.TextField(
            value=self.total_qty, 
            text_align=ft.TextAlign.CENTER, 
            width=80,
            border_color="black",
            label= "Qty",
            read_only=True
        )
        self.total_price = ft.Text(self.amount_total_price, color="black", size=18, weight= ft.FontWeight.W_400)

        return ft.Container(
            width= 630,
            height = 250,
            content = ft.Column(
                controls = [
                    ft.Divider(color="black", height=1),
                    ft.Text(self.description, color= "black", size= 18, weight=ft.FontWeight.W_200, italic=True),
                    ft.Row(
                        width= self.page.window.width,
                        controls= [
                            ft.Row(
                                width= 200,
                                controls = [
                                    ft.IconButton(ft.icons.REMOVE, on_click = lambda e: self.minus_click(e)),
                                    self.qty,
                                    ft.IconButton(ft.icons.ADD, on_click = lambda e: self.plus_click(e)),
                                ],
                                alignment=ft.MainAxisAlignment.START,
                                spacing = 10
                            ),
                            ft.Column(
                                controls= [
                                    ft.Text("Total Price"),
                                    self.total_price                      
                                ],
                                alignment= ft.MainAxisAlignment.CENTER
                            )
                        ],
                        alignment= ft.MainAxisAlignment.START,
                        spacing= 80  
                    ),
                ],
                alignment= ft. MainAxisAlignment.START,
                spacing= 30
            ),
        )

    #NOTE - Dialog Detail Menu
    def detail_menu(self):
        global detail_dialog
        
        self.btn_add_to_cart = ft.ElevatedButton(
            "Add to Cart",
            color="white",
            bgcolor="green",
            icon=ft.icons.ADD_SHOPPING_CART,
            icon_color="white",
            disabled=True,
            on_click= lambda e: self.handle_btn_cart(e)
        )
        
        self.btn_cancel = ft.ElevatedButton(
            "Cancel",
            color="white",
            bgcolor="red", 
            icon=ft.icons.CANCEL_ROUNDED, 
            icon_color= "white", 
            on_click= lambda e: self.page.close(detail_dialog)
        )
        
        return ft.AlertDialog(
            modal=True,
            title = ft.Text(self.title + " | "  + self.display_price),
            content = self.content_detail(),
            actions=[
                self.btn_add_to_cart,
                self.btn_cancel
 
            ],
            actions_alignment=ft.MainAxisAlignment.END,
        )
            
# =============================================================================================================================#
    # #NOTE - function update UI        
    def minus_click(self,e):
        self.qty.value = str(int(self.qty.value) - 1)
        self.total_price.value = str(int(self.qty.value) * self.price)
    
        if int(self.qty.value)<=0:
            self.amount_total_price = 0
            self.qty.value = str(self.amount_total_price)
            self.total_price.value = str(self.amount_total_price)
            
            self.btn_add_to_cart.disabled = True
            self.btn_add_to_cart.bgcolor = "gray"

        else:
            self.amount_total_price = int(self.qty.value) * self.price
            self.qty.value = str(int(self.qty.value) - 1)
            self.total_price.value = str(self.amount_total_price)
            
            self.btn_add_to_cart.disabled = False
            self.btn_add_to_cart.bgcolor = "green"

        self.page.update()

    def plus_click(self,e):
        self.qty.value = str(int(self.qty.value) + 1)
        # print(self.amount_total_price)
        self.amount_total_price = int(self.qty.value) * self.price
        self.total_price.value = str(self.amount_total_price/1000) + "00"
        
        self.btn_add_to_cart.disabled = False
        self.btn_add_to_cart.bgcolor = "green"
        
        #assign total from counter
        self.total_qty = int(self.qty.value)
        self.page.update()


    def on_hover(self, e):
        e.control.border = ft.border.all(2, "orange") if e.data == "true" else ft.border.all(3, "transparent")
        self.page.update()
                
    def on_click(self,e):
        global detail_dialog
        
        detail_dialog = self.detail_menu()
        self.page.open (detail_dialog)
        self.page.update()
        # print("clicked !!")

    def handle_btn_cart(self,e):
        global detail_dialog
        global amount_selected_item
        
        if self.total_qty > 0:
            self.order_qty.visible = True
            self.order_qty.content.value = self.total_qty
        
        self.order_data['item_name'] = self.title
        self.order_data['qty'] = self.total_qty
        self.order_data['price'] = self.price
        self.order_data['total_price'] = self.amount_total_price
                    
        self.page.close(detail_dialog)
        self.page.update()
    # =============================================================================================================================#