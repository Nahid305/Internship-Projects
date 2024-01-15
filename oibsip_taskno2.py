import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np

class BMI_Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("BMI Calculator")

       
        self.weight_var = tk.DoubleVar()
        self.height_var = tk.DoubleVar()

       
        self.bmi_var = tk.StringVar()
        self.category_var = tk.StringVar()

        
        self.create_widgets()

    def create_widgets(self):
      
        weight_label = ttk.Label(self.root, text="Weight (kg):")
        weight_entry = ttk.Entry(self.root, textvariable=self.weight_var)

        height_label = ttk.Label(self.root, text="Height (m):")
        height_entry = ttk.Entry(self.root, textvariable=self.height_var)

       
        calculate_button = ttk.Button(self.root, text="Calculate BMI", command=self.calculate_bmi)

        
        result_label = ttk.Label(self.root, text="BMI:")
        result_value_label = ttk.Label(self.root, textvariable=self.bmi_var)

        category_label = ttk.Label(self.root, text="Category:")
        category_value_label = ttk.Label(self.root, textvariable=self.category_var)

       
        trend_button = ttk.Button(self.root, text="BMI Trend Analysis", command=self.plot_trend)

       
        weight_label.grid(row=0, column=0, padx=10, pady=10)
        weight_entry.grid(row=0, column=1, padx=10, pady=10)

        height_label.grid(row=1, column=0, padx=10, pady=10)
        height_entry.grid(row=1, column=1, padx=10, pady=10)

        calculate_button.grid(row=2, column=0, columnspan=2, pady=10)

        result_label.grid(row=3, column=0, padx=10, pady=10)
        result_value_label.grid(row=3, column=1, padx=10, pady=10)

        category_label.grid(row=4, column=0, padx=10, pady=10)
        category_value_label.grid(row=4, column=1, padx=10, pady=10)

        trend_button.grid(row=5, column=0, columnspan=2, pady=10)

    def calculate_bmi(self):
        try:
            weight = self.weight_var.get()
            height = self.height_var.get()

            if weight <= 0 or height <= 0:
                messagebox.showerror("Error", "Please enter valid values for weight and height.")
                return

            bmi = weight / (height ** 2)
            category = self.classify_bmi(bmi)

            self.bmi_var.set(f"{bmi:.2f}")
            self.category_var.set(category)
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")

    def classify_bmi(self, bmi):
        if bmi < 18.5:
            return "Underweight"
        elif 18.5 <= bmi < 24.9:
            return "Normal weight"
        elif 25 <= bmi < 29.9:
            return "Overweight"
        else:
            return "Obese"

    def plot_trend(self):
        

        num_data_points = 10
        weights = np.random.uniform(50, 100, num_data_points)
        heights = np.random.uniform(1.5, 2, num_data_points)
        bmis = weights / (heights ** 2)

        fig, ax = plt.subplots()
        ax.plot(bmis, marker='o', linestyle='-', color='b')
        ax.set_xlabel('Data Points')
        ax.set_ylabel('BMI')
        ax.set_title('BMI Trend Analysis')

        canvas = FigureCanvasTkAgg(fig, master=self.root)
        canvas_widget = canvas.get_tk_widget()
        canvas_widget.grid(row=6, column=0, columnspan=2, pady=10)

if __name__ == "__main__":
    root = tk.Tk()
    app = BMI_Calculator(root)
    root.mainloop()
