from tkinter import *
import time
import threading
import multiprocessing
import tkinter

window=Tk()
window.title("코로나예방 손씻기 프로그램")
window.geometry("700x700")
window.resizable(True,True)

introlabel = Label(window, text="★손씻고 코로나 예방하자☆",font=("궁서체",30),fg="blue")
introlabel.pack()   

def process1():
    sec = 30
    
    label = Label(window, text="30초 손씻기 타이머를 시작합니다.",font=("바탕체",20),fg="blue")
    label.pack() 
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
    label.pack_forget()

def process2():
    root=tkinter
    image=tkinter.PhotoImage(file="손씻기.gif")
    label=tkinter.Label(window,image=image)
    label.pack()
    root.mainloop()

def process3():
    
    
    p3label = Label(window, text="알림을 받을 주기를 선택해주세요(1시간, 2시간, 3시간)",font=("바탕체",10),fg="red")
    p3bt1=Button()
    p3bt2=Button()
    p3bt3=Button()

    def maketimestring( strlen ) :
        result = ""
        for i in range(strlen):
            result+="■"
            if(i%30 == 29):
                result +="\n"
        print(strlen)
        return result
    
    def printtimestring( sec ):

        
        #while은 반복문으로 sec가 0이 되면 반복을 멈춰라
        while (sec != 0 ):
            timestring = maketimestring(sec)
            #timelabel = Label(window, text=timestring,font=("바탕체",10),fg="black")
            #timelabel.pack() 
            sec = sec-1
            time.sleep(1)
            #timelabel.destroy()

    def distorybutton():
        p3label.destroy()
        p3bt1.destroy()
        p3bt2.destroy()
        p3bt3.destroy()

    def p3start1():
        distorybutton()
        p3label = Label(window, text="1시간 알람을 설정하셨습니다",font=("바탕체",10),fg="red")
        p3label.pack()
        printtimestring(6)
        p3label.destroy()

        p3label = Label(window, text="손씻을 시간입니다",font=("바탕체",10),fg="red")
        p3label.pack()

        
    def p3start2():
        distorybutton()
        p3label = Label(window, text="2시간 알람을 설정하셨습니다",font=("바탕체",10),fg="red")
        p3label.pack()
        printtimestring(12)
        p3label.destroy()

        p3label = Label(window, text="손씻을 시간입니다",font=("바탕체",10),fg="red")
        p3label.pack()

        
    def p3start3():
        distorybutton()
        p3label = Label(window, text="3시간 알람을 설정하셨습니다",font=("바탕체",10),fg="red")
        p3label.pack()
        printtimestring(18)
        p3label.destroy()

        p3label = Label(window, text="손씻을 시간입니다",font=("바탕체",10),fg="red")
        p3label.pack()

    p3label.pack() 
    p3bt1=Button(window,text="1시간", bg="light green", command=p3start1)
    p3bt2=Button(window,text="2시간", bg="light blue", command=p3start2)
    p3bt3=Button(window,text="3시간", bg="light gray", command=p3start3)
            
    p3bt1.pack(pady=5)
    p3bt2.pack(pady=5)
    p3bt3.pack(pady=5)



def start1():
    t = threading.Thread(target=process1)
    t.daemon = True 
    t.start()

def start3():
    t1 = threading.Thread(target=process3)
    t1.daemon = True 
    t1.start()

if __name__ == "__main__": 

    bt1=Button(window,text="손씻기 시작", bg="light green", command = start1)
    bt2=Button(window,text="손씻기 방법", bg="light blue", command = process2)
    bt3=Button(window,text="손씻기 알림", bg="light gray", command = start3)
            
    bt1.pack(pady=5)
    bt2.pack(pady=5)
    bt3.pack(pady=5)


    window.mainloop()

