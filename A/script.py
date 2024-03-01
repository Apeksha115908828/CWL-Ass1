import random
import subprocess
from datetime import datetime
import testcaseGenerator
import matplotlib.pyplot as plt

#load input file to the code file
def addInputToFile(file_path, text):
    with open(file_path, 'w') as file:
        file.write(text)

command = "C:\\Program Files (x86)\\XSB\\config\\x64-pc-windows\\bin\\xsb.exe"

# check if the execCommand Works.
def executeAndGetPlotPoints(file_name, testcase, input, execCommand, plotNumNodes, plotTimeTaken):
    start_time = datetime.now()
    with open('output_' + file_name + '.txt', 'a') as output_file:
        if 'suffix' in file_name or 'queens' in file_name:
            cmd = file_name + ' ' + execCommand
        else :
            # with open('output_' + file_name + '.txt', 'a') as output_file:
            cmd = testcase + ' ' + file_name + ' ' + execCommand
        process = subprocess.Popen(command, shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE,
                                   stderr=subprocess.PIPE)
        stdout, stderr = process.communicate(input=cmd.encode())
    end_time = datetime.now()
    time_diff_milli_seconds = (end_time - start_time).total_seconds() * 1000
    # Add points for number of nodes against time
    plotNumNodes.append(input[0])
    plotTimeTaken.append(time_diff_milli_seconds)


inputForGeneratingTestcases = [[8, 10, 1], [16, 30, 3], [8, 14, 5], [4, 8, 1], [5, 6 ,1], [2, 0, 2]]

def generateGraphTestcases():
    for i in range(1, 5):
        input = inputForGeneratingTestcases[i]
        testcaseGenerator.generate_testcases(input[0], input[1], input[2], "reach_test_" + str(i) + ".P")

# graph reachability
def generateTestcaseAndExecuteGR():
    plt.clf()
    GR_with_table = "reach.P"
    GR_without_table = "graph_reachability.P"
    plotNumNodes_v1 = []
    plotTimeTaken_v1 = []
    plotNumNodes_v2 = []
    plotTimeTaken_v2 = []
    generateGraphTestcases()
    for i in range(1, 5):
        input = inputForGeneratingTestcases[i]
        # addInputToFile(GR_without_table, "input :- [reach_test_" + i + "].")
        # addInputToFile(GR_with_table, "input :- [reach_test_" + i + "].")
        executeAndGetPlotPoints(GR_with_table, "reach_test_" + str(i) + ".P", input, "reach(X).", plotNumNodes_v1, plotTimeTaken_v1)
        executeAndGetPlotPoints(GR_without_table, "reach_test_" + str(i) + ".P", input, "reach(X).", plotNumNodes_v2, plotTimeTaken_v2)

    plotNumNodes_v1, plotTimeTaken_v1 = zip(*sorted(zip(plotNumNodes_v1, plotTimeTaken_v1)))
    plotNumNodes_v2, plotTimeTaken_v2 = zip(*sorted(zip(plotNumNodes_v2, plotTimeTaken_v2)))
    plt.plot(plotNumNodes_v1, plotTimeTaken_v1, label = "GR_with_table")
    plt.plot(plotNumNodes_v2, plotTimeTaken_v2, label = "GR_without_table")
    plt.xlabel('Num of Nodes in the graph')
    plt.ylabel('Time taken to execute')
    plt.title('Graph Reachability plot of nodes against time')
    plt.legend()
    # plt.show()
    plt.savefig('graph_reachability.png')

# NQueens
def generateTestcaseAndExecuteNQueens():
    plt.clf()
    plotNumNodes_1sol = []
    plotTimeTaken_1sol = []
    plotNumNodes_allsol = []
    plotTimeTaken_allsol = []
    for i in range(1, 10):
        executeAndGetPlotPoints("nqueens_1solution.P", " ", [i], "queens(" + str(i) + ", Qs)", plotNumNodes_1sol, plotTimeTaken_1sol)
        executeAndGetPlotPoints("nqueens.P", " ", [i], "queens(" + str(i) + ", Qs)", plotNumNodes_allsol, plotTimeTaken_allsol)

    plt.plot(plotNumNodes_1sol, plotTimeTaken_1sol, label="1 solution")
    plt.plot(plotNumNodes_allsol, plotTimeTaken_allsol, label="all solution")
    plt.xlabel('Num of queens')
    plt.ylabel('Time taken to execute')
    plt.title('Nqueens number of queens against time')
    plt.legend()
    # plt.show()
    plt.savefig('nqueens.png')

#NQueensPlus
def generateTestcaseAndExecuteNQueensPlus():
    plt.clf()
    # plotNumNodes = [[]]
    plotNumNodes = [[0] * 10 for i in range(5)]
    plotTimeTaken = [[0] * 10 for i in range(5)]
    # plotTimeTaken = [[]]
    for k in range(1, 5):
        for i in range(1, 10): # for number of queens
            executeAndGetPlotPoints("nqueens_plus.P", "", [i], "queens(" + str(i) + ", Qs," + str(k) + ").", plotNumNodes[k], plotTimeTaken[k])

    for k in range(1, 5):
        plt.plot(plotNumNodes[k], plotTimeTaken[k], label="Graph for n queens plus with k=" + str(k))
    plt.xlabel('Num of queens')
    plt.ylabel('Time taken to execute')
    plt.title('Nqueens number of queens against time')
    plt.legend()
    # plt.show()
    plt.savefig('nqueensplus.png')

#SuffixAndCut
def generateTestcaseAndExecuteSuffixAndCut():
    plt.clf()
    plotNumNodes = []
    plotTimeTaken = []
    plotNumNodes1 = []
    plotTimeTaken1 = []
    for i in range(1, 10):
        flag = random.randint(0, 1)  # to decide whether to generate a passing testcase or failing
        n = random.randint(5, 15)
        k = random.randint(1, 5)
        list1 = [random.randint(1, 100) for _ in range(n)]
        list2 = list1 + [random.randint(1, 100) for _ in range(k)] if flag else [random.randint(1, 100) for _ in range(n + k)]
        executeAndGetPlotPoints("suffix.P", "", [len(list2)], "suffix([" + str(list1) + "],[" + str(list2) + "]).", plotNumNodes, plotTimeTaken)
        executeAndGetPlotPoints("suffix.P", "", [len(list1)], "cut([" + str(list1) + "]).", plotNumNodes1,
                                plotTimeTaken1)
    plotNumNodes, plotTimeTaken = zip(*sorted(zip(plotNumNodes, plotTimeTaken)))
    plt.plot(plotNumNodes, plotTimeTaken, label="Graph for suffix/2")
    # plotNumNodes1 = []
    # plotTimeTaken1 = []
    # for i in range(1, 10):
    #     flag = random.randint(0, 1)  # to decide whether to generate a passing testcase or failing
    #     n = random.randint(5, 15)
    #     list1 = [random.randint(1, 100) for _ in range(n)]
    #     executeAndGetPlotPoints("suffix.P", "", [len(list1)], "cut([" + str(list1) + "]).", plotNumNodes1,
    #     plotTimeTaken1)
    plotNumNodes1, plotTimeTaken1 = zip(*sorted(zip(plotNumNodes1, plotTimeTaken1)))
    plt.plot(plotNumNodes1, plotTimeTaken1, label="Graph for cut/1")
    plt.xlabel('Num of points')
    plt.ylabel('Time taken to execute')
    plt.title('Suffix/2 Cut/1, number of points against time')
    plt.legend()
    # plt.show()
    plt.savefig('suffix_cut.png')

#Transitive closure
def generateTestcaseAndExecuteTransitiveClosure():
    plt.clf()
    version_1 = "path&cycle_1.P"
    version_2 = "path&cycle_2.P"
    plotNumNodes_v1 = []
    plotTimeTaken_v1 = []
    plotNumNodes_v2 = []
    plotTimeTaken_v2 = []
    
    for i in range(1, 5):
        input = inputForGeneratingTestcases[i]
        # addInputToFile(version_1, "input :- [reach_test_" + i + "].")
        # addInputToFile(version_2, "input :- [reach_test_" + i + "].")
        executeAndGetPlotPoints(version_1, "reach_test_" + str(i) + ".P", input, "cycle(X).", plotNumNodes_v1, plotTimeTaken_v1)
        executeAndGetPlotPoints(version_2, "reach_test_" + str(i) + ".P", input, "cycle(X).", plotNumNodes_v2, plotTimeTaken_v2)
    plotNumNodes_v1, plotTimeTaken_v1 = zip(*sorted(zip(plotNumNodes_v1, plotTimeTaken_v1)))
    plotNumNodes_v2, plotTimeTaken_v2 = zip(*sorted(zip(plotNumNodes_v2, plotTimeTaken_v2)))
    plt.plot(plotNumNodes_v1, plotTimeTaken_v1, label = "Cycle in version 1")
    plt.plot(plotNumNodes_v2, plotTimeTaken_v2, label = "Cycle in version 2")
    plt.xlabel('Num of Nodes in the graph')
    plt.ylabel('Time taken to execute')
    plt.title('Transitive closure plot of nodes against time')
    plt.legend()
    # plt.show()
    plt.savefig('transitiveClosure.png')

def clear_file(file_path):
    with open(file_path, 'w') as file:
        pass  # Truncate the file

if __name__ == "__main__":
    file_paths = ['output_graph_reachability.P.txt', 'output_nqueens.P.txt', 'output_nqueens_plus.P.txt', 'output_suffix.P.txt', 'output_path&cycle_1.P.txt', 'output_path&cycle_2.P.txt']
    for file_path in file_paths:
        clear_file(file_path)

    # generateTestcaseAndExecuteGR()
    # generateTestcaseAndExecuteNQueens()
    # generateTestcaseAndExecuteNQueensPlus()
    # generateTestcaseAndExecuteSuffixAndCut()
    # generateTestcaseAndExecuteTransitiveClosure()