class Part:

    def __init__(self, mn, pn, c):
        self.__model_number = mn
        self.__part_number = pn
        self.__cost = c

    def show_part(self):
        print(f"Model Number is {self.__model_number}, part number is {self.__part_number} and cost is {self.__cost} pesos.")


part = Part(6244, 373, 217.55)
part.show_part()
