edge(6, 15).
edge(4, 3).
edge(5, 4).
edge(3, 10).
edge(14, 10).
edge(11, 5).
edge(10, 9).
edge(11, 8).
edge(1, 3).
edge(15, 11).
edge(6, 11).
edge(6, 14).
edge(14, 6).
edge(12, 15).
edge(3, 15).
edge(9, 10).
edge(10, 8).
edge(13, 7).
edge(15, 4).
edge(15, 7).
edge(12, 5).
edge(3, 2).
edge(4, 7).
edge(3, 5).
edge(3, 11).
edge(3, 14).
edge(8, 7).
edge(8, 10).
edge(10, 13).
edge(15, 12).
source(13).
source(10).
source(6).

reach(X) :- source(X).
reach(X) :- source(Y), edge(Y, X).

#show reach/1.