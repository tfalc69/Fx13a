class MoneyManager:
    def __init__(self, initial_balance):
        self.initial_balance = initial_balance
        self.current_balance = initial_balance
        self.risk_per_trade = 0.02  # 2%
        self.winning_streak = 0
        self.losing_streak = 0
        self.total_trades = 0
        self.profitable_trades = 0

    def calculate_position_size(self):
        base_position = self.current_balance * self.risk_per_trade
        if self.winning_streak >= 3:
            return base_position * (1 + (self.winning_streak * 0.1))
        if self.losing_streak >= 2:
            return base_position * (0.5 ** self.losing_streak)
        return base_position

    def update_balance(self, profit_loss):
        self.current_balance += profit_loss
        if profit_loss > 0:
            self.winning_streak += 1
            self.losing_streak = 0
            self.profitable_trades += 1
        else:
            self.losing_streak += 1
            self.winning_streak = 0
        self.total_trades += 1
