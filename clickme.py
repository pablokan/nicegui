from nicegui import ui

def noti():
    ui.notify('You clicked me!')

#ui.button('Click me!', on_click=lambda: ui.notify('You clicked me!'))
ui.button('Click me!', on_click=noti)

ui.run()