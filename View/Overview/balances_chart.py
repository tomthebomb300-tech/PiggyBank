import customtkinter as ctk

from datetime import datetime
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class Balances_chart:
    def __init__(self, parent, controller):
        self.controller = controller
        self.date = datetime(2025, 1, 1)

        self.create_frame(parent)


    def create_frame(self, parent):
        frame = ctk.CTkFrame(parent, fg_color = "#1d2228")
        frame.pack(side = "bottom", fill = "both", expand = True, padx = 10, pady = 10)
        self.create_header(frame)
        self.create_chart(frame)

    def create_header(self, parent):
        frame = ctk.CTkFrame(parent, fg_color = "#1d2228")
        frame.pack(anchor = "e", pady = (30, 10), padx = (0, 10))

        last_button = ctk.CTkButton(frame, text = "<", width = 30, height = 30, fg_color = "transparent", hover_color = "#3A3A3A", command = self.last_year)
        last_button.pack(side = "left")

        self.year_label = ctk.CTkLabel(frame, text = self.date.strftime("%Y"), font = ("Arial", 16))
        self.year_label.pack(side = "left")

        next_button = ctk.CTkButton(frame, text = ">", width = 30, height = 30, fg_color = "transparent", hover_color = "#3A3A3A", command = self.next_year)
        next_button.pack(side = "right")

    def last_year(self):
        self.date = self.date.replace(year=self.date.year - 1)
        self.update_year()
        self.update_chart()

    def next_year(self):
        self.date = self.date.replace(year=self.date.year + 1)
        self.update_year()
        self.update_chart()

    def update_year(self):
        self.year_label.configure(text = self.date.strftime("%Y"))

    def create_chart(self, parent):
        self.fig = Figure(figsize = (6, 3), dpi = 100, layout="tight")
        self.ax = self.fig.add_subplot(111)

        self.fig.patch.set_facecolor("#1d2228")
        self.ax.set_facecolor("#1d2228")

        self.canvas = FigureCanvasTkAgg(self.fig, parent)
        self.canvas.get_tk_widget().pack(fill = "both", expand = True)
        self.update_chart()


    def update_chart(self):
        months = self.controller.getMonths(self.date.year)
        account = self.controller.getMonthlyAccountBalance(self.date.year)
        cash = self.controller.getMonthlyCashBalance(self.date.year)
        invested = self.controller.getMonthlyInvestedBalance(self.date.year)

        self.ax.clear()
        self.ax.set_facecolor("#1d2228")

        self.ax.plot(months, account,
                     linewidth=1,
                     label="Account Balance")

        self.ax.plot(months, cash,
                     linewidth=1,
                     label="Cash Balance")

        self.ax.plot(months, invested,
                     linewidth=1,
                     label="Deposited Investments")

        self.ax.tick_params(colors="white")
        self.ax.spines["bottom"].set_color("#555")
        self.ax.spines["left"].set_color("#555")
        self.ax.spines["top"].set_visible(False)
        self.ax.spines["right"].set_visible(False)

        self.ax.grid(alpha=0.15)

        legend = self.ax.legend(
            loc="upper left",
            frameon=False
        )

        for text in legend.get_texts():
            text.set_color("white")

        self.canvas.draw()