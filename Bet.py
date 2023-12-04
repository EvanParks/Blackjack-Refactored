class Bet():
    def __init__(self):
        self.bet_amount = 0 
        self.bet_chips = {
            '25' : 0, 
            '50' : 0, 
            '100' : 0, 
            '500' : 0, 
            '1000': 0, 
                    }

    def set_bet_amount(self, value):
        self.bet_amount = value 

    def get_bet_amount(self):
        return self.bet_amount 

    def get_bet_chips(self):
        return self.bet_chips
    
    def calculate_chip_total(self):
        total = 0
        for key, value in self.bet_chips.items():
            total += int(key) * value

        return total 

    def return_chips(self, player, player_win):
        for key, value in self.bet_chips.items():
            if player_win:
                for i in range(value):
                    player.get_chips()[key] += 2
                    self.bet_chips[key] -= 1 
            else:
                for i in range(value):
                    player.get_chips()[key] += 1
                    self.bet_chips[key] -= 1

    def adjust_chips(self, player):
        total = 0
        for key, value in player.get_chips().items():
            total += int(key) * value 
            player.get_chips()[key] = 0

        while total > 0:
            for key, value in player.get_chips().items():
                if total >= int(key):
                    player.get_chips()[key] += 1
                    total -= int(key) 

    def apply_double_down_chips(self, player, amount):
        chips = [] 

        denominations = ['1000', '500', '100', '50', '25']

        for denomination in denominations:
            chip_value = int(denomination)
            chip_count = player.get_chips()[denomination]

            while amount >= chip_value and chip_count > 0:
                chips.append(chip_value)
                amount -= chip_value
                chip_count -= 1

        for i in range(len(chips)):
            player.get_chips()[str(chips[i])] -= 1
            self.bet_chips[str(chips[i])] += 1  

    def reset_chips(self):
        self.bet_chips = {
            '25' : 0, 
            '50' : 0, 
            '100' : 0, 
            '500' : 0, 
            '1000': 0, 
                    }
        self.bet_amount = 0 