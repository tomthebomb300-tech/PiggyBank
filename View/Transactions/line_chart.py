import customtkinter as ctk
from matplotlib.dates import num2date

from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class Line_chart(ctk.CTkFrame):
    def __init__(self, parent, controller, fg_color, corner_radius):
        super().__init__(parent, fg_color=fg_color, corner_radius=corner_radius)
        self.controller = controller

        self.weeks, self.un_filtered_balances = self.controller.getWeeksAndBalances(self.controller.getCategories())

        frame = ctk.CTkFrame(self, fg_color="#1d2228", corner_radius=40)
        frame.pack(fill = "both", expand = True, padx = 10, pady = (0,10))
        self.create_chart(frame)


    def create_chart(self, parent):
        self.fig = Figure(figsize = (6, 3), dpi = 100, layout="tight")
        self.ax = self.fig.add_subplot(111)

        self.fig.patch.set_facecolor("#1d2228")
        self.ax.set_facecolor("#1d2228")

        self.canvas = FigureCanvasTkAgg(self.fig, parent)
        self.canvas.get_tk_widget().pack(side = "bottom", fill = "both", expand = True, pady=(0,40))


    def update(self, categories):
       _, self.filtered_balances = self.controller.getWeeksAndBalances(categories)
       self.update_chart(self.filtered_balances, self.un_filtered_balances, self.weeks)


    def update_chart(self, filtered, un_filtered, weeks):
        self.ax.clear()
        self.add_tooltip()
        self.ax.set_facecolor("#1d2228")

        self.ax.plot(weeks, filtered,"#349404",linewidth=2,label="Fake Balances",)

        self.ax.plot(weeks, un_filtered,"#FFFFFF",linewidth=2,label="Real Balances",)

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

        hover_date = num2date(event.xdata).replace(tzinfo=None)

        index = min(range(len(self.weeks)),key=lambda i: abs((self.weeks[i] - hover_date).total_seconds()))
        if(index >= len(self.weeks) or index < 0):
            self.hide_toolbar()
            return
        self.vline.set_xdata([self.weeks[index], self.weeks[index]])
        self.vline.set_visible(True)


        self.tooltip.set_text("{0} \nFake: {1}\nReal: {2}".format(self.weeks[index].date(), self.filtered_balances[index], self.un_filtered_balances[index]))

        self.tooltip.set_visible(True)
        self.canvas.draw_idle()


    def hide_toolbar(self):
        self.vline.set_visible(False)
        self.tooltip.set_visible(False)
        self.canvas.draw_idle()

    def get_text(self):
        return "blank"