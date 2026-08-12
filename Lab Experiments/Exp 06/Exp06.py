class VacuumCleaner:
    def __init__(self):
        # Environment state: Location A & B (0 = Clean, 1 = Dirty)
        self.environment = {'A': 1, 'B': 1}
        self.agent_location = 'A'

    def clean(self):
        print(f"Initial State: {self.environment}")
        while 1 in self.environment.values():
            loc = self.agent_location
            print(f"\nAgent at Location {loc}")
            
            if self.environment[loc] == 1:
                print(f"Location {loc} is Dirty. Cleaning...")
                self.environment[loc] = 0
                print(f"Location {loc} cleaned.")
            else:
                print(f"Location {loc} is already Clean.")

            # Move to the other location
            self.agent_location = 'B' if loc == 'A' else 'A'
            print(f"Moving to Location {self.agent_location}")

        print(f"\nAll locations cleaned! Final State: {self.environment}")

# Test Run
agent = VacuumCleaner()
agent.clean()
