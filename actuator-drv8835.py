from pololu_drv8835_rpi import motors, MAX_SPEED

# init
def init(default_speed=50):
    motors.setSpeeds(0, 0)
    set_speed(default_speed)

# throttle
cur_speed = MAX_SPEED

def set_speed(speed):
    global cur_speed
    speed = int(MAX_SPEED * speed / 100)
    cur_speed = min(MAX_SPEED, speed)

def get_speed():
    return int(cur_speed * 100 / MAX_SPEED)

def stop():
    motors.motor2.setSpeed(0)
        
def ffw():
    motors.motor2.setSpeed(cur_speed)

def rew():
    motors.motor2.setSpeed(-cur_speed)

# steering
def center():
    motors.motor1.setSpeed(0)
def left():
    motors.motor1.setSpeed(MAX_SPEED)
def right():
    motors.motor1.setSpeed(-MAX_SPEED)

# exit    
def turn_off():
    stop()
    center()
