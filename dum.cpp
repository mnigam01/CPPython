#include <bits/stdc++.h>


using namespace std;

class FenwickTreeRAQ {
private:
    vector<long long> bit0, bit1;
    int n;

    void add(vector<long long>& bit, int k, long long x) {
        k++;
        while (k <= n) {
            bit[k] += x;
            k += k & -k;
        }
    }

    long long pref(vector<long long>& bit, int r) {
        long long ret = 0;
        while (r > 0) {
            ret += bit[r];
            r -= r & -r;
        }
        return ret;
    }

public:
    FenwickTreeRAQ(vector<int>& a) {
        n = a.size();
        bit0.assign(n + 2, 0);
        bit1.assign(n + 2, 0);
        for (int i = 0; i < n; i++) {
            add(bit0, i, -a[i] * i);
            add(bit0, i + 1, a[i] * (i + 1));
            add(bit1, i, a[i]);
            add(bit1, i + 1, -a[i]);
        }
    }

    void add(int k, long long x) {
        assert(0 <= k && k < n);
        add_range(k, k + 1, x);
    }

    void add_range(int l, int r, long long x) {
    assert(0 <= l && l <= r && r <= n);
    add(bit0, l, -x * l);
    add(bit0, r, x * r);
    add(bit1, l, x);
    add(bit1, r, -x);
}

    long long sum(int l, int r) {
        assert(0 <= l && l <= r && r <= n);
        return pref(bit0, r) + r * pref(bit1, r) - pref(bit0, l) - l * pref(bit1, l);
    }

    vector<long long> tolist() {
        vector<long long> res(n);
        for (int i = 0; i < n; i++) {
            res[i] = sum(i, i + 1);
        }
        return res;
    }

    long long operator[](int k) {
        assert(0 <= k && k < n);
        return sum(k, k + 1);
    }
};

void solve() {
    int n, q;
    cin >> n >> q;
    vector<int> a(n);
    for (int i = 0; i < n; i++) {
        cin >> a[i];
    }
    FenwickTreeRAQ fw(a);
    for (int i = 0; i < q; i++) {
        int op;
        cin >> op;
        if (op == 1) {
            int l, r, x;
            cin >> l >> r >> x;
            fw.add_range(l - 1, r, x);
        } else {
            int k;
            cin >> k;
            cout << fw[k - 1] << endl;
        }
    }
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
    solve();
    return 0;
}
