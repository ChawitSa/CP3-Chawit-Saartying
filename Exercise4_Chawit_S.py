class Score:
    def __init__(self, fe, gb, cs, cp):
        self.fndEng = fe
        self.genBus = gb
        self.comSys = cs
        self.ComPro = cp

s1 = Score(100, 99, 98, 97)
print("--- Your Score ---")
print("Foundation English : ", s1.fndEng)
