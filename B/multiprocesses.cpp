#include <iostream>
#include <vector>
#include <algorithm>

struct Task {
    int id;
    int length;
    int start;
    int processor;
};

bool compareTasks(const Task& a, const Task& b) {
    return a.length > b.length;
}

bool isFeasible(std::vector<Task>& tasks, int m, int D) {
    std::sort(tasks.begin(), tasks.end(), compareTasks);

    std::vector<int> processors(m, 0);

    for (Task& task : tasks) {
        int earliestStart = D - task.length;
        int bestProcessor = -1;

        for (int i = 0; i < m; ++i) {
            if (processors[i] <= earliestStart && (bestProcessor == -1 || processors[i] < processors[bestProcessor])) {
                bestProcessor = i;
            }
        }

        if (bestProcessor == -1) {
            return false;  // No processor available for this task
        }

        task.start = processors[bestProcessor];
        task.processor = bestProcessor;
        processors[bestProcessor] += task.length;
    }

    return true;
}

int main() {
    std::vector<Task> tasks = {
        {1, 3, 0, -1},
        {2, 2, 0, -1},
        {3, 1, 0, -1}
    };

    int m = 2;  // Number of processors
    int D = 5;  // Overall deadline

    if (isFeasible(tasks, m, D)) {
        std::cout << "Feasible schedule found:\n";
        for (const Task& task : tasks) {
            std::cout << "Task " << task.id << " starts at " << task.start << " on processor " << task.processor << "\n";
        }
    } else {
        std::cout << "No feasible schedule found.\n";
    }

    return 0;
}
