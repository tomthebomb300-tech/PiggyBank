import customtkinter as ctk
import mplfinance as mpf

from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class Candle_stick_chart(ctk.CTkFrame):
    def __init__(self, parent, controller, fg_color, corner_radius):
        super().__init__(parent, fg_color=fg_color, corner_radius=corner_radius)
        self.controller = controller

        ohlc = self.controller.getOHLC("ME")
        print(ohlc)

        self.create_chart(self)
        self.update_chart(ohlc)

    def create_chart(self, parent):
        self.fig = Figure(figsize = (6, 3), dpi = 100, layout="tight")
        self.ax = self.fig.add_subplot(111)

        self.fig.patch.set_facecolor("#1d2228")
        self.ax.set_facecolor("#1d2228")

        self.canvas = FigureCanvasTkAgg(self.fig, parent)
        self.canvas.get_tk_widget().pack(fill = "both", expand = True, pady=(0,40))

    def update_chart(self, ohlc):
        mpf.plot(
            ohlc,
            type="candle",
            style="charles",
            ax=self.ax
        )