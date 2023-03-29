class Ism:
    def __init__(self, ism_word):
        self.word = ism_word
        self.un = self.word.split("'ٌ'")
        self.an = self.word.split("'ً'")
        self.en = self.word.split("'ٍ'")
        self.ani = self.word.split("انِ")
        self.una = self.word.split('وْنَ')
        self.ini = self.word.split("يْنِ")
        self.ena = self.word.split("يْنَ")

    def get_status(self):
        if len(self.un) > 1 or len(self.ani) > 1 or len(self.una) > 1:
            print("Raf")

        elif len(self.an) > 1:
            print("Nasb")

        elif len(self.en) > 1:
            print("Jarr")

        elif len(self.ini) > 1 or len(self.ena) > 1:
            print("Nasb or Jarr")

    def get_number(self):
        if len(self.un) > 1 or len(self.an) > 1 or len(self.en) > 1:
            print("Singular")

        elif len(self.ani) > 1 or len(self.ini) > 1:
            print("Dual")

        elif len(self.una) > 1 or len(self.ena) > 1:
            print("Plural")

    def get_gender(self):
        print("gender")

    def get_type(self):
        print("type")


p = Ism("مُسْلِمِيْنَ")
p.get_status()
p.get_number()
