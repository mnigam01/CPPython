#include <bits/stdc++.h>
using namespace std;

#define ascii_lowercase "abcdefghijklmnopqrstuvwxyz"
#define ascii_uppercase "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
#define int long long
#define ll long long
#define inf (int)1e18
#define yes "yes"
#define no "no"
#define mod 1000000007
#define endl '\n'


#define fo(i, a, b) for (int i = a; i < b; ++i)
#define ro(i, a, b) for (int i = a; i >b; --i)

// #define fo(i, a, b, ...) for (int i = a; i < b; i+=(__VA_ARGS__ == NULL ? 1 : __VA_ARGS__))
// #define ro(i, a, b, ...) for (int i = a; i > b; i-=(__VA_ARGS__ == NULL ? 1 : __VA_ARGS__))

#define all(x) (x).begin(),(x).end()
#define rall(x) (x).rbegin(),(x).rend()
#define len(x) (int)(x.size())
#define fi first
#define se second
#define append push_back
#define tuple make_pair

#define gh(x) {cout << (x) << '\n';}
// #define Outd(x) {printf("%.10f",x);cout<<endl;}
#define print_vec(vec) { for (size_t iii = 0; iii < vec.size(); iii++) { if (iii == vec.size() - 1) std::cout << vec[iii] << '\n'; else std::cout << vec[iii] << ' '; } }


template<class... T> void in(T&... x) {(cin >> ... >> x);}
#define integer(...) int __VA_ARGS__; in(__VA_ARGS__);cin.ignore();
#ifndef ONLINE_JUDGE
#define de(var) {cerr << #var << ": "; debug_view(var);}
template<typename T> inline void debug_view(T e){cerr << e << endl;}
template<typename T> inline void debug_view(pair<T,T> p){cerr << p.first << ' ' << p.second << endl;}
template<typename T> inline void debug_view(queue<T> q){while(!q.empty()) {cerr << q.front() << " "; q.pop();}cerr << endl;}
template<typename T> inline void debug_view(set<T> s){for(auto x:s){cerr << x << ' ';}cerr << endl;}
template<typename T> inline void debug_view(multiset<T> s){for(auto x:s){cerr << x << ' ';}cerr << endl;}
template<typename T> inline void debug_view(vector<pair<T,T>> &v){for(auto [a,b]: v){cerr<<"{"<<a<<" "<<b<<"} ";} cerr << endl;}
template<typename T> inline void debug_view(vector<T> &v){for(auto e: v){cerr << e << " ";} cerr << endl;}
template<typename T> inline void debug_view(vector<vector<pair<T,T>>> &vv){cerr << "----" << endl;for(auto &v: vv){debug_view(v);} cerr << "--------" << endl;}
template<typename T> inline void debug_view(vector<vector<T>> &vv){cerr << "----" << endl;for(auto &v: vv){debug_view(v);} cerr << "--------" << endl;}
template<typename T1,typename T2> inline void debug_view(map<T1,T2> &mp){cerr << "----" << endl;for(auto [k,v]: mp){cerr << k << ' ' << v << endl;} cerr << "--------" << endl;}
template<typename T1,typename T2> inline void debug_view(map<T1,vector<T2>> &mp){cerr<<"----"<<endl;for(auto [k,v]: mp){cerr<<k<<": ";debug_view(v);} cerr << "--------" << endl;}
template<typename T1,typename T2,typename T3> inline void debug_view(map<pair<T1,T2>,T3> &mp){cerr << "----" << endl;for(auto [p,v]: mp){cerr<<'{'<<p.first<<' '<<p.second<<'}'<<": "<<v<<endl;} cerr<<"--------"<<endl;}
#define deb(var) {cerr << #var << ": "; debugb_view(var);}
template<typename T> inline void debugb_view(T e){bitset<20> b(e); cerr<<b<<endl;}
template<typename T> inline void debugb_view(vector<T> &v){cerr<<"----"<<endl;for(auto e: v){debugb_view(e);}}
#else
#define de(var) {}
#endif

mt19937_64 RNG(chrono::steady_clock::now().time_since_epoch().count());


template<typename T>
unordered_map<T, int> Counter(const vector<T>& a) {
    unordered_map<T, int> counts;
    for (const T& x : a) {
        counts[x]++;
    }
    return counts;
}

vector<int> lst() {
    
    string input;
    getline(cin, input);
    stringstream ss(input);
    vector<int> result;
    int num;
    while (ss >> num) {
        result.push_back(num);
    }
    
    return result;
}

// int integer() {
//     int num;
//     cin >> num;
//     cin.ignore();
//     return num;
// }

string st() {
    string s;
    getline(cin, s);
    if (!s.empty() && s[s.length()-1] == '\n') {
        s.erase(s.length()-1);
    }
    return s;
}

vector<vector<int>> matrixNum(int m) {
    vector<vector<int>> result;
    for (int i = 0; i < m; ++i) {
        result.push_back(lst());
    }
    return result;
}

vector<string> matrixStr(int m) {
    vector<string> matrix;
    for (int i = 0; i < m; i++) {
        matrix.push_back(st());
    }
    return matrix;
}


bool h(int i, int j, string& s, vector<vector<char>>& sp) {
    int r = sp.size();
    int c = sp[0].size();
    for (char d : s) {
        if (d == 'U') {
            i--;
        } else if (d == 'R') {
            j++;
        } else if (d == 'D') {
            i++;
        } else if (d == 'L') {
            j--;
        }
        if (i >= 0 && i < r && j >= 0 && j < c) {
            if (sp[i][j] == '#') {
                return false;
            }
        } else {
            return false;
        }
    }
    return sp[i][j] == '.';
}

template<typename T>
typename T::value_type sum(const T& container) {
    return std::accumulate(container.begin(), container.end(), typename T::value_type());
}


ll max(ll a, ll b) {
    if (a > b)
        return a;
    else
        return b;
}
ll min(ll a, ll b) {
    if (a < b)
        return a;
    else
        return b;
}
int gcd(int a, int b) {
    if (a == 0)
        return b;
    return gcd(b % a, a);
}
int findGCD(vector<int>& arr, int n) {
    int result = arr[0];
    for (int i = 1; i < n; i++) {
        result = gcd(arr[i], result);
 
        if (result == 1) {
            return 1;
        }
    }
    return result;
}
// int power(int x, unsigned int y, unsigned int M) {
//     if (y == 0)
//         return 1;
 
//     int p = power(x, y / 2, M) % M;
//     p = (p * p) % M;
 
//     return (y % 2 == 0) ? p : (x * p) % M;
// }

int power(int base, unsigned int exponent, unsigned int modulus) {   //int power(int base, int exponent, int modulus) { 
    int result = 1;
    base = base % modulus;

    while (exponent > 0) {
        if (exponent % 2 == 1) {
            result = (result * base) % modulus;
        }

        exponent = exponent >> 1;
        base = (base * base) % modulus;
    }

    return result;
}

int modInverse(int A, int M)  // returns modular inverse (works when M is prime)
{
    int g = gcd(A, M);
    if (g != 1) {  // inverse doesnt exist
        return 0;
    }
    else {
        // If a and m are relatively prime, then modulo
        // inverse is a^(m-2) mod m
        return power(A, M - 2, M);
    }
}
bool cmp(pair<int, int> a, pair<int, int> b) {
    if (a.first != b.first) return a.first < b.first;
    return a.second > b.second;
}
bool isPrime(int n)  // O(rt(n))
{
    // Corner cases
    if (n <= 1)
        return false;
    if (n<4)
        return true;
    if (n%2==0 || n%3==0 || n%5==0)
        return false;
    // suppose n=7 that is prime and its pair are (1,7)
    // so if a no. is prime then it can be check by numbers smaller than square root
    //  of the n
    for (int i = 2; i * i <= n; i++) {
        if (n % i == 0)
            return false;
    }
    return true;
}

struct custom_hash {
    static uint64_t splitmix64(uint64_t x) {
        x += 0x9e3779b97f4a7c15;
        x = (x ^ (x >> 30)) * 0xbf58476d1ce4e5b9;
        x = (x ^ (x >> 27)) * 0x94d049bb133111eb;
        return x ^ (x >> 31);
    }

    size_t operator()(uint64_t x) const {
        static const uint64_t FIXED_RANDOM = chrono::steady_clock::now().time_since_epoch().count();
        return splitmix64(x + FIXED_RANDOM);
    }
};

vector<int> myprimes;
unordered_set<int,custom_hash> myprimess;
void SieveOfEratosthenes(int n) {
    // Create a boolean array "prime[0..n]" and initialize
    // all entries it as true. A value in prime[i] will
    // finally be false if i is Not a prime, else true.
    vector<bool> prime(n + 1, true);
 
    for (int p = 2; p * p <= n; p++) {
        // If prime[p] is not changed, then it is a prime
        if (prime[p] == true) {
            // Update all multiples of p greater than or
            // equal to the square of it numbers which are
            // multiple of p and are less than p^2 are
            // already been marked.
            for (int i = p * p; i <= n; i += p)
                prime[i] = false;
        }
    }
 
    // Print all prime numbers
    for (int p = 2; p <= n; p++)
        if (prime[p]) {
            myprimes.push_back(p);
            myprimess.insert(p);
        }
}
void primeFactors(int n) {
    for (int i = 2; i * i <= n; i++) {
        if (n % i == 0) myprimes.push_back(i);
        while (n % i == 0) n /= i;
    }
    if (n > 1) myprimes.push_back(n);
}

class DSU {
public:
    vector<int> parent;
    vector<int> size;
    void make_set(int v) {
        parent[v] = v;
        size[v] = 0;
    }
    DSU(int n) {
        parent.resize(n);
        size.resize(n);
        for (int i = 0; i < n; i++) {
            make_set(i);
        }
    }
    int find_set(int v) {
        if (v == parent[v])
            return v;
        return find_set(parent[v]);
    }
 
    bool union_sets(int a, int b) {
        a = find_set(a);
        b = find_set(b);
        if (a != b) {
            if (size[a] < size[b])
                swap(a, b);
            parent[b] = a;
            size[a] += size[b];
            return false;
        }
        return true;
    }
};

void solve()
{
    // integer(t);
    


}

int32_t main() {

    auto begin = std::chrono::high_resolution_clock::now();
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    #ifndef ONLINE_JUDGE
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    #endif

    int t = 1;
    // integer(t);

    while (t--)
    {
        solve();
    }
    auto end = std::chrono::high_resolution_clock::now();
    auto elapsed = std::chrono::duration_cast<std::chrono::nanoseconds>(end - begin);
    cerr << "Time measured: " << elapsed.count() * 1e-9 << " seconds.\n"; 

    return 0;
}