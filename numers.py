from nicegui import ui, run

def validate_input(input_value):
  """Validates if the input is a number."""
  try:
    float(input_value)
    return True
  except ValueError:
    return False

ui.input(label="Enter a number:", on_change=lambda e: 
    ui.notify(f"Valid number" if validate_input(e.value) else "Invalid input, please enter a number.")
)

ui.run()