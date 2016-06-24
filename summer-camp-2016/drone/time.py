import time

current_milli_time = lambda: int(round(time.time() * 1000))

lastTime = current_milli_time()
secondsCounter = 0

while True:
    nowTime = current_milli_time()
    if (nowTime - lastTime) > 1000:
        secondsCounter += 1
        print secondsCounter
        lastTime = nowTime