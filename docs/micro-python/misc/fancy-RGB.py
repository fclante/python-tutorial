import machine
import neopixel
import time

# Set the number of neopixels and the GPIO pin to use
num_pixels = 8
gpio_pin = 4

# Create a NeoPixel object on the specified pin
neo_pixel = neopixel.NeoPixel(machine.Pin(gpio_pin), num_pixels)

# Run the RGB demo
def rgbdemo(neo_pixel):
    # Get the number of neopixels
    num_pixels = neo_pixel.n

    # Cycle through red, green, and blue
    for color in [(255, 0, 0), (0, 255, 0), (0, 0, 255)]:
        for i in range(4 * num_pixels):
            for pixel in range(num_pixels):
                neo_pixel[pixel] = (0, 0, 0)
            neo_pixel[i % num_pixels] = color
            neo_pixel.write()
            time.sleep_ms(50)

    # Bounce red, green, and blue
    for color in [(64, 0, 0), (0, 64, 0), (0, 0, 64)]:
        for i in range(4 * num_pixels):
            for pixel in range(num_pixels):
                neo_pixel[pixel] = color
            if (i // num_pixels) % 2 == 0:
                neo_pixel[i % num_pixels] = (0, 0, 0)
            else:
                neo_pixel[num_pixels - 1 - (i % num_pixels)] = (0, 0, 0)
            neo_pixel.write()
            time.sleep_ms(100)

# Call the RGB demo function with the NeoPixel object
rgbdemo(neo_pixel)