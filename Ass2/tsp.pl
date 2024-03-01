% % % Define the number of cities
% % #const n=4.

% % % Define the cities
% % city(1).
% % city(2).
% % city(3).
% % city(4).

% % % Define the distance between cities (example distances)
% % distance(1, 2, 10).
% % distance(1, 3, 15).
% % distance(1, 4, 20).
% % distance(2, 3, 35).
% % distance(2, 4, 25).
% % distance(3, 4, 30).
% % distance(4, 1, 20).

% % path(1, 2).
% % path(1, 3).
% % path(1, 4).
% % path(2, 3).
% % path(2, 4).
% % path(3, 4).
% % path(4, 1).

% % % Define a path from one city to another
% % % 1 {path(X, Y); path(Y, X)} 1 :- city(X), city(Y), X < Y.

% % path(X, Y) :- city(X), city(Y), distance(X, Y, _).
% % path(X, Y) :- path(X, Z), path(Z, Y).

% % % Define the total distance of the path
% % total_distance(D) :- D = #sum {D1 : distance(X, Y, D1), path(X, Y)}.

% % % Constraints to ensure the path is a Hamiltonian cycle
% % :- not {path(X, Y) : city(Y)} = 1, city(X).
% % :- not {path(X, Y) : city(X)} = 2, city(Y).

% % % Objective: minimize the total distance
% % % #minimize {D : total_distance(D)}.

% % % Find the optimal path
% % #show path/2.

% % THE TRAVELING SALESPERSON WITHOUT TIME WINDOWS

% % visited (city)
% % travel (from_city, to_city)
% % path (from_city, to_city, travel_cost)

% % Start and end must be in the same city
% :- not location(Place, t, _), location(Place, 0, _).

% % Paths are symmetrical
% path(A, B, COST) :- path(B, A, COST).

% % In each step, there can be only one travel from one city to another
% { travel(Place, T) : place(Place, _, _) } 1 :- T = 0..t-1.

% % If there was a travel to a city, that city has been visited
% visited(Place) :- travel(Place, _).

% % We cannot visit a city we've been to before
% :- travel(Place, T1), visited(Place, T2), T1 > T2.

% % We cannot go to a city where there is no path
% :- travel(To, _), location(From, _, _), not path(From, To, _).

% % Calculate total travel cost
% total_cost(C) :- path(From, To, COST), visited(From), visited(To), C = #sum { COST : path(From, To, COST) }.

% % Find minimal total travel cost
% #minimize { C : total_cost(C) }.
% #show visited/1.

% #const t = 5.

% % Starting point (city_0)
% location(city_0, 0, 0).

% % Define your cities and distances
% % Example:
% path(city_0, city_1, 10).  % Distance from city 0 to city 1 is 10 units
% path(city_1, city_2, 15).  % Distance from city 1 to city 2 is 15 units
% path(city_2, city_3, 15).
% path(city_3, city_4, 15).
% path(city_4, city_5, 15).
% path(city_5, city_1, 15).

% Facts
city(1..5). % Assuming there are 5 cities
start_city(1).
dist(1, 2, 10). % Distance from city 1 to city 2 is 10
dist(1, 3, 15).
dist(1, 4, 20).
% dist(1, 5, 25).
dist(2, 3, 35).
dist(2, 4, 40).
dist(2, 5, 45).
dist(3, 4, 30).
dist(3, 5, 35).
dist(4, 5, 10).
dist(5, 1, 7).

% Variables
tour(X, Y) :- dist(X, Y, _).
{ visit(C) : city(C) } = 1..5. % Visiting each city exactly once

% Constraints
:- start_city(Start), not visit(Start).

% :- not start_city(Start), not visit(Start).

% :- not start_city(Start), not visit(Start). % Start from the start city
1 { tour(X, Y) : dist(X, Y, _) } 1 :- city(X), visit(Y). % Each city is visited once
:- visit(X), visit(Y), X != Y, not tour(X, Y), not tour(Y, X). % Connectivity constraint

% Objective
#minimize { D : dist(X, Y, D), tour(X, Y) }.
