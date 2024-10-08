from nicegui import ui

def saludar(nombre):
    result.set_text(f'Hola {nombre.value}')

n = ui.input('Nombre')

result = ui.label('Aquí irá el resultado')
ui.button('Saludar', on_click=lambda: saludar(n))

ui.run()