import customtkinter as ctk
import numpy as np
import mplcursors

from datetime import datetime
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from scipy.interpolate import PchipInterpolator

class Balances_chart:
    def __init__(self, parent, controller):
        self.controller = controller
        self.date = datetime(2026, 1, 1)

        self.create_frame(parent)


    def create_frame(self, parent):
        frame = ctk.CTkFrame(parent, fg_color = "#1d2228", corner_radius=40)
        frame.pack(side = "bottom", fill = "both", expand = True, padx = 10, pady = 10)
        self.create_header(frame)
        self.create_chart(frame)

    def create_header(self, parent):
        frame = ctk.CTkFrame(parent, fg_color = "#1d2228")
        frame.pack(pady = (30, 10), padx = (0, 10))

        last_button = ctk.CTkButton(frame, text = "<", width = 30, height = 30, fg_color = "transparent", hover_color = "#3A3A3A", command = self.previous_year)
        last_button.pack(side = "left", padx = (0, 20))

        self.year_label = ctk.CTkLabel(frame, font = ("Arial", 20))
        self.year_label.pack(side = "left")
        self.update_year()

        next_button = ctk.CTkButton(frame, text = ">", width = 30, height = 30, fg_color = "transparent", hover_color = "#3A3A3A", command = self.next_year)
        next_button.pack(side = "right", padx = (20, 0))

    def __get_chart_data(self, year):
        self.months = self.controller.getMonths(year)
        self.account = self.controller.getMonthlyAccountBalance(year)
        self.cash = self.controller.getMonthlyCashBalance(year)
        self.invested = self.controller.getMonthlyInvestedBalance(year)
    

    def previous_year(self):
        self.__get_chart_data(self.date.year-1)
        if(len(self.months) <= 0):
            return

        self.date = self.date.replace(year=self.date.year - 1)
        self.update_year()
        self.update_chart()

    def next_year(self):
        self.__get_chart_data(self.date.year+1)
        if(len(self.months) <= 0):
            return

        self.date = self.date.replace(year=self.date.year+1)
        self.update_year()
        self.update_chart()

    def update_year(self):
        self.year_label.configure(text = "{0} {1}".format(self.date.strftime("%Y"), "Balances"))

    def create_chart(self, parent):
        self.fig = Figure(figsize = (6, 3), dpi = 100, layout="tight")
        self.ax = self.fig.add_subplot(111)

        self.fig.patch.set_facecolor("#1d2228")
        self.ax.set_facecolor("#1d2228")

        self.canvas = FigureCanvasTkAgg(self.fig, parent)
        self.canvas.get_tk_widget().pack(fill = "both", expand = True, pady=(0,40))

        self.__get_chart_data(self.date.year)
        self.update_chart()


    def update_chart(self):
        self.x = np.arange(len(self.months))
        x_smooth = np.linspace(self.x.min(), self.x.max(), 300)

        account_smooth = PchipInterpolator(self.x, self.account)(x_smooth)
        cash_smooth = PchipInterpolator(self.x, self.cash)(x_smooth)
        invested_smooth = PchipInterpolator(self.x, self.invested)(x_smooth)



        self.ax.clear()

        self.add_tooltip()

        self.ax.set_facecolor("#1d2228")

        self.ax.plot(x_smooth, account_smooth,"#349404",linewidth=2,label="Account Balance",)
        self.ax.plot(self.months, self.account,"#349404",linewidth=0,marker = "o")

        self.ax.plot(x_smooth, cash_smooth,"#e3ff00",linewidth=2,label="Cash Balance")
        self.ax.plot(self.months, self.cash,"#e3ff00",linewidth=0,marker = "o")
        
        self.ax.plot(x_smooth, invested_smooth,"#bd00ff",linewidth=2,label="Deposited Investments")
        self.ax.plot(self.months, self.invested,"#bd00ff",linewidth=0,marker = "o")

        self.ax.set_xticks(self.x)
        self.ax.set_xticklabels(self.months)
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

        self.canvas.draw()


    def add_tooltip(self):
        self.vline = self.ax.axvline(x = 0, color = "#666666", linestyle = "--", alpha = 0.5)
        self.vline.set_visible(False)

        self.tooltip = self.ax.text(0.85, 0.95, "", transform = self.ax.transAxes ,ha = "left", va ="top",fontsize=10,
                bbox=dict(  boxstyle="round,pad=0.5",
                            facecolor="#2b2b2b",
                            edgecolor="white",
                            alpha=0.9
                        ),
            color="white"
        )
        self.tooltip.set_visible(False)
        self.canvas.mpl_connect("motion_notify_event",self.on_hover)


    def on_hover(self, event):
        if(event.inaxes != self.ax or event.xdata is None):
            self.hide_toolbar()
            return

        month_index = int(round(event.xdata))
        if(month_index >= len(self.months) or month_index < 0):
            self.hide_toolbar()
            return

        point_x = self.x[month_index]

        self.vline.set_xdata([point_x, point_x])
        self.vline.set_visible(True)

        self.tooltip.set_text("{0}\nAccount: €{1}\nCash:       €{2}\nInvested: €{3}".format(
                                                                                    self.months[month_index], 
                                                                                    self.account[month_index], 
                                                                                    self.cash[month_index], 
                                                                                    self.invested[month_index]
                                                                                    ))

        self.tooltip.set_visible(True)
        self.canvas.draw_idle()


    def hide_toolbar(self):
        self.vline.set_visible(False)
        self.tooltip.set_visible(False)
        self.canvas.draw_idle()