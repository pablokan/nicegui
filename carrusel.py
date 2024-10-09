from nicegui import ui

with ui.carousel(animated=True, arrows=True, navigation=True).props('height=800px'):
    with ui.carousel_slide().classes('p-0'):
        ui.image('mahomes.png').classes('w-[270px]')
    with ui.carousel_slide().classes('p-0'):
        ui.image('chris_jones.jpg').classes('w-[270px]')
    with ui.carousel_slide().classes('p-0'):
        ui.image('kelce.jpeg').classes('w-[270px]')

ui.run()