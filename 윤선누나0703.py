from tkinter import *
import time
import threading
import tkinter

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
    b = 0;
    
    label2 = Label(window, text="알림을 받을 주기를 선택해주세요(1시간, 2시간, 3시간) : ",font=("바탕체",10),fg="red")

    def corona_alarm():
        time.sleep(b)
        

    def command1():
        b = 5
        
        label2.pack_forget()
        bt1.pack_forget()
        bt2.pack_forget()
        bt3.pack_forget()

        time.sleep(b)

        label = Label(window, text=" 손씻으세요 ",font=("바탕체",20),fg="red")
        label.pack() 
        

        
        
        
    def command2():
        b = 10
        label2.pack_forget()
        bt1.pack_forget()
        bt2.pack_forget()
        bt3.pack_forget()

        time.sleep(b)

        label = Label(window, text=" 손씻으세요 ",font=("바탕체",20),fg="red")
        label.pack() 
        
    def command3():
        b = 20
        label2.pack_forget()
        bt1.pack_forget()
        bt2.pack_forget()
        bt3.pack_forget()

        time.sleep(b)

        label = Label(window, text=" 손씻으세요 ",font=("바탕체",20),fg="red")
        label.pack() 

    
    label2.pack() 
    bt1=Button(window,text="1시간", bg="light green", command=command1)
    bt2=Button(window,text="2시간", bg="light blue", command=command2)
    bt3=Button(window,text="3시간", bg="light gray",command=command3)
            
    bt1.pack(pady=5)
    bt2.pack(pady=5)
    bt3.pack(pady=5)



def start1():
    t = threading.Thread(target=process1)
    t.daemon = True 
    t.start()


def start3():
    t = threading.Thread(target=process3)
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
bt3=Button(window,text="손씻기 알림", bg="light gray",command=start3)
           
bt1.pack(pady=5)
bt2.pack(pady=5)
bt3.pack(pady=5)

window.mainloop()