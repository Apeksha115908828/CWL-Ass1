import testcaseGenerator

num_nodes = 10  # Number of nodes in the graph
num_edges = 8   # Number of edges to generate
num_sources = 1 # Number of source nodes
filename = "reach_t1.txt"  # Output file name

testcaseGenerator.generate_testcases(8, 10, 1, "reach_t1.P")
testcaseGenerator.generate_testcases(16, 30, 3, "reach_t2.P")
testcaseGenerator.generate_testcases(8, 14, 5, "reach_t3.P")
testcaseGenerator.generate_testcases(4, 8, 1, "reach_t4.P")