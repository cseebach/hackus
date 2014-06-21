import pyglet


class Console(object):
    def __init__(self, window, font_name):
        self.window = window
        self.label = pyglet.text.Label('_',
                                       font_name=font_name,
                                       color=(82, 223, 82, 255),
                                       font_size=20,
                                       x=0, y=0, width=window.width,
                                       multiline=True,
                                       anchor_x='left', anchor_y='bottom')

        self.command_length = 0
        self.backspace_down = False

        self.mode = "output"

    def on_draw(self):
        self.window.clear()
        self.label.draw()

    def set_prompt(self, prompt):
        self.prompt = prompt

    def set_input(self):
        self.write(self.prompt)
        self.mode = "input"

    def set_output(self):
        self.mode = "output"

    #input methods
    def on_text(self, text):
        self.label.begin_update()
        self.label.text = self.label.text[:-1] + text + self.label.text[-1]
        self.label.end_update()
        self.command_length += len(text)

    def on_key_press(self, symbol, modifiers):
        if self.mode == "input":
            if symbol is pyglet.window.key.ENTER:
                command = self.label.text[-self.command_length - 1:-1]
                self.command_length = 0
                self.label.begin_update()
                self.label.text = self.label.text[:-1] + "\n" + self.label.text[-1]
                self.label.end_update()
                self.set_output()
                self.system.evaluate_command(command)
        if symbol is pyglet.window.key.BACKSPACE:
            self.backspace_down = True

    def on_key_release(self, symbol, modifiers):
        if symbol is pyglet.window.key.BACKSPACE:
            self.backspace_down = False

    def check_for_backspace(self, ms):
        if self.backspace_down and len(self.label.text) > 3 and self.mode == "input":
            self.label.begin_update()
            self.label.text = self.label.text[:-2] + self.label.text[-1]
            self.label.end_update()
            self.command_length -= 1

    #output methods
    def write(self, message):
        if self.mode == "output":
            self.label.begin_update()
            self.label.text = self.label.text[:-1] + message + self.label.text[-1]
            self.label.end_update()

    #cursor methods
    def cursor_remove(self, ms):
        self.label.begin_update()
        self.label.text = self.label.text[:-1] + " "
        self.label.end_update()
        pyglet.clock.schedule_once(self.cursor_add, .8)

    def cursor_add(self, ms):
        self.label.begin_update()
        self.label.text = self.label.text[:-1] + "_"
        self.label.end_update()
        pyglet.clock.schedule_once(self.cursor_remove, .8)

    #misc methods
    def schedule(self):
        pyglet.clock.schedule_once(self.cursor_remove, .8)
        pyglet.clock.schedule_interval(self.check_for_backspace, .1)

    def set_system(self, system):
        self.system = system