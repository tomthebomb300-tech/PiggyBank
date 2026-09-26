import customtkinter as ctk

from View.Transactions.search import Search

from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class Investments(ctk.CTkFrame):
    def __init__(self, parent, controller, fg_color, corner_radius):
        super().__init__(parent, fg_color=fg_color, corner_radius=corner_radius)
        self.controller = controller

        dates, deposits, portfolio_value = self.controller.getDatesDepositsPortValue()

        frame = ctk.CTkFrame(self, fg_color="transparent", corner_radius=40)
        frame.pack(fill = "both", expand = True, padx = 20, pady = 20)

        self.create_chart(frame)
        self.create_overview(frame, deposits, portfolio_value)
        self.update_chart(dates, deposits, portfolio_value)


    def create_overview(self, parent, deposits, portfolio_value):
        overview = ctk.CTkFrame(parent, fg_color="transparent", corner_radius=40)
        overview.pack(side="top", anchor = "n")

        deposited = deposits[len(deposits)-1]
        value = portfolio_value[len(portfolio_value)-1]

        self.create_card(overview, "Deposited", round(deposited,2))
        self.create_card(overview, "Value", round(value,2))
        self.create_card(overview, "Un-realized P&L", round(value-deposited,2))


    def create_card(self, parent, title, value):
        card = ctk.CTkFrame(parent, fg_color="#1d2228", corner_radius=40)
        card.pack(side="left", padx = 10, pady = 10)

        title_label = ctk.CTkLabel(card,text=title,font=("Arial", 20),text_color="white")
        title_label.pack(anchor="w",padx=20,pady=(20,0))

        value_label = ctk.CTkLabel(card,text=value,font=("Arial", 32),text_color="white")
        value_label.pack(anchor="w",padx=20,pady=(20,20))


    def create_chart(self, parent):
        self.fig = Figure(figsize = (6, 3), dpi = 100, layout="tight")
        self.ax = self.fig.add_subplot(111)

        self.fig.patch.set_facecolor("#1d2228")
        self.ax.set_facecolor("#1d2228")

        self.canvas = FigureCanvasTkAgg(self.fig, parent)
        self.canvas.get_tk_widget().pack(side = "bottom", fill = "both", expand = True, pady=(20,40))   

    def update_chart(self, dates, deposits, portfolio_value):
        self.ax.clear()
        self.ax.set_facecolor("#1d2228")

        self.ax.plot(dates, deposits,"#ffffff",linewidth=2,label="Deposited Value",)
        self.ax.plot(dates, portfolio_value,"#349404",linewidth=2,label="Portfolio Value",)

        self.ax.set_xlim(min(dates), max(dates))

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