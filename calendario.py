import tkinter as tk
import calendar


def show_calendar(year, month):
    # Create a window
    root = tk.Tk()
    root.title("Calendar")

    # Create a frame for the buttons
    buttons_frame = tk.Frame(root)
    buttons_frame.pack(side="top", fill="x")

    # Create a button for the previous month
    prev_month_button = tk.Button(
        buttons_frame, text="<", command=lambda: show_calendar(year, month - 1))
    prev_month_button.pack(side="left")

    # Create a label for the month and year
    month_label = tk.Label(
        buttons_frame, text=calendar.month_name[month] + " " + str(year), font=("TkDefaultFont", 14))
    month_label.pack(side="left")

    # Create a button for the next month
    next_month_button = tk.Button(
        buttons_frame, text=">", command=lambda: show_calendar(year, month + 1))
    next_month_button.pack(side="right")

    # Create a calendar
    cal = calendar.monthcalendar(year, month)

    # Create a frame to hold the calendar
    frame = tk.Frame(root)
    frame.pack(fill="both", expand=True)

    # Create labels for each day of the week
    for i, day in enumerate(calendar.day_abbr):
        label = tk.Label(frame, text=day, width=7, relief="solid")
        label.grid(row=0, column=i, sticky="ew")
        frame.columnconfigure(i, weight=1)

    # Create labels for each day of the month
    for i, row in enumerate(cal, 1):
        for j, day in enumerate(row):
            if day == 0:
                continue

            label = tk.Label(frame, text=day, width=7, relief="solid")
            label.grid(row=i, column=j, sticky="ewns")
            frame.columnconfigure(j, weight=1)
            frame.rowconfigure(i, weight=1)

    # Set the window to expand to fill the entire screen
    root.columnconfigure(0, weight=1)
    root.rowconfigure(0, weight=1)

    # Display the window
    root.mainloop()


# Display the calendar for February 2023
show_calendar(2023, 2)
