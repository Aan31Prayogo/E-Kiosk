import flet as ft


class CardMenuTemplate(ft.Card):
    def __init__(self, page, json_data):
        super().__init__()
        self.page = page
        self.title = json_data['name']
        self.origin = json_data['origin']
        self.description = json_data['description']
        self.image_url = json_data['image_url']

    def on_hover(self, e):
        print(e.data)
        e.control.border = ft.border.all(3, "amber") if e.data == "true" else ft.border.all(3, "transparent")
        e.control.update()

    def build(self):
        try:
            self.card_content = ft.Container(
                width=180,
                height=200,
                padding=0,
                border_radius=ft.border_radius.all(10),
                border=ft.border.all(2, "#e4e4e4"),
                ink=True,
                on_hover=self.on_hover,
                bgcolor="#e4e4e4",
                content = ft.Column(
                    height=180, 
                    controls=[
                        ft.Image(
                            src=self.image_url,
                            width=200,
                            height=100,
                        ),
                        ft.Text(self.origin, color="#403f3c", size=12, text_align=ft.TextAlign.START),
                        ft.Text(self.title, color="#403f3c", size=18, text_align=ft.TextAlign.START)
                    ],
                    alignment=ft.MainAxisAlignment.START
                ),
            )

            self.card_menu = ft.Card(
                content=self.card_content,
                elevation=5.3
            )

            # print(self.title, self.origin, self.description, self.image_url)
            return self.card_menu
        except Exception as e:
            print(f"Error {e}")