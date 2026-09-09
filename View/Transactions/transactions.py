import customtkinter as ctk

from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from View.Transactions.date_range_slider import Date_range_slider
from View.Transactions.category_selector import Category_selector

class Transactions(ctk.CTkFrame):
    def __init__(self, parent, controller, fg_color, corner_radius):
        super().__init__(parent, fg_color=fg_color, corner_radius=corner_radius)
        self.controller = controller

        self.start_date = self.controller.getStartDate()
        self.last_date = self.controller.getLastDate()

        slider_fetch_frame = ctk.CTkFrame(self, fg_color="transparent")
        slider_fetch_frame.pack(fill = "x", padx = 20, pady = 20)
        slider_fetch_frame.grid_columnconfigure(0, weight=1)
        slider_fetch_frame.grid_columnconfigure(1, weight=0)

        slider = Date_range_slider(parent=slider_fetch_frame,start_date=self.start_date,end_date=self.last_date,command=self.range_changed)
        slider.grid(row = 0, column = 0, sticky = "ew", padx=20, pady=20)
        fetch_button = ctk.CTkButton(slider_fetch_frame, text="Fetch", command=self.fetch)
        fetch_button.grid(row = 0, column = 1, sticky = "ns", padx = 20, pady = 20)


        self.category_selector = Category_selector(parent=self, categories=self.controller.getCategories(), corner_radius=40)
        self.category_selector.pack(side = "left")
        content = ctk.CTkFrame(self, fg_color = "#1d2228")
        content.pack(side = "right", expand = True, padx=20, pady=20)

        self.create_pie_charts(content)
        self.fetch()
        

    def range_changed(self, start, end):
        self.start_date = start
        self.last_date = end

    def fetch(self):
        income = self.controller.getIncome(self.category_selector.get_selected(), self.start_date, self.last_date)
        expense = self.controller.getExpense(self.category_selector.get_selected(), self.start_date, self.last_date)

        self.update_pie(self.inc_fig, self.inc_ax, self.inc_canvas, list(income.keys()), list(income.values()))

        for key in expense:
            expense[key] *= -1
            
        self.update_pie(self.exp_fig, self.exp_ax, self.exp_canvas, list(expense.keys()), list(expense.values()))

    def create_pie_charts(self, parent):
        self.inc_fig = Figure(figsize=(6, 6), dpi=100)
        self.inc_ax = self.inc_fig.add_subplot(111)
        self.inc_canvas = FigureCanvasTkAgg(self.inc_fig, master=parent)
        self.inc_canvas.get_tk_widget().pack(side = "left", fill="both", expand=True, pady=(0,40))

        self.exp_fig = Figure(figsize=(6, 6), dpi=100, layout = "tight")
        self.exp_ax = self.exp_fig.add_subplot(111)
        self.exp_canvas = FigureCanvasTkAgg(self.exp_fig, master=parent)
        self.exp_canvas.get_tk_widget().pack(side = "right", fill="both", expand=True, pady=(0,40))


    def update_pie(self, fig, ax, canvas, labels, values):
        ax.clear()   # Remove the old chart
        colors = ["#B8E64C", "#11C5C6", "#8CB4FF", "#9B84F3", "#D6AA19", "#C71B71"]
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
        ax.text(0, 0, f"€{total:,}", ha="center", va="center", fontsize=18, fontweight="bold", color="white")

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

        for i, wedge in enumerate(wedges):
            contains, _ = wedge.contains(event)

            if contains:
                percentage = values[i] / total * 100
                tooltip.xy = (event.xdata, event.ydata)

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