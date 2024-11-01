from kb import KMKKeyboard

from kmk.extensions.stringy_keymaps import StringyKeymaps
from kmk.keys import KC
from kmk.modules.layers import Layers

Mini48 = KMKKeyboard()

Mini48.modules.append(Layers())
Mini48.extensions.append(StringyKeymaps())

MOLYR = KC.MO(1)

# Make this for better looking formatting...
______ = 'NO'

# fmt:off
Mini48.keymap = [[
  # Layer 0 QWERTY
  'TAB',  'Q',    'W',    'E',    'R',    'T',    'Y',    'U',    'I',    'O',   'P',    'BSLS',
  'LCTL', 'A',    'S',    'D',    'F',    'G',    'H',    'J',    'K',    'L',   'SCLN', 'ENT',
  'LSFT', 'Z',    'X',    'C',    'V',    'B',    'N',    'M',    'COMM', 'DOT', 'SLSH', 'RSFT',
  'ESC',  'LGUI', 'LALT', MOLYR,  'SPC',  ______, ______, ______, 'LEFT', 'DOWN', 'UP',  'RGHT',
], [
  # Layer 1
  'TAB',  'Q',    'W',    'E',    'R',    'T',    'Y',    'U',    'I',    'O',   'P',    'BSLS',
  'LCTL', 'A',    'S',    'D',    'F',    'G',    'H',    'J',    'K',    'L',   'SCLN', 'ENT',
  'LSFT', 'Z',    'X',    'C',    'V',    'B',    'N',    'M',    'COMM', 'DOT', 'SLSH', 'RSFT',
  'ESC',  'LGUI', 'LALT', MOLYR,  'SPC',  ______, ______, ______, 'LEFT', 'DOWN', 'UP',  'RGHT',
]]
# fmt:on

if __name__ == '__main__':
    Mini48.go()
