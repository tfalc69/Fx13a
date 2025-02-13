import numpy as np
import talib

class AIAnalyzer:
    def analyze_transactions(self, transactions):
        if not transactions:
            return "Brak danych do analizy."
        profits = [t.get('profit', 0) for t in transactions]
        avg_profit = sum(profits) / len(profits)
        if avg_profit < 0:
            return "Sugerowana zmiana strategii: dostosuj parametry wskaźników."
        else:
            return "Strategia działa poprawnie."
