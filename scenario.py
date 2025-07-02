
class GameState:
    def __init__(self):
        self.current_level = 1
        self.objectives = []
        self.completed_objectives = []

    def add_objective(self, objective):
        self.objectives.append(objective)

    def complete_objective(self, objective):
        if objective in self.objectives:
            self.completed_objectives.append(objective)
            self.objectives.remove(objective)

    def is_level_complete(self):
        return not self.objectives