import flet as ft

class CardMenuTemplate(ft.Card):
    def __init__(self, page, json_data):
        super().__init__()
        self.page = page
        self.title = json_data['name']
        self.origin = json_data['origin']
        self.description = json_data['description']
        self.image_url = json_data['image_url']
        self.amount_total_price = 0
        self.total_qty = 0
        
        if json_data.get('price'):
            self.price = json_data['price']
        else:
            self.price = 1000
            
        if json_data.get('display_price'):
            self.display_price = json_data['display_price']
        else:
            self.display_price = "IDR 1.000"
    
# =============================================================================================================================#

    #SECTION - UI
    #NOTE - MainView                
    def build(self):
        self.content = ft.Container(
            width=180,
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
                    ft.Text(self.title, color="#403f3c", size=18, text_align=ft.TextAlign.START)
                ],
                alignment=ft.MainAxisAlignment.START
            ),
        )

        # print(self.title)
        self.elevation = 60
        return self.content
    
    # NOTE - Content Dialog Detail Menu
    def content_detail(self):
        self.qty = ft.TextField(value="0", text_align=ft.TextAlign.CENTER, width=80)
        self.total_price = ft.Text("0", color="black", size=18, weight= ft.FontWeight.W_400)

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
                            self.total_price                      
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
        
        return ft.AlertDialog(
            modal=True,
            title = ft.Text(self.title + " | "  + self.display_price),
            content = self.content_detail(),
            actions=[
                ft.ElevatedButton("Add to Cart", color="white", bgcolor="green", icon= ft.icons.ADD_SHOPPING_CART, icon_color="white"),
                ft.ElevatedButton("Cancel", color="white", bgcolor="red", icon=ft.icons.CANCEL_ROUNDED, icon_color= "white", on_click= lambda e: self.page.close(detail_dialog))
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
        else:
            self.amount_total_price = int(self.qty.value) * self.price
            self.qty.value = str(int(self.qty.value) - 1)
            self.total_price.value = str(self.amount_total_price)

        self.qty.update()
        self.total_price.update()

    def plus_click(self,e):
        self.qty.value = str(int(self.qty.value) + 1)
        # print(self.amount_total_price)
        self.amount_total_price = int(self.qty.value) * self.price
        self.total_price.value = str(self.amount_total_price/1000) + "00"
        
        self.qty.update()
        self.total_price.update()
        

    def on_hover(self, e):
        e.control.border = ft.border.all(2, "orange") if e.data == "true" else ft.border.all(3, "transparent")
        e.control.update()
        
    def on_click(self,e):
        global detail_dialog
        
        detail_dialog = self.detail_menu()
        self.page.open (detail_dialog)
        self.page.update()
        # print("clicked !!")

    # =============================================================================================================================#