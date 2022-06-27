from flask import Flask
from flask import render_template
import RPi.GPIO as rpi
import time

app= Flask(__name__)

delay = 0.5

led1 = 3
led2 = 5
led3 = 7
led4 = 8
led5 = 10
led6 = 11
led7 = 12
led8 = 13

all_leds = (led1, led2, led3, led4, led5, led6, led7, led8)
north_leds = (led1, led2)
east_leds = (led3, led4)
south_leds = (led5, led6)
west_leds = (led7, led8)

strobo1_1 = (led2,led4)
strobo2_1 = (led5, led6)
strobo1_2 = (led7, led8)
strobo2_2 = (led1, led3)

breaker = False
print(led1)
rpi.setwarnings(False)
rpi.setmode(rpi.BOARD)
rpi.setup(led1, rpi.OUT)
rpi.setup(led2, rpi.OUT)
rpi.setup(led3, rpi.OUT)
rpi.setup(led4, rpi.OUT)
rpi.setup(led5, rpi.OUT)
rpi.setup(led6, rpi.OUT)
rpi.setup(led7, rpi.OUT)
rpi.setup(led8, rpi.OUT)

rpi.output(led1, 0)
print("Done")

@app.route('/')
def index():
    return render_template('webpage.html')

@app.route('/led1')
def led1on():
    rpi.output(led1,0)
    return render_template('webpage.html')

@app.route('/static_on')
def static_on():
    all_off()
    rpi.output(all_leds,0)
    return render_template('webpage.html')

@app.route('/off')
def all_off():
    print('off')
    global breaker
    breaker = True
    rpi.output(all_leds, 1)
    #stop_the_strobo()
    return render_template('webpage.html')

@app.route('/circling_on')
def circling():
    all_off()
    time.sleep(0.5)

    circling(delay)
    return render_template('webpage.html')

@app.route('/strobo_on')
def strobo_on():
    all_off()
    time.sleep(0.5)
    strobo(delay)
    return render_template('webpage.html')

@app.route('/random_on')
def random_on():
    all_off()
    time.sleep(0.5)
    random(delay)
    return render_template('webpage.html')
@app.route('/one_to_eight_on')
def one_to_eight_on():
    all_off()
    time.sleep(0.5)
    one_to_eight(delay)
    return render_template('webpage.html')


@app.route('/160')
def one_sixty():
    global delay
    delay = 0.338
    return render_template('webpage.html')

@app.route('/60')
def sixty():
    global delay
    delay = 1
    return render_template('webpage.html')

@app.route('/100')
def hundred():
    global delay
    delay = 0.6
    return render_template('webpage.html')

@app.route('/120')
def one_twenty():
    global delay
    delay = 0.5
    return render_template('webpage.html')

@app.route('/150')
def one_fifty():
    global delay
    delay = 0.4
    return render_template('webpage.html')

@app.route('/180')
def one_eigthy():
    global delay
    delay = 0.375
    return render_template('webpage.html')

def strobo(d=delay):
    global breaker
    breaker = False
    while True:
        if breaker:
            break
        rpi.output(strobo1_1,1)
        rpi.output(strobo1_2,1)
        rpi.output(strobo2_2,1)
        rpi.output(strobo2_1,1)
        time.sleep(d)
        if breaker:
            break
        rpi.output(strobo1_2,0)
        rpi.output(strobo1_1,0)
        rpi.output(strobo2_2,0)
        rpi.output(strobo2_1,0)
        if breaker:
            break
        time.sleep(d)
        if breaker:
            break
    return

def random(d=delay):
    global breaker
    breaker = False
    while True:
        if breaker:
            break
        rpi.output(north_leds,1)
        rpi.output(south_leds,1)
        rpi.output(east_leds,0)
        rpi.output(west_leds,0)
        if breaker:
            break
        time.sleep(d)
        if breaker:
            break
        rpi.output(north_leds,0)
        rpi.output(south_leds,0)
        rpi.output(east_leds,1)
        rpi.output(west_leds,1)
        time.sleep(d)
        if breaker:
            break
    return

def circling(d=delay):
    global breaker
    breaker = False
    led_list = [led2, led4, led5, led6, led7, led8, led3, led1]
    i=0
    rpi.output(all_leds, 1)
    while True:
        if breaker:
            break
        rpi.output(led_list[i],0)
        time.sleep(d)
        if breaker:
            break
        rpi.output(led_list[i],1)
        i+=1
        if i==8:
            i=0
        if breaker:
            break

def one_to_eight(d=delay):
    global breaker
    breaker = False
    while True:
        if breaker:
            break
        rpi.output(led2,0)
        time.sleep(d)
        if breaker:
            break
        rpi.output(led4,0)
        time.sleep(d)
        if breaker:
            break
        rpi.output(led5,0)
        time.sleep(d)
        if breaker:
            break
        rpi.output(led6,0)
        time.sleep(d)
        if breaker:
            break
        rpi.output(led7,0)
        time.sleep(d)
        if breaker:
            break
        rpi.output(led8,0)
        time.sleep(d)
        if breaker:
            break
        rpi.output(led3,0)
        time.sleep(d)
        if breaker:
            break
        rpi.output(led1,0)
        time.sleep(d)
        if breaker:
            break
        rpi.output(all_leds,1)
        time.sleep(d)

        if breaker:
            break
    return



if __name__=="__main__":
    print("Start")
    for i in range(2):
        rpi.output(all_leds,1)
        time.sleep(0.1)
        rpi.output(all_leds,0)
        time.sleep(0.1)
    app.run(debug=True, host='192.168.0.107')


