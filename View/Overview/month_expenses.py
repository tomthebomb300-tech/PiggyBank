import customtkinter as ctk

from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class Month_expenses:
    def __init__(self, parent, controller):
        self.parent = parent
        self.controller = controller
        self.create_pie_legend(parent)

    def create_pie_legend(self, parent):
        expenses = self.controller.getBiggestExpenses(8, 2025)

        for c in expenses:
            expenses[c] *= -1

        chart_frame = ctk.CTkFrame(parent)
        chart_frame.pack(side = "top", padx = 10, pady = 10, fill = "both", expand = True)

        labels = list(expenses.keys())
        values = list(expenses.values())
        colors = ["#B8E64C", "#11C5C6", "#8CB4FF", "#9B84F3", "#D6AA19", "#C71B71"]

        fig = Figure(figsize = (6, 6), dpi = 100)
        ax = fig.add_subplot(111)

        wedges, texts, autotexts = ax.pie(
            values, 
            colors = colors, 
            startangle = 90,
            wedgeprops = dict(width=0.35, edgecolor="#1d2228"), 
            autopct = "%1.0f%%", 
            pctdistance = 0.82
        )

        fig.subplots_adjust(bottom = 0.25)

        ax.legend(
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

        
        total = round(sum(values),2)
        ax.text(0, 0, "- €{0}".format(total), ha = "center", va = "center", fontsize = 18, fontweight = "bold", color = "white")

        fig.patch.set_facecolor("#1d2228")

        for t in texts + autotexts:
            t.set_color("white")

        
        canvas = FigureCanvasTkAgg(fig, master = chart_frame)
        canvas.draw()
        canvas.get_tk_widget().pack(fill = "both", expand = True)