import customtkinter as ctk

from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class Pies(ctk.CTkFrame):
    def __init__(self, parent, fg_color, corner_radius):
        super().__init__(parent, fg_color = fg_color, corner_radius = corner_radius)
        self.create_pie_charts(self)



    def create_pie_charts(self, parent):
        self.inc_fig = Figure(figsize=(6, 6), dpi=100, layout = "tight")
        self.inc_ax = self.inc_fig.add_subplot(111)
        self.inc_canvas = FigureCanvasTkAgg(self.inc_fig, master=parent)
        self.inc_canvas.get_tk_widget().pack(side = "left", fill="both", expand=True, pady=40, padx=40)

        self.exp_fig = Figure(figsize=(6, 6), dpi=100, layout = "tight")
        self.exp_ax = self.exp_fig.add_subplot(111)
        self.exp_canvas = FigureCanvasTkAgg(self.exp_fig, master=parent)
        self.exp_canvas.get_tk_widget().pack(side = "right", fill="both", expand=True, pady=40, padx=40)

    def update(self, income, expense):
        self.update_pie(self.inc_fig, self.inc_ax, self.inc_canvas, list(income.keys()), list(income.values()),sign="")
        self.update_pie(self.exp_fig, self.exp_ax, self.exp_canvas, list(expense.keys()), list(expense.values()), sign="-")


    def update_pie(self, fig, ax, canvas, labels, values, sign):
        ax.clear()   # Remove the old chart
        colors = ["#B8E64C", "#11C5C6", "#8CB4FF", "#9B84F3", "#D6AA19", "#C71B71"]

        if len(values) == 0:
            ax.pie([1],colors=["#3A3A3A"],startangle=90,radius=1.2,wedgeprops=dict(width=0.35, edgecolor="#1d2228"))
            ax.text(0, 0,"€0.00",ha="center",va="center",fontsize=18,fontweight="bold",color="white")
            ax.text(0, -0.18,"No transactions",ha="center",va="center",fontsize=10,color="#AAAAAA")
            fig.patch.set_facecolor("#1d2228")
            canvas.draw()
            return
        
        wedges, _, autotexts = ax.pie(
            values,
            colors=colors[:len(values)],
            startangle=90,
            radius=1.2,
            wedgeprops=dict(width=0.35, edgecolor="#1d2228"),
            autopct="%1.0f%%",
            pctdistance=0.82
        )

        total = round(sum(values),2)

        for autotext, val in zip(autotexts, values):
            percentage = (val / total) * 100
            if percentage < 2:
                autotext.set_text("")

        ax.text(0, 0, "{0}€{1}".format(sign, total), ha="center", va="center", fontsize=18, fontweight="bold", color="white")

        fig.patch.set_facecolor("#1d2228")

        for text in autotexts:
            text.set_color("white")

        fig.subplots_adjust(bottom=0.25)

        self.add_tooltip(ax, canvas, labels, values, total, wedges)

        canvas.draw()      # Refresh the window

    def add_tooltip(self, ax, canvas, labels, values, total, wedges):
        tooltip = ax.annotate(
            "",
            xy=(0, 0),
            xytext=(15, 15),
            textcoords="offset points",
            bbox=dict(
                boxstyle="round,pad=0.6",
                fc="#262B35",
                ec="#555555",
                alpha=0.95
            ),
            color="white",
            fontsize=10
        )

        tooltip.set_visible(False)

        canvas.mpl_connect("motion_notify_event",lambda event: self.on_hover(event, tooltip, canvas, ax, wedges, labels, values, total))

    def on_hover(self, event, tooltip, canvas, ax, wedges, labels, values, total):
        if event.inaxes != ax:
            tooltip.set_visible(False)
            canvas.draw_idle()
            return

        canvas_width, canvas_height = canvas.get_width_height()

        for i, wedge in enumerate(wedges):
            contains, _ = wedge.contains(event)

            if contains:
                percentage = values[i] / total * 100
                tooltip.xy = (event.xdata, event.ydata)

                x_offset = -75 if event.x > canvas_width - 200 else 15
                y_offset = -50 if event.y > canvas_height - 100 else 15
                tooltip.set_position((x_offset, y_offset))

                tooltip.set_text(
                    f"{labels[i]}\n"
                    f"€{values[i]:,.2f}\n"
                    f"{percentage:.1f}%"
                )

                tooltip.set_visible(True)
                canvas.draw_idle()
                return

        tooltip.set_visible(False)
        canvas.draw_idle()