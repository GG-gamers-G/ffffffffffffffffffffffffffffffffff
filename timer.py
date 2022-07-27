import time

def coutdown_timer(seconds):
    while seconds > 0:
        minute = int(seconds/59)
        second = int(seconds%59)
        timer = f'{minute}:{second}'
        print (timer) 
        time.sleep(1)
        seconds -=1
    print("ERR ID 10T")
seconds=input("when do we do the hit ;)")

coutdown_timer(int(seconds))


       
