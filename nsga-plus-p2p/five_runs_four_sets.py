
class ParetoSets:

    set_id_mapping = [["run1_NONE_false", 0],
                      ["run1_NONE_true", 1],
                      ["run1_DA_DAG_false", 2],
                      ["run1_DA_DAG_true", 3],
                      ["run2_NONE_false", 4],
                      ["run2_NONE_true", 5],
                      ["run2_DA_DAG_false", 6],
                      ["run2_DA_DAG_true", 7],
                      ["run3_NONE_false", 8],
                      ["run3_NONE_true", 9],
                      ["run3_DA_DAG_false", 10],
                      ["run3_DA_DAG_true", 11],
                      ["run4_NONE_false", 12],
                      ["run4_NONE_true", 13],
                      ["run4_DA_DAG_false", 14],
                      ["run4_DA_DAG_true", 15],
                      ["run5_NONE_false", 16],
                      ["run5_NONE_true", 17],
                      ["run5_DA_DAG_false", 18],
                      ["run5_DA_DAG_true", 19]]

    def __init__(self, name):
        self.name = name
        self.all_solution_list = []
        self.normalized_list = {}
        self.hypervolume_list = [0.0] * len(self.set_id_mapping)
        self.no_of_pareto = [0] * len(self.set_id_mapping)

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