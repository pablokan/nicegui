from nicegui import ui


def validar(e):
    if e.value.isdigit():
        result.set_text('you typed: ' + e.value)
    else:
        e.value[:-1]
        result.set_text('you typed: ' + e.value[:-1])
        i.value(e.value[:-1])

def input_number(label):
    i = ui.input(label=label,
         on_change=lambda e: validar(e),
         validation={'No es un dígito': lambda value: value.isdigit()})
    return i

i = input_number('numerito')
result = ui.label()

ui.run()