#include <iostream>
#include <set>
#include <string>

using namespace std;

int main() {
    int n, m; cin >> n >> m;
    set<int> a, b;
    for (int i = 0; i < n; i++) {
        int x; cin >> x; a.insert(x);
    }
    for (int i = 0; i < m; i++) {
        int x; cin >> x; b.insert(x);
    }
    char op; cin >> op;
    set<int> result;
    switch (op) {
        case 'u':
            set_union(a.begin(), a.end(), b.begin(), b.end(), std::inserter(result, result.begin()));
            break;
        case 'i':
            set_intersection(a.begin(), a.end(), b.begin(), b.end(), std::inserter(result, result.begin()));
            break;
        case 's':
            set_difference(a.begin(), a.end(), b.begin(), b.end(), std::inserter(result, result.begin()));
            break;
        case 'a':
            set_difference(b.begin(), b.end(), a.begin(), a.end(), std::inserter(result, result.begin()));
            break;
        default:
            cout << "Неизвестна операция" << endl;
            break;
    }
    for (auto r : result) {
        cout << r << " ";
    }
    cout << endl;
    return 0;
}
