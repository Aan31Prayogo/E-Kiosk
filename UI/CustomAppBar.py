import flet as ft

def HeaderAppBar():
    appbar__ = ft.AppBar(
        leading = ft.Icon(ft.icons.STACKED_BAR_CHART_ROUNDED, color="white"),
        leading_width = 20,
        bgcolor = "#2b2b2a",
        title = ft.Text("E-Kiosk Systems", color= "white"),
        elevation= 5,
        actions= [
            ft.IconButton(ft.icons.PERSON_ROUNDED, icon_color="white"),
            ft.Text("By Aan Prayogo", size=10, color= "white")
        ]
    )
    
    return appbar__