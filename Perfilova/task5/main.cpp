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
        if (result == 1) {
            if (!ans.empty()) ans += " + ";
            for (int k = 0; k < n; k++) {
                if (k > 0) ans += "^";
                if (vars[k] == 0) {
                    ans += "(-" + sym[k] + ")";
                }
                else ans += sym[k];
            }
        }
    }
    cout << ans << endl;
    return 0;
}
