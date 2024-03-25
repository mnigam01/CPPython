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


template<class... T> void in(T&... x) {(cin >> ... >> x);}
#define integer(...) int __VA_ARGS__; in(__VA_ARGS__);cin.ignore();
#ifndef __DEBUG
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
unordered_map<string,int> memo;



int h(int f, int ind, std::string &minim, std::vector<std::vector<char>>& s) {
    // std::pair<int, int> key = {f, ind};
    auto key = to_string(f)+'-'+to_string(ind);
    if (memo.find(key) != memo.end()) {
        return memo[key];
    }
    if (ind >= minim.size() - 1) {
        return 1;
    }
    if (f == 0) {
        int x = 0;
        if (minim[ind] == s[0][ind]) {
            x += h(f, ind + 1, minim, s);
        }
        if (minim[ind] == s[1][ind - 1]) {
            x += h(1, ind + 1, minim, s);
        }
        memo[key] = x;
        return x;
    } else {
        int x;
        if (minim[ind] == s[1][ind - 1]) {
            x = h(f, ind + 1, minim, s);
            memo[key] = x;
            return x;
        }
        memo[key] = 0;
        return 0;
    }
}


void solve()
{
    

    integer(n);
    auto s = matrixStr(2);

    std::vector<char> stk;
    stk.push_back(s[0][0]);
    int f = 1;
    for (int i = 0; i < n; ++i) {
        char x = '4', y = '4';
        x = (i + 1 < n) ? s[0][i + 1] : '3';
        y = s[1][i];
        if (x == y) {
            stk.push_back(x);
        } else if (f && x < y) {
            stk.push_back(x);
            // f = 0;
        } else {
            stk.push_back(y);
            f = 0;
        }
    }
    std::string minim(stk.begin(), stk.end());

    

    int x = h(0,1,minim,s);
    std::cout << minim << '\n';
    std::cout << x << '\n';
       

}

int32_t main() {

    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    // int t = 1;
    integer(t);

    while (t--)
    {

        solve();

    }

    return 0;
}