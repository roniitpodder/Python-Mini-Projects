import os
import tkinter as tk

WORKTIME = 25*60
BREAKTIME=5*60

WORKCOLOR="#B92828"
BREAKCOLOUR="#85C9E8"

class Pomodoro:
    def __init__(self,root):
        self.root=root
        self.root.title="Pomodoro Timer"
        self.root.geometry("450x350")
        self.root.config(bg=WORKCOLOR)

        current_dir = os.path.dirname(__file__)
        icon_path = os.path.join(current_dir, "clock.png")
        self.icon=tk.PhotoImage(file=icon_path)
        self.root.iconphoto(False,self.icon)

        self.timeLeft=WORKTIME
        self.isRunning=False
        self.isWorkTime=True


        self.modeLabel=tk.Label(root, text="WORK", font=("Times New Roman",20,"bold"), bg=WORKCOLOR, fg="#E8E3E3")
        self.modeLabel.pack(pady=10)

        self.timerLabel=tk.Label(root,text="25:00", font=("Times New Roman",50), bg=WORKCOLOR, fg="black")
        self.timerLabel.pack(pady=20)

        self.startButton=tk.Button(root, text="Start", font=("Times New Roman",10),command=self.startTimer,bg="#B5B5B5", width=15)
        self.startButton.pack()

        self.pauseButton=tk.Button(root, text="Pause", font=("Times New Roman",10),command=self.pauseTimer,bg="#B5B5B5", width=15)
        self.pauseButton.pack(pady=15)

        self.resetButton=tk.Button(root, text="Reset", font=("Times New Roman",10),command=self.resetTimer,bg="#B5B5B5", width=15)
        self.resetButton.pack()

        self.switchButton=tk.Button(root, text="Switch Mode", font=("Times New Roman",10),command=self.switchMode,bg="#B5B5B5", width=15)
        self.switchButton.pack(pady=15)


    def startTimer(self):
        if not self.isRunning:
            self.isRunning=True
            self.countdown()
        
    def pauseTimer(self):
        self.isRunning=False

    def countdown(self):
        if self.timeLeft>0 and self.isRunning:
            mins,secs=divmod(self.timeLeft,60)
            self.timerLabel.config(text=f"{mins:02d}:{secs:02d}")
            self.timeLeft-=1
            self.root.after(1000, self.countdown)
        elif self.timeLeft==0:
            self.root.bell()
            self.switchMode()

    def switchMode(self):
        self.isRunning=False

        if self.isWorkTime:
            self.timeLeft=BREAKTIME
            self.root.config(bg=BREAKCOLOUR)
            self.modeLabel.config(text="BREAK",bg=BREAKCOLOUR)
            self.timerLabel.config(bg=BREAKCOLOUR)
            
        else:
            self.timeLeft=WORKTIME
            self.root.config(bg=WORKCOLOR)
            self.modeLabel.config(text="WORK",bg=WORKCOLOR)
            self.timerLabel.config(bg=WORKCOLOR)

        self.isWorkTime=not self.isWorkTime

        mins,secs=divmod(self.timeLeft,60)
        self.timerLabel.config(text=f"{mins:02d}:{secs:02d}")

    def resetTimer(self):
        self.isRunning=False
        self.timeLeft=WORKTIME
        self.isWorkTime=True

        self.root.config(bg=WORKCOLOR)
        self.modeLabel.config(text="WORK", bg=WORKCOLOR)
        self.timerLabel.config(bg=WORKCOLOR)
        self.timerLabel.config(text="25:00")

root=tk.Tk()
app=Pomodoro(root)
root.mainloop()
