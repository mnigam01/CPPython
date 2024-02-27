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

typedef vector<int> vi;


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

int integer() {
    int num;
    cin >> num;
    cin.ignore();
    return num;
}

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

void solve()
{
    int y,x;cin>>x>>y;cin.ignore();
    auto maxi = max(x,y);
    ll e = maxi*maxi;
    // cout<< e <<'\n';
    if (maxi&1){
        ll t = e-(abs(1-x)+abs(maxi-y));   // 9-(1+0)
        cout<< t <<'\n';

    }else{
        ll t = e-(abs(maxi-x)+abs(1-y));
        cout<< t <<'\n';

    }

    


}

int32_t main() {

    int t = 1;
    cin>>t;cin.ignore();

    while (t--)
    {

        solve();

    }

    
    

    return 0;
}