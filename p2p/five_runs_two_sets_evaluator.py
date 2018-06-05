
import numpy as np
from five_runs_two_sets import ParetoSets
from pygmo import hypervolume


class ParetoEvaluator:

    def __init__(self):
        self.workflow_pareto_sets = []
        return

    def evaluate_pareto_sets(self):
        for each_workflow_pareto in self.workflow_pareto_sets:
            self.normalize_solution_list(each_workflow_pareto)
            # each_workflow_pareto[1].print_all_solution_list()
            self.measure_hypervolume(each_workflow_pareto)
        return

    def normalize_solution_list(self, workflow_pareto_sets):

        _max = np.max(workflow_pareto_sets[1].all_solution_list, axis=0)
        _min = np.min(workflow_pareto_sets[1].all_solution_list, axis=0)
        # print(_max)
        # print(_min)

        for _solution in workflow_pareto_sets[1].all_solution_list:
            _solution[5] = (_solution[2]-_min[2])/(_max[2]-_min[2])
            _solution[6] = (_solution[3]-_min[3])/(_max[3]-_min[3])
            _solution[7] = (_solution[4]-_min[4])/(_max[4]-_min[4])

            workflow_pareto_sets[1].add_normalized_solution(_solution)

        return

    def measure_hypervolume(self, workflow_pareto_sets):

        print(workflow_pareto_sets[1].name)

        # workflow_pareto_sets[1].print_normalized_list()

        ref_point = [1, 1, 1]

        for k, v in workflow_pareto_sets[1].normalized_list.items():
            hv = hypervolume(v)
            workflow_pareto_sets[1].hypervolume_list[k] = hv.compute(ref_point)

        # print(workflow_pareto_sets[1].hypervolume_list)
        # print("")

        return
