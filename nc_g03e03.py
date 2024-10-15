from nicegui import ui

nombres = []
sexos = []
nombres_mujeres = []

def agregar_dato():
    nombre = nombre_input.value
    sexo = sexo_select.value
    if nombre and sexo:
        nombres.append(nombre)
        sexos.append(sexo)
        nombre_input.value = ''
        nombre_input.run_method('focus')  # Enviamos el foco de vuelta al input del nombre
    else:
        ui.notify('Por favor, ingrese nombre y seleccione sexo', color='warning')

def finalizar():
    global nombres_mujeres
    nombres_mujeres = [nombre for nombre, sexo in zip(nombres, sexos) if sexo == 'Mujer']
    resultado.text = f'Nombres de mujeres: {", ".join(nombres_mujeres)}'
    agregar_button.disable()
    finalizar_button.disable()

with ui.column():
    ui.label('Ingrese nombres y sexos:')
    with ui.row():
        nombre_input = ui.input(label='Nombre')
        sexo_select = ui.select(['Hombre', 'Mujer'], label='Sexo')
    with ui.row():
        agregar_button = ui.button('Agregar', on_click=agregar_dato)
        finalizar_button = ui.button('Finalizar', on_click=finalizar)
    resultado = ui.label()

ui.run()