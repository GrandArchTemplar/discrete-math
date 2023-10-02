#include <iostream>
#include <vector>
#include <queue>

using namespace std;


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

    queue<int> q;
    vector<bool> used(n * 2);
    vector<int> d(n * 2, INT_MAX);

    q.push(k);
    used[k] = true;
    d[k] = 0;
    while (!q.empty()) {
        int v = q.front();
        q.pop();
        for (int u : graph[v]) {
            if (!used[u]) {
                used[u] = true;
                q.push(u);
                d[u] = d[v] + 1;
            }
        }
    }

    for (int i = 0; i < n; i++) {
        if (d[i] == INT_MAX) {
            cout << "-" << " ";
        }
        else cout << d[i] << " ";
    }
    cout << endl;

    return 0;
}
