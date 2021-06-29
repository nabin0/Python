import rotatescreen
import time

rotate_screen = rotatescreen.get_primary_display()

n = 5
for i in range(n):
    time.sleep(1)
    rotate_screen.rotate_to(i*90 % 360)
