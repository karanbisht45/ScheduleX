#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>
using namespace std;

struct Process {
    int id, arrival, burst, priority, completion, waiting, turnaround;
};

bool compareArrival(Process p1, Process p2) {
    return p1.arrival < p2.arrival;
}

// First Come First Serve (FCFS)
void fcfs(vector<Process>& processes) {
    int currentTime = 0;
    for (auto& p : processes) {
        if (currentTime < p.arrival)
            currentTime = p.arrival;
        p.completion = currentTime + p.burst;
        p.turnaround = p.completion - p.arrival;
        p.waiting = p.turnaround - p.burst;
        currentTime = p.completion;
        cout << p.id << " " << (currentTime - p.burst) << " " << currentTime << endl;
    }
}

// Shortest Job First (Non-Preemptive)
void sjf(vector<Process>& processes) {
    int n = processes.size(), completed = 0, currentTime = 0;
    vector<bool> done(n, false);
    while (completed < n) {
        int idx = -1, minBurst = 1e9;
        for (int i = 0; i < n; i++) {
            if (!done[i] && processes[i].arrival <= currentTime && processes[i].burst < minBurst) {
                minBurst = processes[i].burst;
                idx = i;
            }
        }
        if (idx == -1)
            currentTime++;
        else {
            cout << processes[idx].id << " " << currentTime << " " << (currentTime + processes[idx].burst) << endl;
            currentTime += processes[idx].burst;
            processes[idx].completion = currentTime;
            processes[idx].turnaround = processes[idx].completion - processes[idx].arrival;
            processes[idx].waiting = processes[idx].turnaround - processes[idx].burst;
            done[idx] = true;
            completed++;
        }
    }
}

// Round Robin
void roundRobin(vector<Process>& processes, int quantum) {
    int n = processes.size(), currentTime = 0;
    queue<int> q;
    vector<int> remaining(n);
    for (int i = 0; i < n; i++) remaining[i] = processes[i].burst;
    
    for (int i = 0; i < n; i++) q.push(i);

    while (!q.empty()) {
        int i = q.front();
        q.pop();

        if (remaining[i] > quantum) {
            cout << processes[i].id << " " << currentTime << " " << (currentTime + quantum) << endl;
            currentTime += quantum;
            remaining[i] -= quantum;
            q.push(i);
        } else {
            cout << processes[i].id << " " << currentTime << " " << (currentTime + remaining[i]) << endl;
            currentTime += remaining[i];
            remaining[i] = 0;
        }
    }
}

// Priority Scheduling (Non-Preemptive)
void priorityScheduling(vector<Process>& processes) {
    int n = processes.size(), completed = 0, currentTime = 0;
    vector<bool> done(n, false);
    while (completed < n) {
        int idx = -1, highestPriority = 1e9;
        for (int i = 0; i < n; i++) {
            if (!done[i] && processes[i].arrival <= currentTime && processes[i].priority < highestPriority) {
                highestPriority = processes[i].priority;
                idx = i;
            }
        }
        if (idx == -1)
            currentTime++;
        else {
            cout << processes[idx].id << " " << currentTime << " " << (currentTime + processes[idx].burst) << endl;
            currentTime += processes[idx].burst;
            processes[idx].completion = currentTime;
            done[idx] = true;
            completed++;
        }
    }
}

int main() {
    int n, choice, quantum;
    cin >> n;
    vector<Process> processes(n);
    
    for (int i = 0; i < n; i++) {
        processes[i].id = i + 1;
        cin >> processes[i].arrival >> processes[i].burst >> processes[i].priority;
    }
    
    cin >> choice;
    if (choice == 3) cin >> quantum;

    sort(processes.begin(), processes.end(), compareArrival);

    if (choice == 1) fcfs(processes);
    else if (choice == 2) sjf(processes);
    else if (choice == 3) roundRobin(processes, quantum);
    else if (choice == 4) priorityScheduling(processes);

    return 0;
}
