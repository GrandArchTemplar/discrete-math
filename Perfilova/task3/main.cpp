#include <iostream>
#include <vector>
#include <map>
#include <string>

using namespace std;

string reflexive(vector<vector<bool>>& adj_matrix, int n) {
    bool refl = true;
    bool arefl = true;
    for (int i = 0; i < n; i++) {
        refl &= adj_matrix[i][i];
        arefl &= !adj_matrix[i][i];
    }
    if (refl) return "рефлексивно";
    if (arefl) return "антирефлексивно";
    return "нерефлексивно";
}

string symmetric(vector<vector<bool>>& adj_matrix, int n) {
    bool symm = true;
    bool asymm = true;
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            if (adj_matrix[i][j]) {
                symm &= (adj_matrix[i][j] == adj_matrix[j][i]);
                asymm &= (adj_matrix[i][j] != adj_matrix[j][i]);
            }

        }
    }
    if (symm) return "симметрично";
    if (asymm) return "антисимметрично";
    return "несимметрично";
}

string transitive(vector<vector<bool>>& adj_matrix, int n) {
    bool trans = true;
    bool atrans = true;

    for (int i = 0; i < n; i++) {
        for (int j = i + 1; j < n; j++) {
            for (int k = 0; k < n; k++) {
                if (k == i || k == j) continue;
                if (adj_matrix[i][k] && adj_matrix[k][j]) {
                    trans &= adj_matrix[i][j];
                    atrans &= !adj_matrix[i][j];
                }

            }
        }
    }

    if (trans) return "транзитивно";
    if (atrans) return "антитранзитивно";
    return "нетранзитивно";
}

int main() {
    int n, m; cin >> n >> m;

    vector<vector<bool>> adj_matrix(n, vector<bool>(n, false));

    for (int i = 0; i < m; i++) {
        int x, y; cin >> x >> y;
        adj_matrix[x][y] = true;
    }

    cout << reflexive(adj_matrix, n) << endl;
    cout << symmetric(adj_matrix, n) << endl;
    cout << transitive(adj_matrix, n) << endl;
    return 0;
}
