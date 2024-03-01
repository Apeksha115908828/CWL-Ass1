# CWL-Ass1

A.
The code for generating the testcases and running the code is present in A/script.py file.
The file testcaseGenerator.py has implementation to generate testcases with edges and source nodes for graph reachability.
Below are the functions to execute for generating the testcases and running the code for the questions present in section A, one should uncomment the function they want to execute
generateTestcaseAndExecuteGR()
generateTestcaseAndExecuteNQueens()
generateTestcaseAndExecuteNQueensPlus()
generateTestcaseAndExecuteSuffixAndCut()
generateTestcaseAndExecuteTransitiveClosure()

The testcases for reachability and transitive_closure are present in reach_test_x.P, n queens/nqueens plus cases are added while execution as they are veru short.

For this section to execute one must have XSB installed at location: C:\\Program Files (x86)\\XSB\\config\\x64-pc-windows\\bin\\xsb.exe
or update the variable command in script.py

1.
The file suffix.P and cut.P contains the code for generating the suffic and printing the output for cut/2 using the append predicate that is present in the append.P file.
To run suffix/2, compile the file using following command and execute with a query e.g. suffix([1, 2, 3], [1, 2, 3, 4, 5, 6]) will return [4, 5, 6].
To run cut/1, compile the file using the following command and execute with a query([1, 2, 3]) and the output should contain all the solutions for the cut.
To Execute: 
1. In script.py, uncomment line generateTestcaseAndExecuteSuffixAndCut() and
2. execute python script.py
3. the output can be found in output_suffix.P.txt
4. the graph for number of nodes against time taken to execute can be found in file suffix.png


2.
The file graph_reachability.P and reach.P contains the code for printing all the vertices that are reachable from the source. The testcase generation code is present in generateTestcases.py and testcaseGenerator.py files.
These will generate random testcases for different value of number of nodes, number of edges and number of sources defined in generateTestcases.py file, some special testcases are present in reach_t5 for cycle, reach_t6 for empty where no connection from source to any nodes, and reach_t7 for disconnected graphs.
To generate random testcases from reach_t1 to reach_t4,
Step1: Run below command on terminal, make sure to have python3 installed on the system(python 2.x would also work, I have tested in python3 environment).
$ python3 generateTestcases.py
The file graph_reachability.P takes in input from the testcase file reach_tx.P, and the time of execution is calculated from after loading the input till the time when all the nodes are reached.
graph_reachability.P: Implementation without using tabling
reach.P: Implementatin using tabling
To Execute: 
1. In script.py, uncomment line generateTestcaseAndExecuteGR() and
2. execute python script.py
3. the output can be found in output_graph_reachability.P.txt
4. the graph for number of nodes against time taken to execute can be found in file graph_reachability.png

There are some special testcases to verify for graphs with cycle and disconnected graphs in reach_t5.P, reach_t6.P, reach_t7.P files to verify correctness.

3.
Transitive closure and cycle detection
The file path&cycle_1.P and path&cycle_2.P contain 2 versions of the checking for path. The file path&cycle_1.P has predicate path/2 'edge(X, Z), path(Z, Y)' which executes edge/2 first and then path/2 and path&cycle_2.P has predicate path/2 'path(Z, Y), edge(X, Z).' which executes path/2 first and then edge/2. Although both the codes are similar except for the order, the timing difference noticed is substantial as can be observed in file transitiveClosure.png.
I tried one more version rearranging the predicates but that was yielding incorrect output

To Execute: 
1. In script.py, uncomment line generateTestcaseAndExecuteTransitiveClosure() and
2. execute python script.py
3. the output can be found in output_path&cycle_1.P.txt and output_path&cycle_2.P.txt
4. the graph for number of nodes against time taken to execute can be found in file transitiveClosure.png

4.
The file nqueens.P has implementation for nqueens problem in prolog for all solutions and nqueens_1solution.P for only 1 solution and then terminate.

To Execute: 
1. In script.py, uncomment line generateTestcaseAndExecuteNQueens() and
2. execute python script.py
3. the output can be found in output_nqueens.P.txt
4. the graph for number of nodes against time taken to execute can be found in file nqueens.png

Reference: The Art of Prolog

The code for nqueens plus is implemented in nqueens_plus.P and run testcases for analysis as similar to nqueens.
To Execute: 
1. In script.py, uncomment line generateTestcaseAndExecuteNQueensPlus() and
2. execute python script.py
3. the output can be found in output_nqueens_plus.P.txt
4. the graph for number of nodes against time taken to execute can be found in file nqueens_plus.png


B.
The code for generating the testcases and running the code is present in B/script.py file.
The file testcaseGenerator.py has implementation to generate testcases with edges and source nodes for graph reachability.
Below are the functions to execute for generating the testcases and running the code for the questions present in section B, one should uncomment the function they want to execute
generateTestcaseAndExecuteGR()
generateTestcaseAndExecuteNQueens()
generateTestcaseAndExecuteNQueensPlus()

1.
The code for graph reachability in clingo can be found in graph_reachability.lp file.
To Execute: 
1. In script.py, uncomment line generateTestcaseAndExecuteGR() and
2. execute python script.py
3. the output can be found in output_graph_reachability.lp.txt
4. the graph for number of nodes against time taken to execute can be found in file graph_reachability_clingo.png

2. The code for nqueens in clingo can be found in nqueens.lp file
To Execute: 
1. In script.py, uncomment line generateTestcaseAndExecuteNQueens() and
2. execute python script.py
3. the output can be found in output_nqueens.lp.txt
4. the graph for number of nodes against time taken to execute can be found in file clingo_nqueens.png

3. The code for nqueens plus in clingo can be found in nqueens_plus.lp file.
To Execute:
1. In script.py, uncomment line generateTestcaseAndExecuteNQueensPlus() and
2. execute python script.py
3. the output can be found in output_nqueens_plus.lp.txt
4. the graph for number of nodes against time taken to execute can be found in file clingo_nqueens_plus.png

C.
The code for n-queens-plus can be found in n_queens_plus.idp. This implementation is based on the one that was shared with the assignment, I have added an additional variable k and the condition to check for distance between no 2 queens to be less than k.

This code has been verified on the online tool http://idp.cs.kuleuven.be/idp. I have tested this code for various different values of k, the maximum value where I could still generate the valid solutions was 5 for 20 queens problem.