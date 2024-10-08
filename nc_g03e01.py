# Pedir el ingreso de 10 números. Contar los mayores de 23 y 
# almacenar los que cumplen la condición.  
# Mostrar la cantidad y los números guardados.


from nicegui import ui

def contarM23(*args):
    try:
        nums = [float(n.value) for n in args]
        result.set_text(f'Resultado: {sum(nums)}')
    except:
        result.set_text('Tenés que poner solamente números')

li = []
for x in range(5):
    li.append(ui.input(f'Número {x+1}'))

result = ui.label('Aquí irá el resultado')
ui.button('Sumar', on_click=lambda: contarM23(*li))

ui.run()