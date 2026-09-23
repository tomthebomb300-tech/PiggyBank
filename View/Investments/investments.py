import customtkinter as ctk

from View.Transactions.search import Search

from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class Investments(ctk.CTkFrame):
    def __init__(self, parent, controller, fg_color, corner_radius):
        super().__init__(parent, fg_color=fg_color, corner_radius=corner_radius)
        self.controller = controller

        frame = ctk.CTkFrame(self, fg_color="#1d2228", corner_radius=40)
        frame.pack(fill = "both", expand = True, padx = 10, pady = (10,10))
        self.create_chart(frame)
        weeks, cum_deposits = self.controller.getWeeksAndInvested()
        print(cum_deposits)
        self.update_chart(weeks, cum_deposits)

    def create_chart(self, parent):
        self.fig = Figure(figsize = (6, 3), dpi = 100, layout="tight")
        self.ax = self.fig.add_subplot(111)

        self.fig.patch.set_facecolor("#1d2228")
        self.ax.set_facecolor("#1d2228")

        self.canvas = FigureCanvasTkAgg(self.fig, parent)
        self.canvas.get_tk_widget().pack(side = "bottom", fill = "both", expand = True, pady=(40,40))   

    def update_chart(self, weeks, cum_deposits):
        self.ax.clear()
        self.ax.set_facecolor("#1d2228")

        self.ax.plot(weeks, cum_deposits,"#349404",linewidth=2,label="Deposited",)

        self.ax.set_xlim(min(weeks), max(weeks))

        self.ax.tick_params(axis = "x", colors = "white")
        self.ax.tick_params(axis = "y", colors = "white")

        self.ax.spines["bottom"].set_color("white")
        self.ax.spines["left"].set_color("white")
        self.ax.spines["top"].set_visible(False)
        self.ax.spines["right"].set_visible(False)

        self.ax.grid(alpha=0.15)

        legend = self.ax.legend(
            loc="upper left",
            frameon=False
        )

        for text in legend.get_texts():
            text.set_color("white")

        self.ax.relim()
        self.ax.autoscale_view()
        self.canvas.draw_idle()