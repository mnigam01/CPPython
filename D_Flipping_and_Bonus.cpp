#include <bits/stdc++.h>

#define int long long
#define ll long long


using namespace std;

int32_t main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m;
    cin >> n >> m;

    vector<int> a(n + 1);
    for (int i = 0; i <n; ++i) {
        cin >> a[i];
    }

    unordered_map<int, int> d;
    for (int i = 0; i < m; ++i) {
        int c, y;
        cin >> c >> y;
        d[c] = y;
    }
    vector<int> dp(5002, 0);
    for (int i = n - 1; i >= 0; --i) {
        vector<int> prv(5002, 0);
        for (int s = 0; s <= n; ++s) {
            int x = a[i] + (d.count(s + 1) ? d[s + 1] : 0) + dp[s + 1];
            int y = dp[0];
            prv[s] = max(x, y);
        }
        dp = prv;
    }



    int ans = dp[0];
    cout << ans << '\n';
    // for (auto i:memo){
    //     cout<< i.first.first<<" "<<i.first.second <<'\n';
    //     cout<< i.second <<'\n';
    // }
    

    return 0;
}
