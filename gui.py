import tkinter as tk
from tkinter import ttk
import subprocess
import platform


class TrafficLight:
    def __init__(self, root):
        self.root = root
        self.root.title("Traffic Light")

        # Get screen dimensions
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()

        # Calculate window position for centering
        x_position = (screen_width - 200) // 2
        y_position = (screen_height - 500) // 2

        # Set window position
        self.root.geometry(f"200x500+{x_position}+{y_position}")

        self.current_color = None
        self.colors = ["#FF0000", "#FFFF00", "#00FF00"]

        self.label = ttk.Label(
            root, text="Traffic Light", font=("Helvetica", 16))
        self.label.place(relx=0.5, rely=0.1, anchor="center")

        self.canvas = tk.Canvas(root, width=100, height=300)
        self.canvas.place(relx=0.5, rely=0.5, anchor="center")

        self.button = ttk.Button(root, text="Change Color".upper(),
                                 command=self.change_color)
        self.button.place(relx=0.5, rely=0.9,
                          anchor="center", width=120, height=50)

        self.draw_traffic_light()
        self.add_3d_effect()

    def draw_traffic_light(self):
        self.circles = []
        for i in range(3):
            circle = self.canvas.create_oval(
                25, 25 + i * 100, 75, 75 + i * 100, fill="#000000", outline="#C1C1C1")
            self.circles.append(circle)

    def change_color(self):
        if self.current_color is not None:
            self.canvas.itemconfig(
                self.circles[self.current_color], fill="#000000")

        self.current_color = (self.current_color +
                              1) % 3 if self.current_color is not None else 0
        self.canvas.itemconfig(
            self.circles[self.current_color], fill=self.colors[self.current_color])

        # Play system beep sound when changing color using subprocess
        if platform.system() == "Windows":
            subprocess.call(["powershell", "[console]::beep(1000,200)"])
        else:
            subprocess.call(["echo", "-e", "\a"])

    def add_3d_effect(self):
        for i, circle in enumerate(self.circles):
            x1, y1, x2, y2 = self.canvas.coords(circle)
            shadow_color = "#CCCCCC"

            # Create a shadow using a smaller oval
            shadow_oval = self.canvas.create_oval(
                x1 + 5, y1 + 5, x2 + 5, y2 + 5, fill=shadow_color, outline=shadow_color)
            self.canvas.lower(shadow_oval)  # Send the shadow to the back


# Create the root window
root = tk.Tk()
traffic_light = TrafficLight(root)
root.mainloop()
