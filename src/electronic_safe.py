from hal import hal_lcd as lcd
from hal import hal_keypad as keypad
from hal import hal_buzzer as buzzer
from threading import Thread

lcd = lcd.lcd()
lcd.lcd_clear()
password = "1234"
display2 = "Enter PIN:"
lcd.lcd_display_string("Safe Lock:     ", 1)
lcd.lcd_display_string("Enter PIN:     ", 2)

def key_pressed(key):
    password.append(key)
    print(password)
    lcd.lcd_write(0x01)
    #display2.append("*")
    #lcd.lcd_display_string("hi", 2)



while True:
   

    keypad.init(key_pressed)

    # Start the keypad scanning which will run forever in an infinite while(True) loop in a new Thread "keypad_thread"
    keypad_thread = Thread(target=keypad.get_key)
    keypad_thread.start()



