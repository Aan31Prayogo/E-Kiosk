import flet as ft
import time

class SplashView(ft.Column):
    def __init__(self, page:ft.Page):
        super().__init__()
        self.page = page
        # self.run_pb()
        
    def build(self):
        self.pb = ft.ProgressBar(
            width= 250,
            color="amber",
        )
        
        return ft.Column(
            height= 400,
            width= self.page.window.width,
            alignment= ft.MainAxisAlignment.CENTER,
            horizontal_alignment= ft.CrossAxisAlignment.CENTER,
            controls= [
                ft.Lottie(
                    src= "https://lottie.host/dcca68d7-9ebd-4f3e-b6d7-8727a9ce93f1/Fyw3nCns5J.json",
                    reverse= False,
                    repeat= True
                ),
                ft.Text(
                    "Preparing your delightful dishes...",
                    color="#403f3c",
                    size= 18,
                    weight= ft.FontWeight.W_300,
                    italic= True
                ),
                self.pb            
            ]
        )
        