from machine import Pin, PWM
from leaphymicropython.utils.boards_config import pin_to_gpio


def set_pwm(pin: int, value: int, freq: int = 50):
    """Sets a pwm pin
    :param pin: int, the pin to set
    :param value: int, the value to set the pin to
    :param freq: int, the frequency of the pwm
    """
    pin = pin_to_gpio(pin)
    if value < 0 or value > 255:
        raise ValueError("PWM value must be between 0 and 255")
    pwm = PWM(Pin(pin))
    pwm.freq(freq)
    pwm.duty_u16(value * 257)


def read_pwm(pin: int):
    """
    Reads a pwm pin
    :param pin: int, the pin to read
    :return: int, the value of the pin
    """
    pin = pin_to_gpio(pin)
    pwm = PWM(Pin(pin))
    return pwm.duty_u16() / 257


def set_pin(pin: int, value: int):
    """
    Sets a pin
    :param pin: int, the pin to set
    :param value: int, the value to set the pin to
    """
    pin = pin_to_gpio(pin)
    pin = Pin(pin, Pin.OUT)
    if value < 0 or value > 1:
        raise ValueError("Pin values must be in between 0 and 1")
    pin.value(value)


def read_pin(pin: int) -> int:
    """
    Reads a pin
    :param pin: int, the pin to read
    :return: int, the value of the pin
    """
    pin = pin_to_gpio(pin)
    pin = Pin(pin, Pin.IN)
    return pin.value()
