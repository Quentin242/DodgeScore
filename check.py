import tkinter as tk
from tkinter import ttk

def calculate_points():
    red_points = 0
    green_points = 0

    # Red points calculations
    for role, value in autofill_vars.items():
        if value.get():
            red_points += autofill_points[role]

    for role, value in champ_experience_vars.items():
        if value.get():
            red_points += 2

    for role, var in bad_recent_vars.items():
        red_points += 1 if var.get() else 0

    for role, var in very_bad_recent_vars.items():
        red_points += 3 if var.get() else 0

    if bad_mental_var.get():
        red_points += 2

    if comp_diff_sad_var.get():
        red_points += 1

    # Green points calculations
    for role, value in good_winrate_vars.items():
        if value.get():
            green_points += 2

    for role, var in good_recent_vars.items():
        green_points += 1 if var.get() else 0

    for role, var in zoggy_recent_vars.items():
        green_points += 2 if var.get() else 0
    
    for role, value in bad_winrate_vars.items():
        if value.get():
            red_points += 2

    if comp_diff_happy_var.get():
        green_points += 1

    net_points = red_points - green_points

    if net_points < 0:
        result_var.set("It's Free! [" + str(net_points) + "]")
    elif net_points == 0:
        result_var.set("It’s Free? [" + str(net_points) + "]")
    elif 1 <= net_points <= 3:
        result_var.set("Winnable [" + str(net_points) + "]")
    elif net_points == 4:
        result_var.set("Medium Fun [" + str(net_points) + "]")
    elif net_points == 5:
        result_var.set("MonkaS [" + str(net_points) + "]")
    else:
        result_var.set("DODGE!!! [" + str(net_points) + "]")

def reset():
    for var in [*autofill_vars.values(), *champ_experience_vars.values(), *bad_winrate_vars.values(), bad_mental_var, comp_diff_happy_var, comp_diff_sad_var, *good_winrate_vars.values(), *good_recent_vars.values(), *zoggy_recent_vars.values(), *bad_recent_vars.values(), *very_bad_recent_vars.values()]:
        var.set(False)
    result_var.set("")  # Clear the result_var text


root = tk.Tk()
root.title("Dodge Point Calculator")

autofill_points = {
    'Top': 1,
    'Jungler': 3,
    'Mid': 3,
    'ADC': 2,
    'Support': 2
}

autofill_vars = {}
champ_experience_vars = {}
good_winrate_vars = {}
bad_winrate_vars = {}  # Added bad_winrate
good_recent_vars = {}
zoggy_recent_vars = {}
bad_recent_vars = {}
very_bad_recent_vars = {}

roles = ["Top", "Jungler", "Mid", "ADC", "Support"]
grid_positions = [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1)]

for idx, role in enumerate(roles):
    row, col = grid_positions[idx]
    frame = ttk.LabelFrame(root, text=role)
    frame.grid(row=row, column=col, padx=10, pady=5, sticky='w')

    good_winrate_var = tk.BooleanVar()
    ttk.Checkbutton(frame, text="Good winrate", variable=good_winrate_var).pack(anchor='w', padx=5, pady=2)
    good_winrate_vars[role] = good_winrate_var

    good_recent_var = tk.BooleanVar()
    ttk.Checkbutton(frame, text="Good Recent", variable=good_recent_var).pack(anchor='w', padx=5, pady=2)
    good_recent_vars[role] = good_recent_var

    zoggy_recent_var = tk.BooleanVar()
    ttk.Checkbutton(frame, text="ZOGGY Recent", variable=zoggy_recent_var).pack(anchor='w', padx=5, pady=2)
    zoggy_recent_vars[role] = zoggy_recent_var

    autofill_var = tk.BooleanVar()
    ttk.Checkbutton(frame, text="Autofill", variable=autofill_var).pack(anchor='w', padx=5, pady=2)
    autofill_vars[role] = autofill_var

    champ_experience_var = tk.BooleanVar()
    ttk.Checkbutton(frame, text="1-2nd time champ", variable=champ_experience_var).pack(anchor='w', padx=5, pady=2)
    champ_experience_vars[role] = champ_experience_var

    bad_winrate_var = tk.BooleanVar()  # Added bad_winrate
    ttk.Checkbutton(frame, text="Bad winrate", variable=bad_winrate_var).pack(anchor='w', padx=5, pady=2)
    bad_winrate_vars[role] = bad_winrate_var

    bad_recent_var = tk.BooleanVar()
    ttk.Checkbutton(frame, text="Bad Recent", variable=bad_recent_var).pack(anchor='w', padx=5, pady=2)
    bad_recent_vars[role] = bad_recent_var

    very_bad_recent_var = tk.BooleanVar()
    ttk.Checkbutton(frame, text="Very Bad Recent", variable=very_bad_recent_var).pack(anchor='w', padx=5, pady=2)
    very_bad_recent_vars[role] = very_bad_recent_var

# Additional Checkboxes
additional_frame = ttk.LabelFrame(root, text="Additional Points")
additional_frame.grid(row=1, column=2, padx=10, pady=5, sticky='w')

bad_mental_var = tk.BooleanVar()
ttk.Checkbutton(additional_frame, text="Bad Mental", variable=bad_mental_var).pack(anchor='w', padx=5, pady=2)

comp_diff_sad_var = tk.BooleanVar()
ttk.Checkbutton(additional_frame, text="Comp Diff Lame", variable=comp_diff_sad_var).pack(anchor='w', padx=5, pady=2)

comp_diff_happy_var = tk.BooleanVar()
ttk.Checkbutton(additional_frame, text="Comp Diff Jipie", variable=comp_diff_happy_var).pack(anchor='w', padx=5, pady=2)

calculate_btn = ttk.Button(root, text="Calculate Points", command=calculate_points)
calculate_btn.grid(row=2, column=0, pady=10)

reset_btn = ttk.Button(root, text="Reset", command=reset)
reset_btn.grid(row=2, column=1, pady=10)

result_var = tk.StringVar()
result_label = ttk.Label(root, textvariable=result_var, font=("Arial", 14))
result_label.grid(row=2, column=2, columnspan=2, pady=10)

root.mainloop()
