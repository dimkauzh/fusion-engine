__author__ = "Dimkauzh"
__version__ = "0.2.3"

import fusionengine.files.data as data
import fusionengine.files.systems as sysconfig

from fusionengine.files.imports import *

class Main:
    def __init__(self):
        sdl2.SDL_Init(sdl2.SDL_INIT_VIDEO)
        self.window = window.Window()
        self.color = color.Colors()
        self.event = event.Event()
        self.keys = event.Keys()
        self.draw = draw.Draw()
        self.image = image.Image()
        self.body = body
        self.system = sysconfig.System()
        self.rendereroptions = sysconfig.RendererOptions()
        self.shape = shape.Shapes()
        self.ui = ui.UI()

        self.DEBUGIMAGE = "src/fusionengine/debugfiles/fe.png"

    def quit(self, window):
        sdl2.SDL_DestroyRenderer(window.renderer)
        sdl2.SDL_DestroyWindow(window.window)
        del window
        sdl2.SDL_Quit()
