#include <bits/stdc++.h>

using namespace std;

template<typename T>
unordered_map<T, int> counter(const vector<T>& a) {
    unordered_map<T, int> counts;
    for (const T& x : a) {
        counts[x]++;
    }
    return counts;
}

int main() {
    vector<int> a_int = {1, 2, 3, 1, 2, 1, 2, 3, 3, 3};
    vector<string> a_string = {"apple", "banana", "apple", "orange", "banana"};
    vector<char> a_char = {'a', 'b', 'c', 'a', 'b', 'c'};

    // Count occurrences for integers
    auto d_int = counter(a_int);

    // Print the counts for integers
    cout << "Counts for integers:" << endl;
    for (const auto& pair : d_int) {
        cout << pair.first << ": " << pair.second << endl;
    }

    // Count occurrences for strings
    unordered_map<string, int> d_string = counter(a_string);

    // Print the counts for strings
    cout << "\nCounts for strings:" << endl;
    for (const auto& pair : d_string) {
        cout << pair.first << ": " << pair.second << endl;
    }

    // Count occurrences for characters
    unordered_map<char, int> d_char = counter(a_char);

    // Print the counts for characters
    cout << "\nCounts for characters:" << endl;
    for (const auto& pair : d_char) {
        cout << pair.first << ": " << pair.second << endl;
    }

    return 0;
}
