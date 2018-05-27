
from three_objectives_point import ThreeObjectivesPoint

class TwoParetoSets:

    def __init__(self, name):
        self.name = name
        self.firstParetoSet = []
        self.secondParetoSet = []

        self.firstObjectiveList = []
        self.secondObjectiveList = []
        self.thirdObjectiveList = []

        return

    def add_pareto_set(self, lines, workflowType):

        points = []
        set_id = 1
        index = 0

        if workflowType == "NONE":
            set_id = 2

        for line in lines:
            objectives = line.split(",")
            point = ThreeObjectivesPoint(float(objectives[0]), float(objectives[1]), float(objectives[2]))
            self.firstObjectiveList.append([set_id, index, float(objectives[0])])
            self.secondObjectiveList.append([set_id, index, float(objectives[1])])            
            self.thirdObjectiveList.append([set_id, index, float(objectives[2])])
            points.append(point)
            index += 1

        if set_id == 1:
            self.firstParetoSet = points
        else:
            self.secondParetoSet = points

        return

    def print_detail(self):
        print(self.name)

        for idx, val in enumerate(self.firstObjectiveList, start = 0):
            print("-> " + str(val[0]) + ", " + str(val[1]) + ", " + str(val[2]) + ", "
                        + str(self.secondObjectiveList[idx][2]) + ", " + str(self.thirdObjectiveList[idx][2]))
        
        return

