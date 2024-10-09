from nicegui import ui

ui.query('body').style(f'background-color: red')
with ui.card().classes(f'bg-yellow'):
    ui.label('Cartel').classes('text-h1')
    ui.label('Cartelito').classes('text-h6')

ui.run()
