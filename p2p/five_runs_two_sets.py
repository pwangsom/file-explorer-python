
class ParetoSets:

    set_id_mapping = [["run1_NONE", 0],
                      ["run1_DA_DAG", 1],
                      ["run2_NONE", 2],
                      ["run2_DA_DAG", 3],
                      ["run3_NONE", 4],
                      ["run3_DA_DAG", 5],
                      ["run4_NONE", 6],
                      ["run4_DA_DAG", 7],
                      ["run5_NONE", 8],
                      ["run5_DA_DAG", 9]]

    def __init__(self, name):
        self.name = name
        self.all_solution_list = []
        self.normalized_list = {}
        self.hypervolume_list = [0.0] * len(self.set_id_mapping)

        return

    def add_pareto_set(self, lines, workflow_run):

        set_id = 1
        index = 0

        for i in range(len(self.set_id_mapping)):
            if self.set_id_mapping[i][0] == workflow_run:
                set_id = self.set_id_mapping[i][1]

        for _line in lines:
            objectives = _line.split(",")
            self.all_solution_list.append([set_id, index, float(objectives[0]), float(objectives[1]),
                                       float(objectives[2]), 0.0, 0.0, 0.0])
            index += 1

        return

    def add_normalized_solution(self, solution):

        if solution[0] not in self.normalized_list:
            self.normalized_list[solution[0]] = []

        self.normalized_list[solution[0]].append([solution[5], solution[6], solution[7]])

        return
    
    def print_all_solution_list(self):
        print(self.name)

        for _solution in self.all_solution_list:
            print(_solution)

        return

    def print_normalized_list(self):
        print(self.name)

        for k, v in self.normalized_list.items():
            print(k)

            for j in v:
                print(j)

        return