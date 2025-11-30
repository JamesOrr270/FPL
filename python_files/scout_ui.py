import pandas as pd
import tkinter as tk
from tkinter import ttk, messagebox
import data_download

data_download.download_FPL_data()

players = pd.read_csv("players.csv")
players['cost_millions'] = players['now_cost'] / 10
players['value'] = players['total_points'] / players['cost_millions']

position_map = {
    1: "Goalkeeper",
    2: "Defender",
    3: "Midfielder",
    4: "Forward"
}
players['position'] = players['element_type'].map(position_map)

def search_players():
    try:
        pos_choice = position_var.get()
        budget = float(budget_entry.get())
        
        if pos_choice == 0:
            messagebox.showerror("Error", "Please select a position")
            return
        
        filtered = players[(players['element_type'] == pos_choice) & 
                          (players['cost_millions'] <= budget)]
        
        if filtered.empty:
            messagebox.showinfo("No Results", f"No {position_map[pos_choice]}s found under £{budget:.1f}m")
            return
        
        best_options_points = filtered[['first_name', 'second_name', 'position', 
                                 'cost_millions', 'total_points', 'value']] \
            .sort_values(by="total_points", ascending=False) \
            .head(10)
        
        best_options_value = filtered[['first_name', 'second_name', 'position', 
                                 'cost_millions', 'total_points', 'value']] \
            .sort_values(by="value", ascending=False) \
            .head(10)
        
        # Clear previous results
        for tree in [points_tree, value_tree]:
            for item in tree.get_children():
                tree.delete(item)
        
        # Populate points table
        for _, row in best_options_points.iterrows():
            points_tree.insert('', 'end', values=(
                row['first_name'], 
                row['second_name'], 
                f"£{row['cost_millions']:.1f}m",
                int(row['total_points']),
                f"{row['value']:.2f}"
            ))
        
        # Populate value table
        for _, row in best_options_value.iterrows():
            value_tree.insert('', 'end', values=(
                row['first_name'], 
                row['second_name'], 
                f"£{row['cost_millions']:.1f}m",
                int(row['total_points']),
                f"{row['value']:.2f}"
            ))
        
        results_label.config(text=f"Top {position_map[pos_choice]}s under £{budget:.1f}m")
        
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid budget (e.g., 6.0)")

# Create main window
root = tk.Tk()
root.title("FPL Scout")
root.geometry("900x700")

# Title
title_label = tk.Label(root, text="FPL Scout", font=("Arial", 20, "bold"))
title_label.pack(pady=10)

# Input frame
input_frame = tk.Frame(root)
input_frame.pack(pady=10)

# Position selection
position_label = tk.Label(input_frame, text="Position:", font=("Arial", 12))
position_label.grid(row=0, column=0, padx=5, pady=5)

position_var = tk.IntVar(value=0)
position_dropdown = ttk.Combobox(input_frame, values=[
    "1 - Goalkeeper",
    "2 - Defender", 
    "3 - Midfielder",
    "4 - Forward"
], width=20, state="readonly")
position_dropdown.grid(row=0, column=1, padx=5, pady=5)

def on_position_select(event):
    selection = position_dropdown.get()
    if selection:
        position_var.set(int(selection[0]))

position_dropdown.bind("<<ComboboxSelected>>", on_position_select)

# Budget entry
budget_label = tk.Label(input_frame, text="Budget (£m):", font=("Arial", 12))
budget_label.grid(row=0, column=2, padx=5, pady=5)

budget_entry = tk.Entry(input_frame, width=10, font=("Arial", 12))
budget_entry.grid(row=0, column=3, padx=5, pady=5)

# Search button
search_button = tk.Button(input_frame, text="Search", command=search_players, 
                         font=("Arial", 12, "bold"), bg="#37003c", fg="white", 
                         padx=20, pady=5)
search_button.grid(row=0, column=4, padx=10, pady=5)

# Results label
results_label = tk.Label(root, text="", font=("Arial", 14, "bold"))
results_label.pack(pady=5)

# Results frame
results_frame = tk.Frame(root)
results_frame.pack(pady=10, fill='both', expand=True)

# Points table
points_label = tk.Label(results_frame, text="Top Players by Points", font=("Arial", 12, "bold"))
points_label.grid(row=0, column=0, padx=10, pady=5)

points_tree = ttk.Treeview(results_frame, columns=("First", "Last", "Cost", "Points", "Value"), 
                           show='headings', height=10)
points_tree.heading("First", text="First Name")
points_tree.heading("Last", text="Last Name")
points_tree.heading("Cost", text="Cost")
points_tree.heading("Points", text="Points")
points_tree.heading("Value", text="Value")

points_tree.column("First", width=100)
points_tree.column("Last", width=100)
points_tree.column("Cost", width=80)
points_tree.column("Points", width=80)
points_tree.column("Value", width=80)

points_tree.grid(row=1, column=0, padx=10, pady=5)

# Value table
value_label = tk.Label(results_frame, text="Top Players by Value", font=("Arial", 12, "bold"))
value_label.grid(row=0, column=1, padx=10, pady=5)

value_tree = ttk.Treeview(results_frame, columns=("First", "Last", "Cost", "Points", "Value"), 
                          show='headings', height=10)
value_tree.heading("First", text="First Name")
value_tree.heading("Last", text="Last Name")
value_tree.heading("Cost", text="Cost")
value_tree.heading("Points", text="Points")
value_tree.heading("Value", text="Value")

value_tree.column("First", width=100)
value_tree.column("Last", width=100)
value_tree.column("Cost", width=80)
value_tree.column("Points", width=80)
value_tree.column("Value", width=80)

value_tree.grid(row=1, column=1, padx=10, pady=5)

root.mainloop()