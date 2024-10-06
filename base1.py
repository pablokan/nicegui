from nicegui import ui

def bg(objeto, color):
    return ui.query(objeto).style(f'background-color: {color}')

def print(msg, size):
    return ui.label(msg).classes(f'text-h{size}')

def box(back_color='white'):
    return ui.card().classes(f'bg-{back_color}')

bg('body', 'magenta')
with box('yellow'):
    print('Título', 1)
    print('Subtítulo', 6)

ui.run()
