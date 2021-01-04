from pynput.mouse import Listener as MouseListener



def on_move(x, y):
    print("Mouse moved to ({0}, {1})".format(x, y))

def on_click(x, y, button, pressed):
    if pressed:
        pressed_down = True
        print('Mouse clicked at ({0}, {1}) with {2}'.format(x, y, button))
    else:
        pressed_down = False
        print('Mouse released at ({0}, {1}) with {2}'.format(x, y, button))


mouse_listener = MouseListener(on_move=on_move, on_click=on_click)

mouse_listener.start()
mouse_listener.join()