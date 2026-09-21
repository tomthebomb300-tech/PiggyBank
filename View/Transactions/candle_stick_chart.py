import customtkinter as ctk
import mplfinance as mpf

from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from View.Transactions.selector import Selector

class Candle_stick_chart(ctk.CTkFrame):
    def __init__(self, parent, controller, fg_color, corner_radius):
        super().__init__(parent, fg_color=fg_color, corner_radius=corner_radius)
        self.controller = controller

        self.timeframe = "ME"
        self.ohlc = self.controller.getOHLC(self.timeframe)

        self.max_candles = 75
        self.first_candle = max(0, len(self.ohlc)-self.max_candles)
        self.dragging = False

        frame = ctk.CTkFrame(self, fg_color="#1d2228", corner_radius=40)
        frame.pack(fill = "both", expand = True, padx = 10, pady = (0,10))

        self.create_chart(frame)

        timeframes = ["YE", "ME", "W", "D"]
        timeframe_selector = Selector(frame, "transparent", timeframes, self.change_timeframe)
        timeframe_selector.pack(side = "top", anchor = "w", padx = (90,0), pady = (20,0))

    def create_chart(self, parent):
        self.fig = Figure(figsize = (6, 3), dpi = 100, layout="tight")
        self.ax = self.fig.add_subplot(111)

        self.fig.patch.set_facecolor("#1d2228")
        self.ax.set_facecolor("#1d2228")

        self.canvas = FigureCanvasTkAgg(self.fig, parent)
        self.canvas.get_tk_widget().pack(side = "bottom", fill = "both", expand = True, pady=(0,40))

        self.canvas.mpl_connect("scroll_event", self.on_scroll)

        colours = mpf.make_marketcolors(
            up = "#05be24",
            down = "#BB0A36",
            wick = {"up":"#c4c4c4","down":"#c4c4c4"}
        )
        self.style = mpf.make_mpf_style(
            marketcolors = colours
        )

    def change_timeframe(self, timeframe):
        print(timeframe)
        self.timeframe = timeframe
        self.ohlc = self.controller.getOHLC(self.timeframe)
        self.first_candle = max(0, len(self.ohlc)-self.max_candles)
        self.update_chart()

    def update_chart(self):
        self.ax.clear()
        self.add_tooltip()

        mpf.plot(
            self.ohlc,
            type="candle",
            style=self.style,
            ax=self.ax
        )
        self.ax.set_xlim(self.first_candle-0.5, self.first_candle+self.max_candles-0.5)
        self.canvas.draw_idle()

    def add_tooltip(self):
            self.vline = self.ax.axvline(x = 0, color = "#666666", linestyle = "--", alpha = 0.5)
            self.vline.set_visible(False)

            self.tooltip = self.ax.text(0.92, 0.95, "", transform = self.ax.transAxes ,ha = "left", va ="top",fontsize=10,
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

        index = int(round(event.xdata))
        if(index >= len(self.ohlc) or index < 0):
            self.hide_toolbar()
            return

        self.vline.set_xdata([index, index])
        self.vline.set_visible(True)


        self.tooltip.set_text("{0}".format(
            self.get_text(self.ohlc.index.tolist()[index].date(), self.ohlc.iloc[index])
        ))

        self.tooltip.set_visible(True)
        self.canvas.draw_idle()


    def hide_toolbar(self):
        self.vline.set_visible(False)
        self.tooltip.set_visible(False)
        self.canvas.draw_idle()

    def get_text(self, date, ohlc):
        open = f"{ohlc.open:,}"
        high = f"{ohlc.high:,}"
        low = f"{ohlc.low:,}"
        close = f"{ohlc.close:,}"
        
        if(self.timeframe == "D"):
            formatted_date = date.strftime('%d / %b / %Y')
            day = date.strftime("%A")
            return "{0}\n{1}\n\nO: {2}\nH: {3}\nL: {4}\nC: {5}".format(formatted_date, day, open, high, low, close)
        elif(self.timeframe == "W"):
            month_year = date.strftime("%b / %Y")
            week = date.strftime("%W")
            return "{0}\nWeek: {1}\n\nO: {2}\nH: {3}\nL: {4}\nC: {5}".format(month_year, week, open, high, low, close)
        elif(self.timeframe == "ME"):
            month_year = date.strftime("%b / %Y")
            return "{0}\n\nO: {1}\nH: {2}\nL: {3}\nC: {4}".format(month_year, open, high, low, close)
        elif(self.timeframe == "YE"):
            year = date.strftime("%Y")
            return "{0}\n\nO: {1}\nH: {2}\nL: {3}\nC: {4}".format(year, open, high, low, close)

    def on_scroll(self, event):
        if(len(self.ohlc) <= self.max_candles):
            return

        if event.button == "up":
            self.first_candle = max(0, self.first_candle - 5)

        elif event.button == "down":
            self.first_candle = min(
                len(self.ohlc) - self.max_candles,
                self.first_candle + 5
            )

        self.ax.set_xlim(
            self.first_candle - 0.5,
            self.first_candle + self.max_candles - 0.5
        )

        self.canvas.draw_idle()