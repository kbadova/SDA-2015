class CLI:
    @staticmethod
    def input_validate(input_text):
        item = input_text[0]
        if item == "exit" or item == "EXIT":
            return True
        if len(input_text) != 3:
            raise Exception("You forgot one argument!!!")
        value = input_text[1]
        weight = input_text[2]
        if item.isdigit():
            raise TypeError("Please input in this order: item value weight")
        try:
            weight == int(weight)
            value == int(value)
        except (TypeError, ValueError):
            raise TypeError("Please input in this order: item value weight")

    @staticmethod
    def input_command():
        command = input()
        list_of_inputs = command.split(" ")
        CLI.input_validate(list_of_inputs)
        return list_of_inputs

    @staticmethod
    def validate_N(N):
        try:
            N == int(N)
        except (TypeError, ValueError):
            raise TypeError("PLease enter your capacity correctly!")

    @staticmethod
    def message_enter_N():
        return "Enter the capacity of your sack"

    @staticmethod
    def message_enter_items():
        return "Enter your items and exit:"

    def __init__(self):
        self.dict = {}
        self.N = 0

    def make_dict_of_items(self, item, value, weight):
        self.dict[item] = (int(value), int(weight))
        return self.dict

    def enter_N(self):
        print(CLI.message_enter_N())
        N = input()
        CLI.validate_N(N)
        return int(N)

    def input(self):
        self.N = self.enter_N()
        print(CLI.message_enter_items())
        text = CLI.input_command()
        while text[0] != "exit" and text[0] != "EXIT":
            self.make_dict_of_items(text[0], text[1], text[2])
            text = self.input_command()
        return self.dict

    def get_N(self):
        return self.N


class IndianaJones:
    def __init__(self):
        cli = CLI()
        self.list = []
        self.dict = cli.input()
        self.N = cli.get_N()
        self.list_of_carried_items = []

    def dict_to_list(self):
        for item in self.dict:
            self.list.append(self.dict[item])
        self.list = sorted(self.list)
        self.list.reverse()
        return self.list

    def get_value_from_dict(self, value):
        for item in self.dict:
            if self.dict[item] == value:
                return item

    def carry_items(self):
        self.dict_to_list()
        for tuplee in self.list:
            if tuplee[1] <= self.N:
                self.list_of_carried_items.append(self.get_value_from_dict(tuplee))
                self.N -= tuplee[1]
        return self.list_of_carried_items


def main():
    # test = CLI()
    # print(test.input())
    indi = IndianaJones()
    # print(indi.dict_to_list())
    print(indi.carry_items())

if __name__ == '__main__':
    main()

