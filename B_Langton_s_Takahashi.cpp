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
    int h,w,n;cin>>h>>w>>n;
    int x,y;
    x = y = 0;
    vi dx(4) = {-1,0,1,0};
    vi dy(4) = {0,1,0,-1};
    vector<string> res (h,string(w,'.'));
    int d = 0;
    while (n--){
        if (res[x][y]=='.'){
            res[x][y]=='#';
            x += dx[(d+1)%4];
            y += dy[(d+1)%4];
            d = (d+1)%4
        }else{
            res[x][y]=='.';
            x += dx[(4+d-1)%4];
            y += dy[(4+d-1)%4];
            d= (4+d-1)%4;
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
    
    cin >> t;
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