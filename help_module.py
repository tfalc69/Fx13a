import tkinter as tk

class HelpWindow(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Pomoc")
        self.geometry("600x400")
        self.setup_ui()

    def setup_ui(self):
        help_text = (
            "FX13X1Bot - Pomoc i Instrukcje

"
            "Zakładki:
"
            "• Trading - uruchamianie bota, logi, wykresy
"
            "• Strategie - zarządzanie strategiami
"
            "• Wallet - zarządzanie kapitałem
"
            "• Nauka AI - analiza transakcji
"
            "• Pomoc - instrukcja obsługi
"
        )
        text_widget = tk.Text(self, wrap=tk.WORD)
        text_widget.insert(tk.END, help_text)
        text_widget.config(state=tk.DISABLED)
        text_widget.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
