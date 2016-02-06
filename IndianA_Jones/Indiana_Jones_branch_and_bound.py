from Idiana_JOnes import CLI

MAX_WEIGHT = 0
TUPLES = ()


class State():

    @staticmethod
    def upperbound(available):  # define upperbound using fractional knaksack
        upperbound = 0  # initial upperbound
        remaining = MAX_WEIGHT
        for avail, item in zip(available, TUPLES):
            weight_item = item[1]
            value_item = item[2]
            if weight_item * avail <= remaining:
                remaining -= weight_item
                upperbound += value_item * avail
            else:
                upperbound += value_item * remaining / weight_item
                break
        return upperbound

    @staticmethod
    def get_tuples(tuples):
        global TUPLES
        TUPLES = tuples

    @staticmethod
    def get_N(N):
        global MAX_WEIGHT
        MAX_WEIGHT = N

    def __init__(self, level, value, weight, token):
            # token = list marking if a task is token. ex. [1, 0, 0] means
            # item0 token, item1 non-token, item2 non-token
            # available = list marking all tasks available, not explored yet
            self.level = level
            self.value = value
            self.weight = weight
            self.token = token
            self.ub = State.upperbound(self.token[:self.level]+[1]*(len(TUPLES)-self.level))

    def develop(self):
        level = self.level + 1
        _, weight, value = TUPLES[self.level]
        left_weight = self.weight + weight
        print("max we" + str(MAX_WEIGHT) + str(len(TUPLES)))
        if left_weight <= MAX_WEIGHT:  # if not overweighted, give left child
            left_value = self.value + value
            left_token = self.token[:self.level]+[1]+self.token[level:]  # otbelqzvam che moje da bude vzet
            left_child = State(level, left_value, left_weight, left_token)
        else:
            left_child = None
        right_child = State(level, self.value, self.weight, self.token)
        return ([] if left_child is None else [left_child]) + [right_child]

    def carry_items():
        data_sorted = sorted(TUPLES, key=lambda k: float(k[2])/k[1])
        data_sorted.reverse()

        Root = State(0, 0, 0, [0] * len(data_sorted))  # start with nothing
        waiting_States = []  # list of States waiting to be explored
        current_state = Root
        while current_state.level < len(data_sorted):
            waiting_States.extend(current_state.develop())
            # sort the waiting list based on their upperbound
            waiting_States.sort(key=lambda x: x.ub)
            # explore the one with largest upperbound
            current_state = waiting_States.pop()
        best_item = [item for tok, (item, _, _)
                     in zip(current_state.token, data_sorted) if tok == 1]

        return "Total weight: {}\nTotal Value: {}\nItems:{}".\
               format(current_state.weight, current_state.value, best_item)


def main():
    cli = CLI()
    tuples = cli.input()
    N = cli.get_N()
    State.get_tuples(tuples)
    State.get_N(N)
    print(State.carry_items())

if __name__ == '__main__':
    main()


