# Simple NFA to DFA

# NFA definition
nfa = {
    'A': {'0': ['A', 'B'], '1': ['A']},
    'B': {'0': [], '1': ['B']}
}

alphabet = ['0', '1']
start = ['A']

dfa = []
queue = [start]

while queue:
    state = queue.pop(0)
    if state not in dfa:
        dfa.append(state)

    for symbol in alphabet:
        new_state = []
        for s in state:
            new_state += nfa[s][symbol]

        new_state = list(set(new_state))

        if new_state and new_state not in dfa:
            queue.append(new_state)

        print(state, "--", symbol, "-->", new_state)
