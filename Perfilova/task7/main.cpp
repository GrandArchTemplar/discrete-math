#include <iostream>
#include <vector>
#include <queue>

using namespace std;


int dfs(vector<vector<int>> &graph, vector<bool> &visited, int v, int dest) {
    if (v == dest) return 0;
    visited[v] = true;
    int mn = INT_MAX - 1;
    for (auto u : graph[v]) {
        if (!visited[u]) {
            mn = min(mn, dfs(graph, visited, u, dest) + 1);
        }
    }
    visited[v] = false;
    return mn;
}

int main() {
    int n, m, k; cin >> n >> m >> k; k--;
    int aux_vert = n;

    vector<vector<int>> graph(n * 2);


    for (int i = 0; i < m; i++) {
        int f, t, w; cin >> f >> t >> w;
        f--; t--;
        if (w == 1) {
            graph[f].push_back(t);
        }
        if (w == 2) {
            // искуственная вершина посередине ребра
            graph[f].push_back(aux_vert);
            graph[aux_vert].push_back(t);
            aux_vert++;
        }
    }

    for (int i = 0; i < n; i++) {
        vector<bool> visited(n * 2, false);
        int res = dfs(graph, visited, k, i);
        if (res >= INT_MAX - 1) {
            cout << "-" << " ";
        }
        else cout << res << " ";
    }

    return 0;
}
