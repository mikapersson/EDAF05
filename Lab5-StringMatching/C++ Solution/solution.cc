#include "setup.cc"

// Global variables in order for the align-function to reach them efficiently
vector<vector<int>> gain_matrix;
map<char, int> letter_to_index;
vector<pair<string, string>> queries;
map<pair<int, int>, pair<int, int>> align_cache;
string word1;
string word2;

// Declare functions used in main
int gain(const char&, const char&);
void align_words();
pair<int, int> align_words_rec(const int&, const int&);
pair<string, string> backtrack();

int main() {
    std::tie(gain_matrix, letter_to_index, queries) = setup();
    

}

// Define functions used in main
int gain(const char& c1, const char& c2){

}

void align_words(){

}

pair<int, int> align_words_rec(const int& pos1, const int& pos2){

}

pair<string, string> backtrack(){

}
