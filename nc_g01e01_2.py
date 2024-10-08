from nicegui import ui

def sumar(*args):
    try:
        nums = [float(n.value) for n in args]
        result.set_text(f'Resultado: {sum(nums)}')
    except:
        result.set_text('Tenés que poner solamente números')

li = []
for x in range(3):
    li.append(ui.input(f'Número {x+1}'))

result = ui.label('Aquí irá el resultado')
ui.button('Sumar', on_click=lambda: sumar(*li))

ui.run()