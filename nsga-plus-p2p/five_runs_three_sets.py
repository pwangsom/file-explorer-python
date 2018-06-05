
class ParetoSets:

    set_id_mapping = [["run1_NONE_false", 0],
                      ["run1_DA_DAG_false", 1],
                      ["run1_DA_DAG_true", 2],
                      ["run2_NONE_false", 3],
                      ["run2_DA_DAG_false", 4],
                      ["run2_DA_DAG_true", 5],
                      ["run3_NONE_false", 6],
                      ["run3_DA_DAG_false", 7],
                      ["run3_DA_DAG_true", 8],
                      ["run4_NONE_false", 9],
                      ["run4_DA_DAG_false", 10],
                      ["run4_DA_DAG_true", 11],
                      ["run5_NONE_false", 12],
                      ["run5_DA_DAG_false", 13],
                      ["run5_DA_DAG_true", 14]]

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