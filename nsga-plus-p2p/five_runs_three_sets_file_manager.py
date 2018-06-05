
from five_runs_three_sets import ParetoSets

class ParetoFileManager:

    key_index = 4

    workflow_lists = ["epigenomics", "inspiral", "montage"]
    workflow_sizes = ["_50_", "_100_", "_500_", "_1000_"]
    workflow_runs = ["run1", "run2", "run3", "run4", "run5"]
    workflow_types = ["NONE", "DA_DAG"]
    workflow_nsga = ["false", "true"]

    def __init__(self):
        self.workflow_pareto_sets = []

        return

    def read_file(self, path_file_name):
        workflow_name = path_file_name.rpartition('\\')[2]
        print("")
        print("Processing: " + workflow_name)
                
        lines = self.read_line(path_file_name)

        workflow_keys = self.determine_workflow_key(workflow_name)

        self.process_worklflow_key(workflow_keys, lines)

        return


    def process_worklflow_key(self, workflow_keys, lines):
        print(workflow_keys[3])

        if self.workflow_pareto_sets:

            if any(workflow_keys[self.key_index] == _set[0] for _set in self.workflow_pareto_sets):
                self.add_two_sets(workflow_keys, lines)

            else:                
                pareto_set_collection = self.create_new_two_sets(workflow_keys, lines)
                # Structure is as follow
                # [0] = workflow name e.g. epigenomics_50
                # [1] = pareto set structure
                # [2] = hypervolume of run1 of DA-DAG cluster 
                # [3] = hypervolume of run1 of NONE cluster 
                # [4] = hypervolume of run2 of DA-DAG cluster 
                # [5] = hypervolume of run2 of NONE cluster 
                # [6] = hypervolume of run3 of DA-DAG cluster 
                # [7] = hypervolume of run3 of NONE cluster 
                # [8] = hypervolume of run4 of DA-DAG cluster 
                # [9] = hypervolume of run4 of NONE cluster 
                # [10] = hypervolume of run5 of DA-DAG cluster 
                # [11] = hypervolume of run5 of NONE cluster 

                self.workflow_pareto_sets.append([workflow_keys[self.key_index], pareto_set_collection])
            
        else:
            pareto_set_collection = self.create_new_two_sets(workflow_keys, lines)
            self.workflow_pareto_sets.append([workflow_keys[self.key_index], pareto_set_collection])

        return
    
    def create_new_two_sets(self, workflow_keys, lines):            
        pareto_sets = ParetoSets(workflow_keys[self.key_index])
        pareto_sets.add_pareto_set(lines, workflow_keys[2] + "_" + workflow_keys[3])

        return pareto_sets

    def add_two_sets(self, workflow_keys, lines):

        for _set in self.workflow_pareto_sets:
            if workflow_keys[self.key_index] == _set[0]:
                _set[1].add_pareto_set(lines, workflow_keys[2] + "_" + workflow_keys[3])

        return

    def read_line(self, path_file_name):
        with open(path_file_name, 'rt') as fd:
            lines = fd.readlines()
        return lines


    def determine_workflow_key(self, workflow_name):

        workflow_keys = []
        
        for _name in self.workflow_lists:
            if(workflow_name.find(_name) > -1):
                workflow_keys.append(_name)
        
        for _size in self.workflow_sizes:
            if(workflow_name.find(_size) > -1):
                workflow_keys.append(_size)

        for _run in self.workflow_runs:
            if(workflow_name.find(_run) > -1):
                workflow_keys.append(_run)

        for _type in self.workflow_types:
            if(workflow_name.find(_type) > -1):
                for _nsga in self.workflow_nsga:
                    if(workflow_name.find(_nsga) > -1):
                        workflow_keys.append(_type + "_" + _nsga)

        if len(workflow_keys) == self.key_index:
            key_name = workflow_keys[0] + workflow_keys[1]
            workflow_keys.append(key_name[:-1])
            print(workflow_keys)

        return workflow_keys

    def print_parato_sets(self):

        for _set in self.workflow_pareto_sets:
            _set[1].print_detail()

        return