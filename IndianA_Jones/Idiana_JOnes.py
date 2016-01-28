class CLI:
    @staticmethod
    def input_validate(input_text):
        item = input_text[0]
        if item == "exit" or item == "EXIT":
            return True
        if len(input_text) != 3:
            raise Exception("You forgot one argument!!!")
        weight = input_text[1]
        value = input_text[2]
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
        self.tuple = ()
        self.N = 0

    def make_tuple_of_items(self, item, value, weight):
        self.tuple += ((item, int(value), int(weight)), )
        return self.tuple

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
            self.make_tuple_of_items(text[0], text[1], text[2])
            text = self.input_command()
        return self.tuple

    def get_N(self):
        return self.N


class IndianaJones:

    @staticmethod
    def knapsack(tuples, limit):
        # generate a table with values
        #  initialize a matrix with zeros
        table = [[0 for w in range(0, limit + 1)] for j in range(0, len(tuples) + 1)]
        for j in range(1, len(tuples) + 1):
            #  get all items one by one
            item = tuples[j-1][0]
            wt = tuples[j-1][1]
            val = tuples[j-1][2]

            for w in range(1, limit + 1):
                if w < wt:
                    table[j][w] = table[j-1][w]
                else:
                    table[j][w] = max(table[j-1][w],
                                      table[j-1][w-wt] + val)

        result = []
        for j in range(len(tuples), 0, -1):
            if table[j][limit] != table[j-1][limit]:
                item, wt, val = tuples[j-1]
                result.append(tuples[j-1])
                limit -= wt
        return result

    def __init__(self):
        cli = CLI()
        # self.list = []
        self.tuple = cli.input()
        print(self.tuple)
        self.N = cli.get_N()
        # self.list_of_carried_items = []

    # def dict_to_list(self):
    #     for item in self.dict:
    #         self.list.append(self.dict[item])
    #     self.list = sorted(self.list)
    #     self.list.reverse()
    #     return self.list

    # def get_value_from_dict(self, value):
    #     for item in self.dict:
    #         if self.dict[item] == value:
    #             return item

    # def carry_items(self):
    #     self.dict_to_list()
    #     for tuplee in self.list:
    #         if tuplee[1] <= self.N:
    #             self.list_of_carried_items.append(self.get_value_from_dict(tuplee))
    #             self.N -= tuplee[1]
    #     return self.list_of_carried_items

    def totalvalue(self, comb):
        ' Totalise a particular combination of items'
        totwt = totval = 0
        for item, wt, val in comb:
            totwt += wt
            totval += val
        return (totval, -totwt) if totwt <= 400 else (0, 0)

    # items = (
                        #     ("map", 9, 150), ("compass", 13, 35), ("water", 153, 200), ("sandwich", 50, 160),
                        #     ("glucose", 15, 60), ("tin", 68, 45), ("banana", 27, 60), ("apple", 39, 40),
                        #     ("cheese", 23, 30), ("beer", 52, 10), ("suntan cream", 11, 70), ("camera", 32, 30),
                        #     ("t-shirt", 24, 15), ("trousers", 48, 10), ("umbrella", 73, 40),
                        #     ("waterproof trousers", 42, 70), ("waterproof overclothes", 43, 75),
                        #     ("note-case", 22, 80), ("sunglasses", 7, 20), ("towel", 18, 12),
                        #     ("socks", 4, 50), ("book", 30, 10),
                        #     )

    def message_carry_items(self, result):
        return ("Indiana JOnes can carry the following items\n  " +
                '\n  '.join(item for (item, wt, val) in result))

    def message_total_value(self, result):
        return ("for a total value of %i and a total weight of %i" % (result))

    def carry_items(self):
        result = IndianaJones.knapsack(self.tuple, self.N)
        val, wt = self.totalvalue(result)
        print(self.message_carry_items(result))
        print(self.message_total_value((val, -wt)))


def main():
    # test = CLI()
    # print(test.input())
    indi = IndianaJones()
    print(indi.carry_items())

if __name__ == '__main__':
    main()

