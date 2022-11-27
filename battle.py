class Battle:
    def __init__(self, gorkha_army, foe_army, foe_kingdom):
        self.gorkha_army = gorkha_army
        self.foe_army = foe_army
        self.foe = foe_kingdom

    # def match_making(self):

    def war(self):
        if self.gorkha_army > self.foe_army:
            print(f"Congratulation!!! You conquered {self.foe}")
            return True
        else:
            print(f"You are defeated by {self.foe}!")
            return False
