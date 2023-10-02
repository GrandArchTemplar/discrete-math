#include <iostream>
#include <set>
#include <string>
using namespace std;

int main() {
    int n; cin >> n;
    vector<int> a(n);
    for (int i = 0; i < n; i++) cin >> a[i];

    int c = 1 << n;
    for (int mask = 0; mask < c; mask++) {
        vector<int> subs;
        for (int b = 0; b < n; b++) {
            if (((1 << b) & mask) > 0) {
                subs.push_back(a[b]);
            }
        }
        if (subs.size() == 0) {
            cout << "[]" << endl;
        }
        else {
            for (auto el : subs) {
                cout << el << " ";
            }
            cout << endl;
        }
    }
    return 0;
}
