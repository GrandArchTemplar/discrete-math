#include <iostream>

using namespace std;

int main() {
    int n; cin >> n;
    string sym[] = {"a", "b", "c", "d", "e"};
    string ans;
    for (int i = 0; i < (1 << n); i++) {
        vector<int> vars(n);
        for (int j = 0; j < n; j++) {
            cin >> vars[j];
        }
        int result; cin >> result;
        if (result == 0) {
            ans += "(";
            for (int k = 0; k < n; k++) {
                if (k > 0) ans += " + ";
                if (vars[k] == 1) {
                    ans += "-";
                }
                ans += sym[k];
            }
            ans += ")";
        }
    }
    cout << ans << endl;
    return 0;
}
