from machine import Pin
from time import sleep

# Initialize motion detection flag
motion = False

# Interrupt handler function
def handle_interrupt(pin):
    global motion
    global interrupt_pin
    motion = True
    interrupt_pin = pin 

# Set up LED and PIR sensor pins
led = Pin(2, Pin.OUT) # NodeMCU built-in LED
pir = Pin(13, Pin.IN) # GPIO13 NodeMCU pin D7

# Set up interrupt on rising edge of PIR sensor
pir.irq(trigger=Pin.IRQ_RISING, handler=handle_interrupt)

# Main loop
while True:
    if motion:
        print('Motion detected! Interrupt caused by:', interrupt_pin)
        led.value(0) # Turn on LED
        sleep(5) # Wait for 5 seconds
        led.value(1) # Turn off LED
        print('Motion stopped!')
        motion = False # Reset motion detection flag