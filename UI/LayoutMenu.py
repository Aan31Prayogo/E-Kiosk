import flet as flet

class LayoutMenu(ft.Row):
    def __init__(self, page):
        super().__init__()
        self.page = page
        
        self.spacing = 10
        self.wrap = True
        self.con