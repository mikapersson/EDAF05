#include "setup.cc"
#include <algorithm>  // std::max

using std::tie;

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
    tie(gain_matrix, letter_to_index, queries) = setup();
    align_words();

    return 0;
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
        tie(aligned1, aligned2) = backtrack();
        cout << aligned1 << " " << aligned2 << endl;
        align_cache.clear();
    }
}

/**
 * Recursive help function for 'align_words', fills out 'align_cache'
 */
pair<int, int> align_words_rec(const int& pos1, const int& pos2){
    // If we've already computed the value for 'pos1' and 'pos2'
    auto it = align_cache.find({pos1, pos2});
    if(it != align_cache.end()){
        return it->second;
    } else {
        int position;  // determines what alternative is optimal (insert * in word1, word2? etc..)
        int max_gain;

        // Three base cases
        if(pos1 == -1 && pos2 == -1){
            position = 0;
            max_gain = 0;
        } else if(pos1 > -1 && pos2 == -1){
            position = 2;
            max_gain = -4 * (pos1+1);
        } else if(pos1 == -1 && pos2 > -1){
            position = 1;
            max_gain = -4 * (pos2+1);
        } else {
            // The two letters that are to be compared
            char letter1 = word1[pos1];
            char letter2 = word2[pos2];

            // No '*' added
            int gain1;
            int position1;
            tie(gain1, position1) = align_words_rec(pos1-1, pos2-1);
            gain1 += gain(letter1, letter2);

            // '*' added after letter1
            int gain2;
            int position2;
            tie(gain2, position2) = align_words_rec(pos1, pos2-1);
            gain2 -= 4;

            // '*' added after letter2
            int gain3;
            int position3;
            tie(gain3, position3) = align_words_rec(pos1-1, pos2);
            gain3 -= 4;

            // Determine which of the three cases that was optimal
            int temp_max = std::max(gain1, gain2);
            max_gain = std::max(temp_max, gain3);
            if(max_gain == gain1){
                position = 0;
            } else if(max_gain == gain2){
                position = 1;
            } else {
                position = 2;
            }
        }

        align_cache.emplace(std::make_pair(pos1, pos2), std::make_pair(max_gain, position));
        return std::make_pair(max_gain, position);
    }
}

/**
 * Finds the optimal alignment of 'word1' and 'word2' with respect to 'align_cache'
 */
pair<string, string> backtrack(){
    string aligned1("");
    string aligned2("");

    int pos1 = word1.size()-1;
    int pos2 = word2.size()-1;

    while(pos1 >= 0 || pos2 >=0){
        int ignore;
        int position;
        tie(ignore, position) = align_cache[{pos1, pos2}];

        char letter1 = (pos1 >= 0) ? word1[pos1] : '*';
        char letter2 = (pos2 >= 0) ? word2[pos2] : '*';

        if(position == 0){
            aligned1 = letter1 + aligned1;
            aligned2 = letter2 + aligned2;
            pos1 -= 1;
            pos2 -= 1;
        } else if(position == 1){
            aligned1 = '*' + aligned1;
            aligned2 = letter2 + aligned2;
            pos2 -= 1;
        } else {
            aligned1 = letter1 + aligned1;
            aligned2 = '*' + aligned2;
            pos1 -= 1;
        }
    }

    return std::make_pair(aligned1, aligned2);
}
