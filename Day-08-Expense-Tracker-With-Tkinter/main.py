
import tkinter as tk
from tkinter import ttk, messagebox
import json
import uuid
import math
from pathlib import Path


class ExpenseTracker:
    def __init__(self, root):
        self.root = root
        self.root.title("Personal Expense Tracker")
        self.root.geometry("950x720")
        self.root.configure(bg="#1e1e2e")
        self.root.minsize(800, 650)

        self.data_file = Path(__file__).with_name("expenses.json")
        self.categories = [
            "Food",
            "Transportation",
            "Shopping",
            "Entertainment",
            "Other"
        ]

        self.expenses = self.load_expenses()

        self.setup_styles()
        self.create_widgets()
        self.refresh_table()

    def load_expenses(self):
        if not self.data_file.exists():
            return []

        try:
            with open(self.data_file, "r", encoding="utf-8") as file:
                data = json.load(file)

            if not isinstance(data, list):
                raise ValueError("Invalid data format.")

            for expense in data:
                if not isinstance(expense, dict):
                    raise ValueError("Invalid expense record.")

                if "id" not in expense:
                    expense["id"] = str(uuid.uuid4())

                if "category" not in expense:
                    expense["category"] = "Other"

                if not isinstance(expense.get("description"), str):
                    raise ValueError("Invalid description.")

                amount = expense.get("amount")

                if (
                    not isinstance(amount, (int, float))
                    or isinstance(amount, bool)
                    or not math.isfinite(amount)
                    or amount <= 0
                ):
                    raise ValueError("Invalid amount.")

            return data

        except (OSError, ValueError, TypeError, json.JSONDecodeError) as error:
            messagebox.showerror("Load Error", str(error))
            return []

    def save_expenses(self):
        try:
            with open(self.data_file, "w", encoding="utf-8") as file:
                json.dump(self.expenses, file, indent=4)
            return True

        except OSError as error:
            messagebox.showerror("Save Error", str(error))
            return False

    def setup_styles(self):
        style = ttk.Style()
        style.theme_use("clam")

        style.configure(
            "Treeview",
            background="#2a2a3e",
            foreground="white",
            fieldbackground="#2a2a3e",
            rowheight=32,
            font=("Arial", 11),
            borderwidth=0
        )

        style.configure(
            "Treeview.Heading",
            background="#45455f",
            foreground="white",
            font=("Arial", 11, "bold")
        )

        style.map(
            "Treeview",
            background=[("selected", "#6366f1")],
            foreground=[("selected", "white")]
        )

    def create_widgets(self):
        header = tk.Label(
            self.root,
            text="Personal Expense Tracker",
            font=("Arial", 26, "bold"),
            bg="#1e1e2e",
            fg="white"
        )
        header.pack(pady=(25, 5))

        subtitle = tk.Label(
            self.root,
            text="Manage your spending in one place",
            font=("Arial", 11),
            bg="#1e1e2e",
            fg="#a0a0b5"
        )
        subtitle.pack(pady=(0, 20))

        form_frame = tk.Frame(
            self.root,
            bg="#2a2a3e",
            padx=20,
            pady=20
        )
        form_frame.pack(fill="x", padx=40)

        form_frame.columnconfigure(0, weight=1)
        form_frame.columnconfigure(1, weight=1)
        form_frame.columnconfigure(2, weight=1)

        fields = [
            ("Description", 0),
            ("Amount (₺)", 1),
            ("Category", 2)
        ]

        for text, column in fields:
            label = tk.Label(
                form_frame,
                text=text,
                font=("Arial", 11),
                bg="#2a2a3e",
                fg="white"
            )
            label.grid(row=0, column=column, pady=5)

        self.description_entry = tk.Entry(
            form_frame,
            font=("Arial", 12),
            width=24
        )
        self.description_entry.grid(
            row=1, column=0, padx=8, sticky="ew"
        )

        self.amount_entry = tk.Entry(
            form_frame,
            font=("Arial", 12),
            width=14
        )
        self.amount_entry.grid(
            row=1, column=1, padx=8, sticky="ew"
        )

        self.category_box = ttk.Combobox(
            form_frame,
            values=self.categories,
            state="readonly",
            font=("Arial", 11),
            width=18
        )
        self.category_box.set("Food")
        self.category_box.grid(
            row=1, column=2, padx=8, sticky="ew"
        )

        add_button = tk.Button(
            form_frame,
            text="+ Add Expense",
            font=("Arial", 12, "bold"),
            bg="#6366f1",
            fg="white",
            activebackground="#4f46e5",
            activeforeground="white",
            relief="flat",
            cursor="hand2",
            command=self.add_expense
        )
        add_button.grid(
            row=2,
            column=0,
            columnspan=3,
            pady=(20, 0),
            ipadx=30,
            ipady=6
        )

        stats_frame = tk.Frame(
            self.root,
            bg="#1e1e2e"
        )
        stats_frame.pack(fill="x", padx=45, pady=20)

        self.total_label = tk.Label(
            stats_frame,
            text="Total Spent: ₺0.00",
            font=("Arial", 15, "bold"),
            bg="#1e1e2e",
            fg="white"
        )
        self.total_label.pack(side="left")

        self.count_label = tk.Label(
            stats_frame,
            text="Transactions: 0",
            font=("Arial", 12),
            bg="#1e1e2e",
            fg="#a0a0b5"
        )
        self.count_label.pack(side="right")

        filter_frame = tk.Frame(
            self.root,
            bg="#1e1e2e"
        )
        filter_frame.pack(fill="x", padx=45, pady=(0, 10))

        filter_label = tk.Label(
            filter_frame,
            text="Filter:",
            font=("Arial", 11),
            bg="#1e1e2e",
            fg="white"
        )
        filter_label.pack(side="left", padx=(0, 10))

        self.filter_box = ttk.Combobox(
            filter_frame,
            values=["All Categories"] + self.categories,
            state="readonly",
            width=20
        )
        self.filter_box.set("All Categories")
        self.filter_box.pack(side="left")

        self.filter_box.bind(
            "<<ComboboxSelected>>",
            self.refresh_table
        )

        table_frame = tk.Frame(
            self.root,
            bg="#1e1e2e"
        )
        table_frame.pack(
            fill="both",
            expand=True,
            padx=45,
            pady=10
        )

        self.expense_table = ttk.Treeview(
            table_frame,
            columns=("Description", "Category", "Amount"),
            show="headings",
            selectmode="browse"
        )

        self.expense_table.heading(
            "Description", text="Description"
        )
        self.expense_table.heading(
            "Category", text="Category"
        )
        self.expense_table.heading(
            "Amount", text="Amount (₺)"
        )

        self.expense_table.column(
            "Description", width=300
        )
        self.expense_table.column(
            "Category", width=180, anchor="center"
        )
        self.expense_table.column(
            "Amount", width=150, anchor="center"
        )

        scrollbar = ttk.Scrollbar(
            table_frame,
            orient="vertical",
            command=self.expense_table.yview
        )

        self.expense_table.configure(
            yscrollcommand=scrollbar.set
        )

        scrollbar.pack(side="right", fill="y")
        self.expense_table.pack(
            side="left", fill="both", expand=True
        )

        delete_button = tk.Button(
            self.root,
            text="Delete Selected Expense",
            font=("Arial", 11, "bold"),
            bg="#b44350",
            fg="white",
            activebackground="#963744",
            activeforeground="white",
            relief="flat",
            cursor="hand2",
            command=self.delete_expense
        )
        delete_button.pack(pady=(5, 20), ipadx=15, ipady=7)

    def refresh_table(self, event=None):
        for item in self.expense_table.get_children():
            self.expense_table.delete(item)

        selected_category = self.filter_box.get()

        visible_expenses = [
            expense for expense in self.expenses
            if (
                selected_category == "All Categories"
                or expense["category"] == selected_category
            )
        ]

        for expense in visible_expenses:
            self.expense_table.insert(
                "",
                tk.END,
                iid=expense["id"],
                values=(
                    expense["description"],
                    expense["category"],
                    f'{expense["amount"]:.2f}'
                )
            )

        total = sum(
            expense["amount"] for expense in visible_expenses
        )

        self.total_label.config(
            text=f"Total Spent: ₺{total:.2f}"
        )

        self.count_label.config(
            text=f"Transactions: {len(visible_expenses)}"
        )

    def add_expense(self):
        description = self.description_entry.get().strip()

        if not description:
            messagebox.showerror(
                "Invalid Input",
                "Please enter a description."
            )
            return

        try:
            amount = float(self.amount_entry.get())
        except ValueError:
            messagebox.showerror(
                "Invalid Input",
                "Please enter a valid amount."
            )
            return

        if not math.isfinite(amount) or amount <= 0:
            messagebox.showerror(
                "Invalid Input",
                "Amount must be a positive, finite number."
            )
            return

        expense = {
            "id": str(uuid.uuid4()),
            "description": description,
            "amount": amount,
            "category": self.category_box.get()
        }

        self.expenses.append(expense)

        if not self.save_expenses():
            self.expenses.pop()
            return

        self.description_entry.delete(0, tk.END)
        self.amount_entry.delete(0, tk.END)

        self.refresh_table()

    def delete_expense(self):
        selected = self.expense_table.selection()

        if not selected:
            messagebox.showwarning(
                "No Selection",
                "Please select an expense."
            )
            return

        selected_id = selected[0]

        expense_to_delete = next(
            (
                expense for expense in self.expenses
                if expense["id"] == selected_id
            ),
            None
        )

        if expense_to_delete is None:
            return

        confirmed = messagebox.askyesno(
            "Confirm Deletion",
            "Are you sure you want to delete this expense?"
        )

        if not confirmed:
            return

        index = self.expenses.index(expense_to_delete)
        self.expenses.pop(index)

        if not self.save_expenses():
            self.expenses.insert(index, expense_to_delete)
            return

        self.refresh_table()


if __name__ == "__main__":
    root = tk.Tk()
    app = ExpenseTracker(root)
    root.mainloop()
