class Score:
    def __init__(self, fe, gb, cs, cp):
        self.fndEng = fe
        self.genBus = gb
        self.comSys = cs
        self.comPro = cp

s1 = Score(100, 99, 98, 97)
print("--- Your Score ---")
print("Foundation English :\t\t\t", s1.fndEng,
      "\nGeneral Business :\t\t\t", s1.genBus,
      "\nIntroduction to Computer System :\t", s1.comSys,
      "\nComputer Programming :\t\t\t",s1.comPro)
