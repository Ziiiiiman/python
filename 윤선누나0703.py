from tkinter import *
import time
import threading
import tkinter

def process1():
    print("손씻기 타이머를 시작합니다.")
    sec = 30
    print(sec)
    
    label1 = Label(window, text=str(sec),font=("바탕체",20),fg="red")
    label1.pack() 
    
#while은 반복문으로 sec가 0이 되면 반복을 멈춰라
    while (sec != 0 ):
        sec = sec-1
        time.sleep(1)
        label1.pack_forget()
        label1 = Label(window, text=str(sec),font=("바탕체",20),fg="red")
        label1.pack() 
        #print(sec)
    

def process2():
    root=tkinter
    image=tkinter.PhotoImage(file="손씻기.gif")
    label=tkinter.Label(window,image=image)
    label.pack()
    root.mainloop()

    
def process3():
    import threading
    import time
    b = 0;
    def corona_alarm():
        print("손 씻을 시간입니다. 소독제를 이용해 손을 씻어주세요")
        threading.Timer(b, corona_alarm).start()
    while True:
        a = input("알림을 받을 주기를 선택해주세요(1시간, 2시간, 3시간) : ");
        if (a == '1시간'):
            b = 2.5;
            break;
        elif (a == '2시간'):
            b = 5;
            break;
        elif (a == '3시간'):
            b = 10;
            break;
    corona_alarm();

def start1():
    t = threading.Thread(target=process1)
    t.daemon = True 
    t.start()

window=Tk()
window.title("코로나예방 손씻기 프로그램")
window.geometry("700x700")
window.resizable(True,True)

label1 = Label(window, text="★손씻고 코로나 예방하자☆",font=("궁서체",30),fg="blue")
label1.pack()    

bt1=Button(window,text="손씻기 시작", bg="light green", command=start1)
bt2=Button(window,text="손씻기 방법", bg="light blue", command=process2)
bt3=Button(window,text="손씻기 알림", bg="light gray",command=process3)
           
bt1.pack(pady=5)
bt2.pack(pady=5)
bt3.pack(pady=5)

window.mainloop()