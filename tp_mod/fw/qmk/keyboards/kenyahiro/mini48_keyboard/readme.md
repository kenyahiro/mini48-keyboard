# mini48-keyboard

A customizable Hotswap keyboard.

* Keyboard Maintainer: [kenyahiro](https://github.com/kenyahiro)

Make example for this keyboard (after setting up your build environment):

    make kenyahiro/mini48-keyboard:default

## Bootloader

Enter the bootloader in 3 ways:

* **Bootmagic reset**: Hold down the key at (0,0) in the matrix
* **Physical reset button**: Double tap the reset button on the back of the PCB
* **Keycode in layout**: Press the key mapped to `QK_BOOT` if it is available

See the [build environment setup](https://docs.qmk.fm/#/getting_started_build_tools) and the [make instructions](https://docs.qmk.fm/#/getting_started_make_guide) for more information. Brand new to QMK? Start with our [Complete Newbs Guide](https://docs.qmk.fm/#/newbs).
