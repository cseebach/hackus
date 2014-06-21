__author__ = 'Cameron Seebach'

import pyglet

from hackus.console import Console
from hackus.system import System

window = pyglet.window.Window(800, 600)

pyglet.font.add_file('Inconsolata.ttf')

console = Console(window, "Inconsolata")

system = System(console)

window.push_handlers(console)
console.schedule()

system.boot()

pyglet.app.run()
