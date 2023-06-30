from engine.files.imports import *


class Event:
    def __init__(self):
        pass

    def keyDown(self, key, window):
        event = window.event
        if event.type == sdl2.SDL_KEYDOWN:
            if event.key.keysym.sym == key:
                return True
        return False
    def keyDownOnce(self, key, window):
        pass


class Keys:
    def __init__(self):
        self.KEY_UNKNOWN = sdl2.SDLK_UNKNOWN
        self.KEY_RETURN = sdl2.SDLK_RETURN
        self.KEY_ESCAPE = sdl2.SDLK_ESCAPE
        self.KEY_BACKSPACE = sdl2.SDLK_BACKSPACE
        self.KEY_TAB = sdl2.SDLK_TAB
        self.KEY_SPACE = sdl2.SDLK_SPACE
        self.KEY_EXCLAIM = sdl2.SDLK_EXCLAIM
        self.KEY_QUOTEDBL = sdl2.SDLK_QUOTEDBL
        self.KEY_HASH = sdl2.SDLK_HASH
        self.KEY_PERCENT = sdl2.SDLK_PERCENT
        self.KEY_DOLLAR = sdl2.SDLK_DOLLAR
        self.KEY_AMPERSAND = sdl2.SDLK_AMPERSAND
        self.KEY_QUOTE = sdl2.SDLK_QUOTE
        self.KEY_LEFTPAREN = sdl2.SDLK_LEFTPAREN
        self.KEY_RIGHTPAREN = sdl2.SDLK_RIGHTPAREN
        self.KEY_ASTERISK = sdl2.SDLK_ASTERISK
        self.KEY_PLUS = sdl2.SDLK_PLUS
        self.KEY_COMMA = sdl2.SDLK_COMMA
        self.KEY_MINUS = sdl2.SDLK_MINUS
        self.KEY_PERIOD = sdl2.SDLK_PERIOD
        self.KEY_SLASH = sdl2.SDLK_SLASH
        self.KEY_0 = sdl2.SDLK_0
        self.KEY_1 = sdl2.SDLK_1
        self.KEY_2 = sdl2.SDLK_2
        self.KEY_3 = sdl2.SDLK_3
        self.KEY_4 = sdl2.SDLK_4
        self.KEY_5 = sdl2.SDLK_5
        self.KEY_6 = sdl2.SDLK_6
        self.KEY_7 = sdl2.SDLK_7
        self.KEY_8 = sdl2.SDLK_8
        self.KEY_9 = sdl2.SDLK_9
        self.KEY_COLON = sdl2.SDLK_COLON
        self.KEY_SEMICOLON = sdl2.SDLK_SEMICOLON
        self.KEY_LESS = sdl2.SDLK_LESS
        self.KEY_EQUALS = sdl2.SDLK_EQUALS
        self.KEY_GREATER = sdl2.SDLK_GREATER
        self.KEY_QUESTION = sdl2.SDLK_QUESTION
        self.KEY_AT = sdl2.SDLK_AT
        self.KEY_LEFTBRACKET = sdl2.SDLK_LEFTBRACKET
        self.KEY_BACKSLASH = sdl2.SDLK_BACKSLASH
        self.KEY_RIGHTBRACKET = sdl2.SDLK_RIGHTBRACKET
        self.KEY_CARET = sdl2.SDLK_CARET
        self.KEY_UNDERSCORE = sdl2.SDLK_UNDERSCORE
        self.KEY_BACKQUOTE = sdl2.SDLK_BACKQUOTE
        self.KEY_a = sdl2.SDLK_a
        self.KEY_b = sdl2.SDLK_b
        self.KEY_c = sdl2.SDLK_c
        self.KEY_d = sdl2.SDLK_d
        self.KEY_e = sdl2.SDLK_e
        self.KEY_f = sdl2.SDLK_f
        self.KEY_g = sdl2.SDLK_g
        self.KEY_h = sdl2.SDLK_h
        self.KEY_i = sdl2.SDLK_i
        self.KEY_j = sdl2.SDLK_j
        self.KEY_k = sdl2.SDLK_k
        self.KEY_l = sdl2.SDLK_l
        self.KEY_m = sdl2.SDLK_m
        self.KEY_n = sdl2.SDLK_n
        self.KEY_o = sdl2.SDLK_o
        self.KEY_p = sdl2.SDLK_p
        self.KEY_q = sdl2.SDLK_q
        self.KEY_r = sdl2.SDLK_r
        self.KEY_s = sdl2.SDLK_s
        self.KEY_t = sdl2.SDLK_t
        self.KEY_u = sdl2.SDLK_u
        self.KEY_v = sdl2.SDLK_v
        self.KEY_w = sdl2.SDLK_w
        self.KEY_x = sdl2.SDLK_x
        self.KEY_y = sdl2.SDLK_y
        self.KEY_z = sdl2.SDLK_z
        self.KEY_CAPSLOCK = sdl2.SDLK_CAPSLOCK
        self.KEY_F1 = sdl2.SDLK_F1
        self.KEY_F2 = sdl2.SDLK_F2
        self.KEY_F3 = sdl2.SDLK_F3
        self.KEY_F4 = sdl2.SDLK_F4
        self.KEY_F5 = sdl2.SDLK_F5
        self.KEY_F6 = sdl2.SDLK_F6
        self.KEY_F7 = sdl2.SDLK_F7
        self.KEY_F8 = sdl2.SDLK_F8
        self.KEY_F9 = sdl2.SDLK_F9
        self.KEY_F10 = sdl2.SDLK_F10
        self.KEY_F11 = sdl2.SDLK_F11
        self.KEY_F12 = sdl2.SDLK_F12
        self.KEY_PRINTSCREEN = sdl2.SDLK_PRINTSCREEN
        self.KEY_SCROLLLOCK = sdl2.SDLK_SCROLLLOCK
        self.KEY_PAUSE = sdl2.SDLK_PAUSE
        self.KEY_INSERT = sdl2.SDLK_INSERT
        self.KEY_HOME = sdl2.SDLK_HOME
        self.KEY_PAGEUP = sdl2.SDLK_PAGEUP
        self.KEY_DELETE = sdl2.SDLK_DELETE
        self.KEY_END = sdl2.SDLK_END
        self.KEY_PAGEDOWN = sdl2.SDLK_PAGEDOWN
        self.KEY_RIGHT = sdl2.SDLK_RIGHT
        self.KEY_LEFT = sdl2.SDLK_LEFT
        self.KEY_DOWN = sdl2.SDLK_DOWN
        self.KEY_UP = sdl2.SDLK_UP
        self.KEY_NUMLOCKCLEAR = sdl2.SDLK_NUMLOCKCLEAR
        self.KEY_KP_DIVIDE = sdl2.SDLK_KP_DIVIDE
        self.KEY_KP_MULTIPLY = sdl2.SDLK_KP_MULTIPLY
        self.KEY_KP_MINUS = sdl2.SDLK_KP_MINUS
        self.KEY_KP_PLUS = sdl2.SDLK_KP_PLUS
        self.KEY_KP_ENTER = sdl2.SDLK_KP_ENTER
        self.KEY_KP_1 = sdl2.SDLK_KP_1
        self.KEY_KP_2 = sdl2.SDLK_KP_2
        self.KEY_KP_3 = sdl2.SDLK_KP_3
        self.KEY_KP_4 = sdl2.SDLK_KP_4
        self.KEY_KP_5 = sdl2.SDLK_KP_5
        self.KEY_KP_6 = sdl2.SDLK_KP_6
        self.KEY_KP_7 = sdl2.SDLK_KP_7
        self.KEY_KP_8 = sdl2.SDLK_KP_8
        self.KEY_KP_9 = sdl2.SDLK_KP_9
        self.KEY_KP_0 = sdl2.SDLK_KP_0
        self.KEY_KP_PERIOD = sdl2.SDLK_KP_PERIOD
        self.KEY_APPLICATION = sdl2.SDLK_APPLICATION
        self.KEY_POWER = sdl2.SDLK_POWER
        self.KEY_KP_EQUALS = sdl2.SDLK_KP_EQUALS
        self.KEY_F13 = sdl2.SDLK_F13
        self.KEY_F14 = sdl2.SDLK_F14
        self.KEY_F15 = sdl2.SDLK_F15
        self.KEY_F16 = sdl2.SDLK_F16
        self.KEY_F17 = sdl2.SDLK_F17
        self.KEY_F18 = sdl2.SDLK_F18
        self.KEY_F19 = sdl2.SDLK_F19
        self.KEY_F20 = sdl2.SDLK_F20
        self.KEY_F21 = sdl2.SDLK_F21
        self.KEY_F22 = sdl2.SDLK_F22
        self.KEY_F23 = sdl2.SDLK_F23
        self.KEY_F24 = sdl2.SDLK_F24
        self.KEY_EXECUTE = sdl2.SDLK_EXECUTE
        self.KEY_HELP = sdl2.SDLK_HELP
        self.KEY_MENU = sdl2.SDLK_MENU
        self.KEY_SELECT = sdl2.SDLK_SELECT
        self.KEY_STOP = sdl2.SDLK_STOP
        self.KEY_AGAIN = sdl2.SDLK_AGAIN
        self.KEY_UNDO = sdl2.SDLK_UNDO
        self.KEY_CUT = sdl2.SDLK_CUT
        self.KEY_COPY = sdl2.SDLK_COPY
        self.KEY_PASTE = sdl2.SDLK_PASTE
        self.KEY_FIND = sdl2.SDLK_FIND
        self.KEY_MUTE = sdl2.SDLK_MUTE
        self.KEY_VOLUMEUP = sdl2.SDLK_VOLUMEUP
        self.KEY_VOLUMEDOWN = sdl2.SDLK_VOLUMEDOWN
        self.KEY_KP_COMMA = sdl2.SDLK_KP_COMMA
        self.KEY_KP_EQUALSAS400 = sdl2.SDLK_KP_EQUALSAS400
        self.KEY_ALTERASE = sdl2.SDLK_ALTERASE
        self.KEY_SYSREQ = sdl2.SDLK_SYSREQ
        self.KEY_CANCEL = sdl2.SDLK_CANCEL
        self.KEY_CLEAR = sdl2.SDLK_CLEAR
        self.KEY_PRIOR = sdl2.SDLK_PRIOR
        self.KEY_RETURN2 = sdl2.SDLK_RETURN2
        self.KEY_SEPARATOR = sdl2.SDLK_SEPARATOR
        self.KEY_OUT = sdl2.SDLK_OUT
        self.KEY_OPER = sdl2.SDLK_OPER
        self.KEY_CLEARAGAIN = sdl2.SDLK_CLEARAGAIN
        self.KEY_CRSEL = sdl2.SDLK_CRSEL
        self.KEY_EXSEL = sdl2.SDLK_EXSEL
        self.KEY_KP_00 = sdl2.SDLK_KP_00
        self.KEY_KP_000 = sdl2.SDLK_KP_000
        self.KEY_THOUSANDSSEPARATOR = sdl2.SDLK_THOUSANDSSEPARATOR
        self.KEY_DECIMALSEPARATOR = sdl2.SDLK_DECIMALSEPARATOR
        self.KEY_CURRENCYUNIT = sdl2.SDLK_CURRENCYUNIT
        self.KEY_CURRENCYSUBUNIT = sdl2.SDLK_CURRENCYSUBUNIT
        self.KEY_KP_LEFTPAREN = sdl2.SDLK_KP_LEFTPAREN
        self.KEY_KP_RIGHTPAREN = sdl2.SDLK_KP_RIGHTPAREN
        self.KEY_KP_LEFTBRACE = sdl2.SDLK_KP_LEFTBRACE
        self.KEY_KP_RIGHTBRACE = sdl2.SDLK_KP_RIGHTBRACE
        self.KEY_KP_TAB = sdl2.SDLK_KP_TAB
        self.KEY_KP_BACKSPACE = sdl2.SDLK_KP_BACKSPACE
        self.KEY_KP_A = sdl2.SDLK_KP_A
        self.KEY_KP_B = sdl2.SDLK_KP_B
        self.KEY_KP_C = sdl2.SDLK_KP_C
        self.KEY_KP_D = sdl2.SDLK_KP_D
        self.KEY_KP_E = sdl2.SDLK_KP_E
        self.KEY_KP_F = sdl2.SDLK_KP_F
        self.KEY_KP_XOR = sdl2.SDLK_KP_XOR
        self.KEY_KP_POWER = sdl2.SDLK_KP_POWER
        self.KEY_KP_PERCENT = sdl2.SDLK_KP_PERCENT
        self.KEY_KP_LESS = sdl2.SDLK_KP_LESS
        self.KEY_KP_GREATER = sdl2.SDLK_KP_GREATER
        self.KEY_KP_AMPERSAND = sdl2.SDLK_KP_AMPERSAND
        self.KEY_KP_DBLAMPERSAND = sdl2.SDLK_KP_DBLAMPERSAND
        self.KEY_KP_VERTICALBAR = sdl2.SDLK_KP_VERTICALBAR
        self.KEY_KP_DBLVERTICALBAR = sdl2.SDLK_KP_DBLVERTICALBAR
        self.KEY_KP_COLON = sdl2.SDLK_KP_COLON
        self.KEY_KP_HASH = sdl2.SDLK_KP_HASH
        self.KEY_KP_SPACE = sdl2.SDLK_KP_SPACE
        self.KEY_KP_AT = sdl2.SDLK_KP_AT
        self.KEY_KP_EXCLAM = sdl2.SDLK_KP_EXCLAM
        self.KEY_KP_MEMSTORE = sdl2.SDLK_KP_MEMSTORE
        self.KEY_KP_MEMRECALL = sdl2.SDLK_KP_MEMRECALL
        self.KEY_KP_MEMCLEAR = sdl2.SDLK_KP_MEMCLEAR
        self.KEY_KP_MEMADD = sdl2.SDLK_KP_MEMADD
        self.KEY_KP_MEMSUBTRACT = sdl2.SDLK_KP_MEMSUBTRACT
        self.KEY_KP_MEMMULTIPLY = sdl2.SDLK_KP_MEMMULTIPLY
        self.KEY_KP_MEMDIVIDE = sdl2.SDLK_KP_MEMDIVIDE
        self.KEY_KP_PLUSMINUS = sdl2.SDLK_KP_PLUSMINUS
        self.KEY_KP_CLEAR = sdl2.SDLK_KP_CLEAR
        self.KEY_KP_CLEARENTRY = sdl2.SDLK_KP_CLEARENTRY
        self.KEY_KP_BINARY = sdl2.SDLK_KP_BINARY
        self.KEY_KP_OCTAL = sdl2.SDLK_KP_OCTAL
        self.KEY_KP_DECIMAL = sdl2.SDLK_KP_DECIMAL
        self.KEY_KP_HEXADECIMAL = sdl2.SDLK_KP_HEXADECIMAL
        self.KEY_LCTRL = sdl2.SDLK_LCTRL
        self.KEY_LSHIFT = sdl2.SDLK_LSHIFT
        self.KEY_LALT = sdl2.SDLK_LALT
        self.KEY_LGUI = sdl2.SDLK_LGUI
        self.KEY_RCTRL = sdl2.SDLK_RCTRL
        self.KEY_RSHIFT = sdl2.SDLK_RSHIFT
        self.KEY_RALT = sdl2.SDLK_RALT
        self.KEY_RGUI = sdl2.SDLK_RGUI
        self.KEY_MODE = sdl2.SDLK_MODE
        self.KEY_AUDIONEXT = sdl2.SDLK_AUDIONEXT
        self.KEY_AUDIOPREV = sdl2.SDLK_AUDIOPREV
        self.KEY_AUDIOSTOP = sdl2.SDLK_AUDIOSTOP
        self.KEY_AUDIOPLAY = sdl2.SDLK_AUDIOPLAY
        self.KEY_AUDIOMUTE = sdl2.SDLK_AUDIOMUTE
        self.KEY_MEDIASELECT = sdl2.SDLK_MEDIASELECT
        self.KEY_WWW = sdl2.SDLK_WWW
        self.KEY_MAIL = sdl2.SDLK_MAIL
        self.KEY_CALCULATOR = sdl2.SDLK_CALCULATOR
        self.KEY_COMPUTER = sdl2.SDLK_COMPUTER
        self.KEY_AC_SEARCH = sdl2.SDLK_AC_SEARCH
        self.KEY_AC_HOME = sdl2.SDLK_AC_HOME
        self.KEY_AC_BACK = sdl2.SDLK_AC_BACK
        self.KEY_AC_FORWARD = sdl2.SDLK_AC_FORWARD
        self.KEY_AC_STOP = sdl2.SDLK_AC_STOP
        self.KEY_AC_REFRESH = sdl2.SDLK_AC_REFRESH
        self.KEY_AC_BOOKMARKS = sdl2.SDLK_AC_BOOKMARKS
        self.KEY_BRIGHTNESSDOWN = sdl2.SDLK_BRIGHTNESSDOWN
        self.KEY_BRIGHTNESSUP = sdl2.SDLK_BRIGHTNESSUP
        self.KEY_DISPLAYSWITCH = sdl2.SDLK_DISPLAYSWITCH
        self.KEY_KBDILLUMTOGGLE = sdl2.SDLK_KBDILLUMTOGGLE
        self.KEY_KBDILLUMDOWN = sdl2.SDLK_KBDILLUMDOWN
        self.KEY_KBDILLUMUP = sdl2.SDLK_KBDILLUMUP
        self.KEY_EJECT = sdl2.SDLK_EJECT
        self.KEY_SLEEP = sdl2.SDLK_SLEEP
