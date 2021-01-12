Distance = 0
_4digit: grove.TM1637 = None

def on_forever():
    global Distance
    Distance = grove.measure_in_centimeters(DigitalPin.C16)
basic.forever(on_forever)

def on_forever2():
    global _4digit
    _4digit = grove.create_display(DigitalPin.C16, DigitalPin.C17)
    _4digit.show(input.temperature())
    pins.digital_write_pin(DigitalPin.P0, 0)
    pins.digital_write_pin(DigitalPin.P0, 1)
basic.forever(on_forever2)

def on_forever3():
    if 10 >= Distance:
        motors.dual_motor_power(Motor.A, -100)
        motors.dual_motor_power(Motor.B, 100)
    else:
        motors.dual_motor_power(Motor.AB, 100)
basic.forever(on_forever3)
