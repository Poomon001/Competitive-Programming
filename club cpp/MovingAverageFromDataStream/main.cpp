#include <iostream>
#include <vector>

/**
     Link: https://leetcode.com/problems/moving-average-from-data-stream/
     Purpose: Calculate the moving average of all integers in the sliding window
     parameter: None
     return: None
     Pre-Condition: 1 <= size <= 1000
                  : -10^5 <= val <= 10^5
                  : At most 10^4 calls will be made to next.
     Post-Condition: none
**/
class MovingAverage_M1 {
    std::vector<int> window;
private:
    int count;
    int index;
    double total;
    int size;

public:
    explicit MovingAverage_M1(int size) : window(size) {
        this->size = size;
        count = 0;
        index = 0;
        total = 0;
    }

    double next(int val) {
        // check if there is space in window
        if (count < size) {
            index = (index + 1) % size;
            count++;
        }else{
            index = (index + 1) % size;
            total -= window[index];
        }

        // remove the element
        total += val;
        window[index] = val;

        return total / count;
    }
};

/**
     Link: https://leetcode.com/problems/moving-average-from-data-stream/
     Purpose: Calculate the moving average of all integers in the sliding window
     parameter: None
     return: None
     Pre-Condition: 1 <= size <= 1000
                  : -10^5 <= val <= 10^5
                  : At most 10^4 calls will be made to next.
     Post-Condition: none
**/
class MovingAverage_M2 {
private:
    int* window;
    int count;
    int index;
    double total;
    int size;

public:
    explicit MovingAverage_M2(int size) {
        this->size = size;
        window = new int[size];
        count = 0;
        index = 0;
        total = 0;
    }

    ~MovingAverage_M2() {
        std::cout << "Clean Up array memory" << "\n";
        delete[] window;
    }

    double next(int val) {
        // check if there is space in window
        if (count < size) {
            index = (index + 1) % size;
            count++;
        }else{
            index = (index + 1) % size;
            total -= window[index];
        }

        // remove the element
        total += val;
        window[index] = val;

        return total / count;
    }
};

int main() {
    std::cout << "\n" << "=== M1 Test1 ===" << "\n";
    MovingAverage_M1* mv1 = new MovingAverage_M1(3);
    std::cout << mv1->next(15) << "\n";
    std::cout << mv1->next(5) << "\n";
    std::cout << mv1->next(10) << "\n";
    std::cout << mv1->next(3) << "\n";
    std::cout << mv1->next(12) << "\n";
    std::cout << mv1->next(4) << "\n";
    delete mv1;

    std::cout << "\n" << "=== M1 Test2 ===" << "\n";
    MovingAverage_M1 mv2(3);
    std::cout << mv2.next(15) << "\n";
    std::cout << mv2.next(5) << "\n";
    std::cout << mv2.next(10) << "\n";
    std::cout << mv2.next(3) << "\n";
    std::cout << mv2.next(12) << "\n";
    std::cout << mv2.next(4) << "\n";

    std::cout << "\n" << "=== M2 Test3 ===" << "\n";
    MovingAverage_M2* mv3 = new MovingAverage_M2(3);
    std::cout << mv3->next(15) << "\n";
    std::cout << mv3->next(5) << "\n";
    std::cout << mv3->next(10) << "\n";
    std::cout << mv3->next(3) << "\n";
    std::cout << mv3->next(12) << "\n";
    std::cout << mv3->next(4) << "\n";
    delete mv3;

    std::cout << "\n" << "=== M2 Test4 ===" << "\n";
    MovingAverage_M2 mv4(3);
    std::cout << mv4.next(15) << "\n";
    std::cout << mv4.next(5) << "\n";
    std::cout << mv4.next(10) << "\n";
    std::cout << mv4.next(3) << "\n";
    std::cout << mv4.next(12) << "\n";
    std::cout << mv4.next(4) << "\n";

    return 0;
}
