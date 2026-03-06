class NFA:
    def __init__(self, start, end):
        self.start = start
        self.end = end

# Input
regex = input("Enter regular expression (a*): ")

# States
start_state = 0
loop_state = 1
final_state = 2

# Output
print("\nNFA Representation")
print("Start State:", start_state)
print("Transitions:")
print(f"{start_state} --ε--> {loop_state}")
print(f"{loop_state} --a--> {loop_state}")
print(f"{loop_state} --ε--> {final_state}")
print("Final State:", final_state)
