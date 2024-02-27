#include <bits/stdc++.h>
using namespace std;

#define ascii_lowercase "abcdefghijklmnopqrstuvwxyz"
#define ascii_uppercase "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
#define int long long
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


// bool h(int i, int j, const string& s, const vector<vector<char>>& sp) {
//     int r = sp.size();
//     int c = sp[0].size();
//     for (char d : s) {
//         if (d == 'U') {
//             i--;
//         } else if (d == 'R') {
//             j++;
//         } else if (d == 'D') {
//             i++;
//         } else if (d == 'L') {
//             j--;
//         }
//         if (i >= 0 && i < r && j >= 0 && j < c) {
//             if (sp[i][j] == '#') {
//                 return false;
//             }
//         } else {
//             return false;
//         }
//     }
//     return sp[i][j] == '.';
// }

map<int,int> res;
void h(vector<int> &s, int ind = 1) {
    if (ind == 10) {
        auto tot = accumulate(s.begin(), s.end(), 0);
        if (tot == 0) {
            return;
        }
        int num = 0;
        for (int digit : s) {
            num = num * 10 + digit;
        }
        if (res.find(tot)==res.end()){
            res[tot] = 9999999999999;
        }
        res[tot] = min(res[tot], num);
        return;
    }
    s.push_back(ind);
    h(s, ind + 1);
    s.pop_back();
    h(s, ind + 1);
}


int32_t main() {

    // auto begin = std::chrono::high_resolution_clock::now();

    auto t = 0;cin>>t;
    vector<int> s;
    h(s);
    while (t--)
    {

        int x;cin>>x;
        if (res.find(x) != res.end()) {
            x = res[x];
            cout << x << endl; // Assuming gh(x) is equivalent to printing x
        } else {
            cout << -1 << endl; // Assuming gh(-1) is equivalent to printing -1
        }
        
    }
    

    // auto end = std::chrono::high_resolution_clock::now();
    // auto elapsed = std::chrono::duration_cast<std::chrono::nanoseconds>(end - begin);
    // cerr << "Time measured: " << elapsed.count() * 1e-9 << " seconds.\n"; 
    return 0;
}