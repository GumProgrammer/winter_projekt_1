let Distance = 0
let _4digit : grove.TM1637 = null
basic.forever(function on_forever() {
    
    Distance = grove.measureInCentimeters(DigitalPin.C16)
})
basic.forever(function on_forever2() {
    
    _4digit = grove.createDisplay(DigitalPin.C16, DigitalPin.C17)
    _4digit.show(input.temperature())
    pins.digitalWritePin(DigitalPin.P0, 0)
    pins.digitalWritePin(DigitalPin.P0, 1)
})
basic.forever(function on_forever3() {
    if (10 >= Distance) {
        motors.dualMotorPower(Motor.A, -100)
        motors.dualMotorPower(Motor.B, 100)
    } else {
        motors.dualMotorPower(Motor.AB, 100)
    }
    
})
