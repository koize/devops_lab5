import time
from hal import hal_lcd as lcd

lcd = lcd.lcd()
lcd.lcd_clear()

while True:
    local_time = time.localtime()
    time_string = time.strftime("%H:%M:%S     ", local_time)
    date_string = time.strftime("%d/%m/%Y", local_time)
    lcd.lcd_display_string(time_string, 1)
    lcd.lcd_display_string(date_string, 2)
    time.sleep(0.5)
    time_string = time.strftime("%H %M %S     ", local_time)
    lcd.lcd_display_string(time_string, 1)
    time.sleep(0.5)
