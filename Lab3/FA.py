
def get_option():
    print("\nPlease choose an option:\n"
          "0 - exit\n"
          "1 - display states\n"
          "2 - display the alphabet\n"
          "3 - display the initial state\n"
          "4 - display the final states\n"
          "5 - display the transitions\n"
          "6 - check dfa\n")
    return int(input("option = "))


class FA:
    def __init__(self):
        self.__states = []
        self.__alphabet = []
        self.__transitions = []
        self.__init_state = ''
        self.__final_states = []

    def read_file(self, file):
        f = open(file, "r")
        i = 0
        for line in f:
            elements = line.split("\n")[0].split(",")
            if i == 0:
                self.__states = elements
            elif i == 1:
                self.__alphabet = elements
            elif i == 2:
                self.__init_state = elements[0]
            elif i == 3:
                self.__final_states = elements
            else:
                self.__transitions.append(elements)
            i += 1
        f.close()

    def get_transition_for(self, s, a):
        t_list = []
        for transition in self.__transitions:
            if transition[0] == s and transition[1] == a:
                t_list.append(transition[2])
        return t_list

    def check_dfa(self, sequence):
        crt_states = [self.__init_state]
        i = 0
        for char in sequence:
            if char not in self.__alphabet:
                print("invalid input")
                return False
            next_states = []
            for crt_state in crt_states:
                t_list = self.get_transition_for(crt_state, char)
                if len(t_list) == 0:
                    if i != len(sequence)-1:
                        return False
                    if crt_state not in self.__final_states:
                        return False
                elif i == len(sequence) - 1:
                    for t in t_list:
                        if t not in self.__final_states:
                            return False
                else:
                    for t in t_list:
                        if t not in next_states:
                            next_states.append(t)
            crt_states = next_states
            print(crt_states, char)
            i = i+1
        return True

    def run_menu(self):
        while True:
            opt = get_option()
            if opt == 0:
                exit()
            elif opt == 1:
                print("\nthe states are: ", self.__states)
            elif opt == 2:
                print("\nthe alphabet is: ", self.__alphabet)
            elif opt == 3:
                print("\nthe initial state is: ", self.__init_state)
            elif opt == 4:
                print("\nthe final states are: ", self.__final_states)
            elif opt == 5:
                print("\nthe transitions are: ")
                for transition in self.__transitions:
                    print(transition[0]+", "+transition[1]+" -> "+transition[2])
            elif opt == 6:
                sequence = input("Input the sequence: ")
                k = self.check_dfa(sequence)
                print(k)
                if k:
                    print("it is accepted")
                else:
                    print("it is not accepted")

