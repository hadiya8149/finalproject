class Score:
    def __init__(self, neg, neu, pos, compound):
        self.neg = neg
        self.neu = neu
        self.pos = pos
        self.compound = compound

score_1 = Score(0.072,0.754,0.174,0.9994)
print(score_1.neg)
