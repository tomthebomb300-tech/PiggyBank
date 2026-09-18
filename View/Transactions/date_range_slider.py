import customtkinter as ctk
from datetime import timedelta

class Date_range_slider(ctk.CTkFrame):

    def __init__(self, parent, start_date, end_date, command=None):
        super().__init__(parent, fg_color="transparent")

        self.command = command

        self.min_date = start_date
        self.max_date = end_date
        self.total_days = (end_date - start_date).days
        self.start_day = 0
        self.end_day = self.total_days
        
        self.canvas = ctk.CTkCanvas(self,height=90,bg="#1d2228",highlightthickness=0)
        self.canvas.pack(fill="x", expand=True)

        self.canvas.bind("<Configure>", self.redraw)    
        self.canvas.bind("<Button-1>", self.click)      
        self.canvas.bind("<B1-Motion>", self.drag)       

        self.active_handle = None

    def redraw(self, event=None):
        self.canvas.delete("all")
        w = self.canvas.winfo_width()
        left = 30
        right = w - 30
        track_y = 55

        self.canvas.create_line(left, track_y, right, track_y, fill="#5A5A5A", width=6)

        sx = self.day_to_x(self.start_day)
        ex = self.day_to_x(self.end_day)

        self.canvas.create_line(sx,track_y,ex,track_y,fill="#84CC16",width=6)

        self.canvas.create_oval(sx-8, track_y-8,sx+8, track_y+8,fill="#222",outline="#888")
        self.canvas.create_oval(ex-8, track_y-8,ex+8, track_y+8,fill="#222",outline="#888")

        start = self.min_date + timedelta(days=self.start_day)
        end = self.min_date + timedelta(days=self.end_day)
        self.canvas.create_text(sx,20,text=start.strftime("%d/%m/%y"),fill="white")
        self.canvas.create_text(ex,20,text=end.strftime("%d/%m/%y"),fill="white")

    def day_to_x(self, day):
        left = 30
        right = self.canvas.winfo_width() - 30
        return left + (day / self.total_days) * (right - left)


    def x_to_day(self, x):
        left = 30
        right = self.canvas.winfo_width() - 30
        x = max(left, min(right, x))
        return round((x-left) / (right-left) * self.total_days)

    def click(self, event):
        sx = self.day_to_x(self.start_day)
        ex = self.day_to_x(self.end_day)

        if abs(event.x - sx) < 15:
            self.active_handle = "start"
        elif abs(event.x - ex) < 15:
            self.active_handle = "end"
        else:
            self.active_handle = None

    def drag(self, event):
        if not self.active_handle:
            return

        day = self.x_to_day(event.x)

        if self.active_handle == "start":
            self.start_day = min(day, self.end_day)
        else:
            self.end_day = max(day, self.start_day)

        self.redraw()
        if self.command:
            self.command(self.min_date + timedelta(days=self.start_day),self.min_date + timedelta(days=self.end_day))