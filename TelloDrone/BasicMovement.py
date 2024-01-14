from djitellopy import tello
from time import sleep

drone = tello.Tello()
drone.connect()

print(f'Drone Battery Level: %s' % drone.get_battery())
drone.takeoff()
drone.send_rc_control(0, 50, 0, 0) # Forward 50
sleep(2)
drone.send_rc_control(0, 0, 0, 30) # Turn on Yaw
sleep(2)
drone.send_rc_control(0, 0, 0, 0) #stop
drone.land() # ask to land

