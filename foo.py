from nicegui import ui

def sumar():
    result.set_text(str(float(n1.value)*2))

n1 = ui.input('Primer número')
ui.button('Duplicar', on_click=sumar)
result = ui.label('Resultado: ')

ui.run()
