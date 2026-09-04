import customtkinter as ctk

from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from datetime import datetime

class Month_expenses(ctk.CTkFrame):
    def __init__(self, parent, controller, fg_color, corner_radius):
        super().__init__(parent, fg_color=fg_color, corner_radius=corner_radius)

        self.controller = controller
        self.date = datetime(2025, 8, 1)

        self.create_header(self)
        self.create_chart(self)

    def __get_expenses(self, month, year):
        self.expenses = self.controller.getBiggestExpenses(month, year)

    def update_month(self):
        self.month_label.configure(text = "{0} {1}".format(self.date.strftime("%B %Y"), "Expenses"))


    def last_month(self):
        updated_date = self.date
        if updated_date.month == 1:
            updated_date = updated_date.replace(year=updated_date.year - 1, month=12)
        else:
            updated_date = updated_date.replace(month=updated_date.month - 1)

        self.__get_expenses(updated_date.month, updated_date.year)
        if(len(self.expenses) <= 0):
            return

        self.date = updated_date
        self.update_month()
        self.update_chart()


    def next_month(self):
        updated_date = self.date
        if updated_date.month == 12:
            updated_date = updated_date.replace(year=updated_date.year + 1, month=1)

        else:
            updated_date = updated_date.replace(month=updated_date.month + 1)

        self.__get_expenses(updated_date.month, updated_date.year)
        if(len(self.expenses) <= 0):
            return
        
        self.date = updated_date
        self.update_month()
        self.update_chart()


    def create_header(self, parent):
        header_frame = ctk.CTkFrame(parent, fg_color = "#1d2228")
        header_frame.pack(side = "top", padx = 10, pady = (30, 10), fill = "both", expand = True)

        last_button = ctk.CTkButton(header_frame, text = "<", width = 30, height = 30, fg_color = "transparent", hover_color = "#3A3A3A", command = self.last_month)
        last_button.pack(side = "left", padx = 40)

        self.month_label = ctk.CTkLabel(header_frame, font = ("Arial", 20))
        self.month_label.pack(side = "left", expand = True)
        self.update_month()

        next_button = ctk.CTkButton(header_frame, text = ">", width = 30, height = 30, fg_color = "transparent", hover_color = "#3A3A3A", command = self.next_month)
        next_button.pack(side = "right", padx = 40)


    def create_chart(self, parent):
        self.fig = Figure(figsize=(6, 6), dpi=100, layout = "tight")
        self.ax = self.fig.add_subplot(111)

        self.canvas = FigureCanvasTkAgg(self.fig, master=parent)
        self.canvas.get_tk_widget().pack(fill="both", expand=True, pady=(0,40))

        self.__get_expenses(self.date.month, self.date.year)
        self.update_chart()


    def update_chart(self):
        #convert negative to positive
        for c in self.expenses:
            self.expenses[c] *= -1

        self.ax.clear()   # Remove the old chart

        labels = list(self.expenses.keys())
        values = list(self.expenses.values())

        colors = ["#B8E64C", "#11C5C6", "#8CB4FF", "#9B84F3", "#D6AA19", "#C71B71"]

        wedges, _, autotexts = self.ax.pie(
            values,
            colors=colors[:len(values)],
            startangle=90,
            radius=1.2,
            wedgeprops=dict(width=0.35, edgecolor="#1d2228"),
            autopct="%1.0f%%",
            pctdistance=0.82
        )

        total = round(sum(values),2)
        self.ax.text(0, 0, f"- €{total:,}", ha="center", va="center", fontsize=18, fontweight="bold", color="white")

        self.ax.legend(
            wedges, 
            [f"{label}\n- €{value:,}" for label, value in zip(labels, values)], 
            loc = "upper center", 
            bbox_to_anchor = (0.5, -0.05), 
            ncol = 3,
            frameon = False,
            labelcolor = "white",
            fontsize = 11,
            handlelength = 1.2,
            handletextpad = 0.6,
            columnspacing = 4
        ) 

        self.fig.patch.set_facecolor("#1d2228")

        for text in autotexts:
            text.set_color("white")

        self.fig.subplots_adjust(bottom=0.25)

        self.canvas.draw()      # Refresh the window