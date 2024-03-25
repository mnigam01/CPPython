#include <bits/stdc++.h>
using namespace std;

#define ascii_lowercase "abcdefghijklmnopqrstuvwxyz"
#define ascii_uppercase "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
// #define int long long
#define ll long long
#define inf (int)1e18
#define yes "yes"
#define no "no"
#define mod 1000000007


#define fo(i, a, b) for (int i = a; i < b; ++i)
#define ro(i, a, b) for (int i = a; i >b; --i)

// #define fo(i, a, b, ...) for (int i = a; i < b; i+=(__VA_ARGS__ == NULL ? 1 : __VA_ARGS__))
// #define ro(i, a, b, ...) for (int i = a; i > b; i-=(__VA_ARGS__ == NULL ? 1 : __VA_ARGS__))

#define all(x) (x).begin(),(x).end()
#define rall(x) (x).rbegin(),(x).rend()
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
    string input;
    getline(cin, input);
    return input;
}

vector<vector<int>> matrixNum(int m) {
    vector<vector<int>> result;
    for (int i = 0; i < m; ++i) {
        result.push_back(lst());
    }
    return result;
}

vector<vector<char>> matrixStr(int m) {
    vector<vector<char>> matrix;
    for (int i = 0; i < m; i++) {
        string input;
        getline(cin, input);
        vector<char> row;
        for (char c : input) {
            row.push_back(c);
        }
        matrix.push_back(row);
    }
    return matrix;
}


bool h2(int i, int j, string& s, vector<vector<char>>& sp) {
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

int power(int base, int exponent, int modulus) {
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


void precompute() {
    
}

unordered_map<char, pair<int, int>> dir = {
    {'U', {-1, 0}},
    {'R', {0, 1}},
    {'D', {1, 0}},
    {'L', {0, -1}}
};
// vector<std::vector<int>> dir = {{-1, 0}, {0, 1}, {1, 0}, {0, -1}};


template <class S, S (*op)(S, S), S (*e)()>
struct SegTree {
    int n, size, log;
    vector<S> d;
    SegTree() : SegTree(0) {}
    explicit SegTree(int n) : SegTree(vector<S>(n, e())) {}
    explicit SegTree(const vector<S> &v) : n(int(v.size())) {
        log = ceil_pow2(n), size = 1 << log;
        d = vector<S>(2 * size, e());
        for (int i = 0; i < n; i++) d[size + i] = v[i];
        for (int i = size - 1; i >= 1; i--) update(i);
    }

    int ceil_pow2(int n) {  // minimum non-neg x s.t. `n <= 2^x`
        int x = 0;
        while ((1U << x) < (unsigned int)(n)) x++;
        return x;
    }
    void set(int p, S x) {  // assert(0 <= p < n)
        p += size, d[p] = x;
        for (int i = 1; i <= log; ++i) update(p >> i);
    }
    S get(int p) const { return d[p + size];}
    S prod(int l, int r) {   // [l, r)
        S sl = e(), sr = e();
        l += size, r += size;
        while (l < r) {
            if (l & 1) sl = op(sl, d[l++]);
            if (r & 1) sr = op(d[--r], sr);
            l >>= 1, r >>= 1;
        }
        return op(sl, sr);
    }
    S all_prod() const {return d[1];}

    void update(int k) {
        d[k] = op(d[2 * k], d[2 * k + 1]);
    }
    template <bool (*f)(S)> int max_right(int l) const {
        return max_right(l, [](S x) { return f(x); });
    }
    template <class F>     // 0 <= l <= n, f(e()) is true
    int max_right(int l, F f) const { 
        if (l == n) return n;
        l += size;
        S x = e();
        do {
            while (l % 2 == 0) l >>= 1;
            if (!f(op(x, d[l]))) {
                while (l < size) {
                    l = (2 * l);
                    if (f(op(x, d[l]))) {
                        x = op(x, d[l]);
                        l++;
                    }
                }
                return l - size;
            }
            x = op(x, d[l]);
            l++;
        } while ((l & -l) != l);
        return n;
    }
    template <bool (*f)(S)> int min_left(int r) const {
        return min_left(r, [](S x) { return f(x); });
    }
    template <class F>  // 0 <= r <= n, f(e()) is true
    int min_left(int r, F f) const {
        if (r == 0) return 0;
        r += size;
        S x = e();
        do {
            r--;
            while (r > 1 && (r % 2)) r >>= 1;
            if (!f(op(d[r], x))) {
                while (r < size) {
                    r = (2 * r + 1);
                    if (f(op(d[r], x))) {
                        x = op(d[r], x);
                        r--;
                    }
                }
                return r + 1 - size;
            }
            x = op(d[r], x);
        } while ((r & -r) != r);
        return 0;
    }
};

struct S {
    int a, acnt, b, bcnt;
    S(int a_val, int acnt_val, int b_val, int bcnt_val) 
        : a(a_val), acnt(acnt_val), b(b_val), bcnt(bcnt_val) {}

    // Constructor to initialize from a vector
    S(const vector<int>& v) {
        a = v[0];
        acnt = v[1];
        b = v[2];
        bcnt = v[3];
    }
};

// S op(S a, S b) {
//     if (a.a == b.a) {
//         if (a.b == b.b) return S{a.a, a.acnt+b.acnt, a.b, a.bcnt+b.bcnt};
//         if (a.b < b.b) return S{a.a, a.acnt+b.acnt, b.b, b.bcnt};
//         return S{a.a, a.acnt+b.acnt, a.b, a.bcnt};
//     }
//     if (a.a < b.a) swap(a, b);
//     if (a.b == b.a) return S{a.a, a.acnt, a.b, a.bcnt+b.acnt};
//     if (a.b < b.a) return S{a.a, a.acnt, b.a, b.acnt};
//     return a;
// }



S op(S x, S y) {
    unordered_map<int, int> d;
    d[x.a]+=x.acnt;
    d[x.b]+=x.bcnt;
    d[y.a]+=y.acnt;
    d[y.b]+=y.bcnt;
    
    
    vector<pair<int, int>> p(d.begin(), d.end());
    std::sort(p.begin(), p.end(), [](const auto& a, const auto& b) {
        return a.first > b.first;
    });

    std::vector<int> tmp = {p[0].first, p[0].second};
    if (p.size() != 1) {
        tmp.push_back(p[1].first);
        tmp.push_back(p[1].second);
    } else {
        tmp.push_back(0);
        tmp.push_back(0);
    }
    return S(tmp);
}

S e() {
    return S{0, 0, 0, 0};
}




void solve()
{
    integer(n,q);
    auto a = lst();
    // vector<S> b; 
    // for (auto i:a){
    //     b.push_back(S{i,1,0,0});
    // }
    SegTree<S, op, e> seg(n);
    fo(i,0,n){
        seg.set(i,S{a[i],1,0,0});
    }

    




    while (q--){
        integer(c,l,r);
        // de(c);de(l);de(r);
        if (c == 1) {
            seg.set(l - 1, S{r, 1, 0, 0});
        } else {
            auto cnt = seg.prod(l - 1, r);
            gh(cnt.bcnt);
        }
    }
    
}



int32_t main() {

    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    // #ifndef ONLINE_JUDGE
    // freopen("input.txt","r",stdin);
    // freopen("output.txt","w",stdout);
    // #endif

    int t = 1;
    // integer(t);
    precompute();

    while (t--)
    {

        solve();

    }

    return 0;
}