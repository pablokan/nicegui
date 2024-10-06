from nicegui import ui

def sumar():
    try:
        num1 = float(n1.value)
        num2 = float(n2.value)
        result.set_text(f'Resultado: {num1 + num2}')
    except:
        result.set_text('Tenés que poner solamente números')

n1 = ui.input('Primer número')
n2 = ui.input('Segundo número')
ui.button('Sumar', on_click=sumar)
result = ui.label('Resultado: ')

ui.run()
