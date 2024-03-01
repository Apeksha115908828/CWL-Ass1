import subprocess
from datetime import datetime
import testcaseGenerator
import matplotlib.pyplot as plt
import os

def executeAndGetPlotPoints(file_name, testcase, input, plotNumNodes, plotTimeTaken):
    start_time = datetime.now()
    with open('output_'+ file_name + '.txt', 'a') as output_file:
        subprocess.Popen(['/opt/homebrew/bin/clingo', testcase, file_name], stdout=output_file).wait()

    end_time = datetime.now()
    time_diff_milli_seconds = (end_time - start_time).total_seconds() * 1000
    # Add points for number of nodes against time
    plotNumNodes.append(input[0])
    plotTimeTaken.append(time_diff_milli_seconds)

inputForGeneratingTestcases = [[8, 10, 1], [16, 30, 3], [8, 14, 5], [4, 8, 1], [5, 6 ,1], [2, 0, 2]]

def generateGraphTestcases():
    for i in range(1, 5):
        input = inputForGeneratingTestcases[i]
        testcaseGenerator.generate_testcases(input[0], input[1], input[2], "reach_test_" + str(i) + ".lp")

def generate_testcases_nqueens(i):
    with open("nqueens_test.lp", 'w') as file:   
        file.write(f"#const n = {i}.\n")

def generate_testcases_nqueens_plus(n, k):
    with open("nqueens_plus_test.lp", 'w') as file:   
        file.write(f"#const n = {n}.\n #const k = {k}.\n")

# graph reachability
def generateTestcaseAndExecuteGR():
    plt.clf()
    generateGraphTestcases()
    file_name = "graph_reachability.lp"
    plotNumNodes_v1 = []
    plotTimeTaken_v1 = []
    
    for i in range(1, 5):
        input = inputForGeneratingTestcases[i]
        executeAndGetPlotPoints(file_name, "reach_test_" + str(i) + ".lp", input, plotNumNodes_v1, plotTimeTaken_v1)
    plt.plot(plotNumNodes_v1, plotTimeTaken_v1, label = "Graph with clingo")
    plt.xlabel('Num of Nodes in the graph')
    plt.ylabel('Time taken to execute')
    plt.title('Graph Reachability plot of nodes against time')
    plt.legend()
    plt.savefig('graph_reachability_clingo.png')

# NQueens
def generateTestcaseAndExecuteNQueens():
    plt.clf()
    plotNumNodes = []
    plotTimeTaken = []
    for i in range(3, 11):
        generate_testcases_nqueens(i)
        executeAndGetPlotPoints("nqueens.lp", "nqueens_test.lp", [i], plotNumNodes, plotTimeTaken)

    plt.plot(plotNumNodes, plotTimeTaken)
    plt.xlabel('Num of queens')
    plt.ylabel('Time taken to execute')
    plt.title('Nqueens number of queens against time')
    # plt.show()
    plt.savefig('clingo_nqueens.png')

# NQueens Plus
def generateTestcaseAndExecuteNQueensPlus():
    plt.clf()
    plotNumNodes = [[] * 10 for i in range(1, 7)]
    plotTimeTaken = [[] * 10 for i in range(1, 7)]
    for k in range(1, 6):
        for i in range(max(k, 4), 10):
            generate_testcases_nqueens_plus(i, k)
            executeAndGetPlotPoints("nqueens_plus.lp", "nqueens_plus_test.lp", [i], plotNumNodes[k], plotTimeTaken[k])

    for k in range(1, 6):
        plt.plot(plotNumNodes[k], plotTimeTaken[k], label="Graph for n queens plus with k=" + str(k))
    
    plt.xlabel('Num of queens')
    plt.ylabel('Time taken to execute')
    plt.title('Nqueens number of n queens plus against time')
    plt.legend()
    # plt.show()
    plt.savefig('clingo_nqueens_plus.png')

# clear the files
def clear_file(file_path):
    with open(file_path, 'w') as file:
        pass

if __name__ == "__main__":
    file_paths = ['output_nqueens.lp.txt', 'output_nqueens_plus.lp.txt', 'output_graph_reachability.lp.txt']
    for file_path in file_paths:
        clear_file(file_path)
    # generateTestcaseAndExecuteGR()
    # generateTestcaseAndExecuteNQueens()
    # generateTestcaseAndExecuteNQueensPlus()