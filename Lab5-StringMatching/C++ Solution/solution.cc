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
/**
 * Calculates the gain of the two letters 'c1' and 'c2'
 */
int gain(const char& c1, const char& c2){
    return gain_matrix[letter_to_index[c1]][letter_to_index[c2]];
}

/**
 * Find optimal alignment for all the string-pairs in the global vector 'queries',
 * such that the total gain of aligning the strings is maximized
 */
void align_words(){
    string aligned1;
    string aligned2;
    for(const auto& q : queries){
        word1 = q.first;
        word2 = q.second;

        align_words_rec(word1.size()-1, word2.size()-1);
        std::tie(aligned1, aligned2) = backtrack();
        cout << aligned1 << " " << aligned2 << endl;
        align_cache.clear();
    }
}

/**
 * Recursive help function for 'align_words', fills out 'align_cache'
 */
pair<int, int> align_words_rec(const int& pos1, const int& pos2){
    // If we've already computed the value for 'pos1' and 'pos2'
    
}

pair<string, string> backtrack(){

}
