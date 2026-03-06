# Simple Regex to NFA (single symbol)

class NFA:
    def __init__(self, start, symbol, end):
        self.start = start
        self.symbol = symbol
        self.end = end

# Input
regex = input("Enter regular expression: ")

# Create NFA
start_state = 0
end_state = 1
nfa = NFA(start_state, regex, end_state)

# Output
print("\nNFA Representation")
print("Start State:", nfa.start)
print("Transition:", f"{nfa.start} --{nfa.symbol}--> {nfa.end}")
print("Final State:", nfa.end)
