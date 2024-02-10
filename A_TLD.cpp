#include <bits/stdc++.h>
using namespace std;
#define int long long
#define inf (int)1e18
#define yes "yes"
#define no "no"
#define fog(i, a, b) for (int i = a; i < b; i++)
#define rof(i, a, b) for (int i = a; i > b; i--)
#define all(x) (x).begin(),(x).end()
#define rall(x) (x).rbegin(),(x).rend()
#define fi first
#define se second
#define pb push_back
#define mp make_pair


typedef pair<int, int> pii;
typedef vector<int> vi;
// typedef long long ll;
// typedef vector<ll> vll;
// typedef vector<vll> vvll;
typedef vector<vi> vvi;
map<int,int> mpii;
map<string,int> mpsi;
map<string,string> mpss;


mt19937_64 RNG(chrono::steady_clock::now().time_since_epoch().count());

void Solve() 
{
    string s;
    cin>>s;
    rof(i,s.size()-1,-1){
        if (s[i]=='.'){
            cout<< s.substr(i+1) <<'\n';
            return ;
        }
    }
}

int32_t main() 
{
    auto begin = std::chrono::high_resolution_clock::now();
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    int t = 1;
    //#ifndef ONLINE_JUDGE
    //freopen("in.txt",  "r", stdin);
    //freopen("out.txt", "w", stdout);
    //#endif
    
    // cin >> t;
    fog(i,1,t+1)
    {
        //cout << "Case #" << i << ": ";
        Solve();
    }
    auto end = std::chrono::high_resolution_clock::now();
    auto elapsed = std::chrono::duration_cast<std::chrono::nanoseconds>(end - begin);
    cerr << "Time measured: " << elapsed.count() * 1e-9 << " seconds.\n"; 
    return 0;
}