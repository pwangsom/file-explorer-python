
import glob

from pareto_file_manager import ParetoFileManager

outLists = glob.glob(r'''C:\Users\pwang\Desktop\Misc\test1\*.out''')

manager = ParetoFileManager()

for outFile in outLists:
    manager.read_file(outFile)

manager.print_parato_sets()


