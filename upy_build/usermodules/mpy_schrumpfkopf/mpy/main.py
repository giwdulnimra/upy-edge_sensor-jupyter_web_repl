# test for corehead MicroPython-module
import corehead, time

LED_PIN = 45
print("...creating console-object")
my_console = corehead.console()
print("...creating led-object")
my_led = corehead.led(LED_PIN)

my_console.info("putting Pin %d high", LED_PIN)
my_led.on()
status_bool = my_led.status()   # checking LED-Status with modul intern function
print("Python verification: LED is", "ON" if status_bool else "OFF")

time.sleep(5)

my_console.info("putting Pin %d low", LED_PIN)
my_led.off()
status_bool = my_led.status()
print("Python verification: LED is", "ON" if status_bool else "OFF")
