# NFA to DFA (User Input - Simple Version)

n = int(input("Enter number of states: "))
states = input("Enter states (space separated): ").split()
alphabet = input("Enter alphabet symbols (space separated): ").split()

nfa = {}

print("Enter transitions (comma separated, use - for no transition):")
for state in states:
    nfa[state] = {}
    for symbol in alphabet:
        trans = input(f"Transition from {state} on {symbol}: ")
        if trans == "-":
            nfa[state][symbol] = []
        else:
            nfa[state][symbol] = trans.split(",")

start = input("Enter start state: ")

# Subset Construction
dfa = []
queue = [[start]]

while queue:
    current = queue.pop(0)
    if current not in dfa:
        dfa.append(current)

    for symbol in alphabet:
        new_state = []
        for s in current:
            new_state += nfa[s][symbol]

        new_state = list(set(new_state))

        if new_state and new_state not in dfa:
            queue.append(new_state)

        print(current, "--", symbol, "-->", new_state)
