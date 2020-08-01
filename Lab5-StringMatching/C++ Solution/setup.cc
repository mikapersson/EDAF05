#include <iostream>
#include <vector>
#include <map>
#include <tuple>
#include <utility>
#include <string>
#include <sstream>
#include <iterator>

using std::map;
using std::vector;
using std::string;
using std::cin;
using std::cout;
using std::endl;
using std::pair;

// Functions used for verifying that everything is going according to plan
void print_gain_matrix(const vector<vector<int>>&);
void print_letter_index(const map<char, int>&);
void print_queries(const vector<pair<string, string>>&);


/**
 * Read and create gain-matrix (from stdin), create letter-to-index conversion map and queries
 */
std::tuple<vector<vector<int>>, map<char, int>, vector<pair<string, string>>> setup() {
    // Read letters
    string letters_raw;
    std::getline(cin, letters_raw);
    std::istringstream iss(letters_raw);
    vector<char> letters(std::istream_iterator<char>{iss}, std::istream_iterator<char>{});
    auto nr_letters = letters.size();

    // Create gain-matrix
    vector<vector<int>> gain_matrix(nr_letters, vector<int>(nr_letters));
    int temp_int;
    for(vector<char>::size_type i = 0; i != nr_letters; ++i){
        for(vector<char>::size_type j = 0; j != nr_letters; ++j){
            cin >> temp_int;
            gain_matrix[i][j] = temp_int;
        }
    }

    // Create letter-to-index map
    map<char, int> letter_to_index;
    for(vector<char>::size_type i = 0; i != nr_letters; ++i) {
        letter_to_index[letters[i]] = i;
    }

    // Create queries
    vector<pair<string, string>>::size_type nr_queries;
    cin >> nr_queries;
    vector<pair<string, string>> queries;
    string first;
    string second;
    for(vector<pair<string, string>>::size_type i = 0; i != nr_queries; ++i){
        cin >> first >> second;
        queries.emplace_back(first, second);
    }

    return std::make_tuple(gain_matrix, letter_to_index, queries);
}

void print_gain_matrix(const vector<vector<int>>& matrix){
    auto size = matrix.size();
    for(vector<vector<int>>::size_type i = 0; i != size; ++i){
        for(vector<vector<int>>::size_type j = 0; j != size; ++j){
            cout << matrix[i][j] << " ";
        }
        cout << endl;
    }
}

void print_letter_index(const map<char, int>& lti){
    for(const auto& e : lti){
        cout << e.first << " : " << e.second << endl;
    }
}

void print_queries(const vector<pair<string, string>>& q){
    for(const auto& p : q){
        cout << p.first << " : " << p.second << endl;
    }
}
