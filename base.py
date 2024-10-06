from nicegui import ui

def bg(objeto, color):
    return ui.query(objeto).style(f'background-color: {color}')

def print(msg, size):
    return ui.label(msg).classes(f'text-h{size}')    

def box(color):
    return ui.card().classes(f'bg-{color}')

bg('body', 'yellow')
with box('grey'):
    print('Título', 1)
    print('Subtítulo', 6)

ui.run()
