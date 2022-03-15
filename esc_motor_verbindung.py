import time
import RPi.GPIO as GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

GPIO.setup(7, GPIO.OUT)

p = GPIO.PWM(7, 50)

p.start(0)
print ("starting 0")
time.sleep(3)

p.ChangeDutyCycle(0)
time.sleep(5)



while True:
#	i = 7
# 	while i<8: 
# 		
# 		print(i)
	p.ChangeDutyCycle(7)

# 		i +=.02
	
# 	while i>4:
# 		print(i)
# 		p.ChangeDutyCycle(i)
# 		time.sleep(.05)
# 		i -=.05