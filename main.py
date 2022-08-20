def on_button_pressed_a():
    basic.show_number(randint(0, 6))
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_forever():
    pass
basic.forever(on_forever)
