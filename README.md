# Pico PIN bruteforcer

This is my code to have the Raspberry pi Pico emulate a USB keyboard, and automatically attempt all possible 4 digit PINs.



## Installation

Install CircuitPython to Pico, and add the code.py, combos.txt, and adafruid_hid library.

## Roadmap

- Add handling for lockouts for too many attempts.

- Add handling for when Pico correctly guesses PIN.

- Add more choice of PINs to try (e.e choose amount of digits, or popular combinations etc).

- Test on operating systems other than Android 

## Bugs

- On some newer phones, every second attempt results in the third digit being omitted.
