
from two_pareto_sets import TwoParetoSets

class ParetoFileManager:

    workflow_lists = ["epigenomics", "inspiral", "montage"]
    workflow_sizes = ["_50_", "_100_", "_500_", "_1000_"]
    workflow_types = ["DA_DAG", "NONE"]

    def __init__(self):
        self.parato_sets = []

        return

    def read_file(self, pathFileName):
        workflowName = pathFileName.rpartition('\\')[2]
        print("")
        print("Processing: " + workflowName)
                
        lines = self.read_line(pathFileName)

        workflowKeys = self.determine_workflow_key(workflowName)

        self.process_worklflow_key(workflowKeys, lines)

        return


    def process_worklflow_key(self, workflowKey, lines):
        print(workflowKey[3])

        if self.parato_sets:

            if any(workflowKey[3] == pareto_set[0] for pareto_set in self.parato_sets):
                
                print(workflowKey[3]  + " exists..")
                self.add_two_sets(workflowKey, lines)

            else:                
                print(workflowKey[3]  + " does not exists..")
                matched_set = self.create_new_two_sets(workflowKey, lines)
                self.parato_sets.append([workflowKey[3], matched_set])
            
        else:
            print("First time..")
            matched_set = self.create_new_two_sets(workflowKey, lines)
            self.parato_sets.append([workflowKey[3], matched_set])

        return
    
    def create_new_two_sets(self, workflowKey, lines):            
        two_sets = TwoParetoSets(workflowKey[3])
        two_sets.add_pareto_set(lines, workflowKey[2])

        return two_sets

    def add_two_sets(self, workflowKey, lines):

        for pareto_set in self.parato_sets:
            if workflowKey[3] == pareto_set[0]:
                pareto_set[1].add_pareto_set(lines, workflowKey[2])

        return

    def read_line(self, pathFileName):
        with open(pathFileName, 'rt') as fd:
            lines = fd.readlines()
        return lines


    def determine_workflow_key(self, workflowName):

        workflow_key = []
        
        for _name in self.workflow_lists:
            if(workflowName.find(_name) > -1):
                workflow_key.append(_name)
        
        for _size in self.workflow_sizes:
            if(workflowName.find(_size) > -1):
                workflow_key.append(_size)
        
        for _type in self.workflow_types:
            if(workflowName.find(_type) > -1):
                workflow_key.append(_type)

        if len(workflow_key) == 3:
            key_name = workflow_key[0] + workflow_key[1]
            workflow_key.append(key_name[:-1])
            print(workflow_key)

        return workflow_key

    def print_parato_sets(self):

        for pareto_set in self.parato_sets:
            pareto_set[1].print_detail()


        return