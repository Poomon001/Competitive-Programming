#include <iostream>
#include <string>
#include <algorithm>

/**
     Link: https://leetcode.com/problems/maximum-score-after-splitting-a-string
     Purpose: Given a string s of zeros and ones, Find the maximum score after splitting the string into left substring and right substring.
            : The score after splitting a string is the number of zeros in the left substring plus the number of ones in the right substring.
            : All possible ways of splitting s into two non-empty substrings are:
              left = "0" and right = "11101", score = 1 + 4 = 5
              left = "01" and right = "1101", score = 1 + 3 = 4
              left = "011" and right = "101", score = 1 + 2 = 3
              left = "0111" and right = "01", score = 1 + 1 = 2
              left = "01110" and right = "1", score = 2 + 1 = 3
     parameter: string s - a string of '0' and '1'
     return: int ans - the score
     Pre-Condition: 2 <= s.length <= 500
                  : The string s consists of characters '0' and '1' only.
     Post-Condition: none
**/
// prefix counting - runtime: O(n), memory: O(1)
int maxScore(std::string s) {
    int one = std::count(s.begin(), s.end(), '1');
    int zero = 0;
    int ans = 0;

    for(int i = 0; i < s.length() - 1; i++) {
        if (s.at(i) == '1'){
            one -= 1;
        }else{
            zero += 1;
        }
        ans = std::max(ans, one + zero);
    }

    return ans;
}

int main() {
    std::cout << maxScore("1011101") << std::endl; // 5
    std::cout << maxScore("00111") << std::endl; // 5
    std::cout << maxScore("1111") << std::endl; // 3
    std::cout << maxScore("011101") << std::endl; // 5
    std::cout << maxScore("11100") << std::endl; // 2
    std::cout << maxScore("00") << std::endl; // 1
    std::cout << maxScore("0100") << std::endl; // 2
    return 0;
}
