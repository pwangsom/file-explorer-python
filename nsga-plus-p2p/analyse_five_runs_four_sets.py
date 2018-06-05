
import glob

from five_runs_four_sets_file_manager import ParetoFileManager
from five_runs_four_sets_evaluator import ParetoEvaluator

def process_files(out_lists):

    manager = ParetoFileManager()

    for out_file in out_lists:
        manager.read_file(out_file)

    print("")

    evaluator = ParetoEvaluator()
    evaluator.workflow_pareto_sets = manager.workflow_pareto_sets
    evaluator.evaluate_pareto_sets()

    return evaluator.workflow_pareto_sets





# Main
it = "900"
third = "vm"

# D:\Users\Peerasak\Google Drive KMUTT\PhD Works\Experiments\peer-to-peer-super-agent\result\nsga-plus-commu\300

folder_name = 'D:/Users/Peerasak/Google Drive KMUTT/PhD Works/Experiments/peer-to-peer-super-agent/result' + \
              '/nsga-plus-' + third + '/' + it + '/*.out'

print(folder_name)

out_lists = glob.glob(folder_name)

print("Files in list: " + str(len(out_lists)) + " files")

workflow_pareto_sets = process_files(out_lists)

print("")
print("===Final Result===")
print("Iter: " + it + ", Third: " + third)
for _pareto_set in workflow_pareto_sets:
    _details = _pareto_set[0] + ","

    for _hypervolume in _pareto_set[1].hypervolume_list:
        _details += str(_hypervolume) + ","

    print(_details)


print("")
for _pareto_set in workflow_pareto_sets:
    _details = _pareto_set[0] + ","

    for _on_of_pareto in _pareto_set[1].no_of_pareto:
        _details += str(_on_of_pareto) + ","

    print(_details)
