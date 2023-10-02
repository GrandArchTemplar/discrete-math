#include <iostream>
#include <queue>
#include <map>

using namespace std;

struct node {
    char data; int freq; bool leaf;
    node* left; node* right;
    node(char c, int f) : data(c), freq(f), leaf(true), left(NULL), right(NULL) {}
    node(int f, node* left, node* right) : data(NULL), freq(f), leaf(false), left(left), right(right) {}
};


struct cmp {
    bool operator()(node* a, node* b)
    {
        return a->freq > b->freq;
    }
};

node* generate(priority_queue<node*, vector<node*>, cmp> pq)
{
    while (pq.size() != 1) {
        node* left = pq.top(); pq.pop();
        node* right = pq.top(); pq.pop();
        node* n = new node(left->freq + right->freq, left, right);
        pq.push(n);
    }
    return pq.top();
}

void print(node* root, vector<int> &code)
{
    if (root->left) {
        code.push_back(0);
        print(root->left, code);
        code.pop_back();
    }

    if (root->right) {
        code.push_back(1);
        print(root->right, code);
        code.pop_back();
    }

    if (!root->left && !root->right) {
        cout << root->data << " ";
        for (auto c : code) {
            cout << c;
        }
        cout << endl;
    }
}

int main()
{
    string s; cin >> s;
    map<char, int> fr;

    priority_queue<node*, vector<node*>, cmp> pq;

    for (auto c : s) {
        if (fr.count(c) == 0) fr[c] = 0;
        fr[c]++;
    }

    for (auto kvp : fr) {
        pq.push(new node(kvp.first, kvp.second));
    }

    node* root = generate(pq);

    vector<int> code;
    print(root, code);
    return 0;
}
