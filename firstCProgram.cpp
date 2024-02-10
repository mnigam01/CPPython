#include <bits/stdc++.h>
using namespace std;

#define mod (int)(1e9) + 7
#define inf max()
#define yes "yes"
#define no "no"
#define maxi max()
#define mini min()

typedef long long ll;
typedef pair<int, int> pii;
typedef vector<int> vi;
typedef vector<ll> vll;
typedef vector<vi> vvi;
typedef vector<vll> vvll;

#define for(i, a, b) for (int i = a; i < b; i++)
#define fast_io ios_base::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);

int ceil_div(int x, int y) { return (x + y - 1) / y; }

class DSU {
public:
    vector<int> rank, parent;

    DSU(int n) {
        rank.resize(n + 1);
        parent.resize(n + 1);
        for (int i = 0; i <= n; i++)
            parent[i] = i;
    }

    int find(int x) {
        if (parent[x] == x)
            return x;
        return parent[x] = find(parent[x]);
    }

    int union_(int a, int b) {
        int x = find(a);
        int y = find(b);

        if (x == y)
            return 1;

        if (rank[x] < rank[y])
            parent[x] = y;
        else if (rank[x] > rank[y])
            parent[y] = x;
        else {
            parent[y] = x;
            rank[x]++;
        }

        return 0;
    }
};

vector<int> lst() {
    string line;
    getline(cin, line);
    stringstream ss(line);
    vector<int> result;
    int num;
    while (ss >> num)
        result.push_back(num);
    return result;
}

int integer() {
    int num;
    cin >> num;
    cin.ignore(); // Consume the newline character
    return num;
}

string st() {
    string line;
    getline(cin, line);
    return line;
}

vector<vector<int>> matrixNum(int m) {
    vector<vector<int>> matrix;
    for (int i = 0; i < m; i++) {
        vector<int> row = lst();
        matrix.push_back(row);
    }
    return matrix;
}

vector<string> matrixStr(int m) {
    vector<string> matrix;
    for (int i = 0; i < m; i++) {
        string row = st();
        matrix.push_back(row);
    }
    return matrix;
}

vector<string> ans;

template<typename T>
void gh(T out, char s = ' ') {
    stringstream ss;
    if (typeid(out) == typeid(int)) {
        ss << out;
    } else if (typeid(out) == typeid(string)) {
        ss << out;
    } else {
        for (int i = 0; i < out.size(); i++) {
            if (i > 0)
                ss << s;
            ss << out[i];
        }
    }
    ans.push_back(ss.str());
}
    
int m = 1e1;
vector<int> _prime(m,0);
set<int> s;

void sieve() {
    
    for (int i = 0; i < _prime.size(); ++i)
        _prime[i] = i;
    
    _prime[0] = _prime[1] = -1;
    for (int i = 2; i <= static_cast<int>(sqrt(_prime.size())); ++i) {
        if (_prime[i] == i) {
            for (int j = i * i; j < _prime.size(); j += i) {
                _prime[j] = i;
            }
        }
    }

    for (int i = 0; i < _prime.size(); ++i) {
        if (_prime[i] == i) {
            s.insert(i);
        }
    }
}

unordered_map<int, int> dijkstra(int src, unordered_map<int, vector<pair<int, int>>>& d) {
    priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> pq;
    unordered_map<int, int> p;
    unordered_set<int> vis;

    pq.push({0, src});
    p[src] = 0;

    while (!pq.empty()) {
        auto [dist, node] = pq.top();
        pq.pop();

        if (vis.find(node) != vis.end())
            continue;

        vis.insert(node);

        for (auto [j, weight] : d[node]) {
            if (p[node] + weight < p[j]) {
                p[j] = p[node] + weight;
                pq.push({p[j], j});
            }
        }
    }

    return p;
}

vector<vector<int>> directions1 = {{0,1},{1,0},{0,-1},{-1,0},{1,-1},{-1,1},{1,1},{-1,-1}};

// List of directions as vectors (alternative)
vector<vector<int>> directions2 = {{-1,-1},{-1,1},{1,1},{1,-1}};

// List of directions as key-value pairs
unordered_map<char, vector<int>> directions3 = {
    {'U', {0,1}},
    {'R', {1,0}},
    {'D', {0,-1}},
    {'L', {-1,0}}
};

void solve()
{
	gh('Hello World');
}

int main()
{
	fast_io;
	#ifndef ONLINE_JUDGE
    freopen("input.txt","r",stdin);     
    freopen("output.txt","w",stdout);
    #endif
	
	sieve();
	
    int t=1;
    // cin >> t;
    while (t--) {
        solve();
    }
	

	return 0;
}
