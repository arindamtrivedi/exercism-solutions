#include "armstrong_numbers.h"
#include<vector>
#include<cmath>

namespace armstrong_numbers {
    bool is_armstrong_number(int n){
        std::vector<int> digits = {}; int sum{0}; int num{n};
        //First, we have to separate the digits.
        do{
            digits.push_back(num%10);
            num /= 10;
        }while(num!=0);
        //Now, we evaluate the sum
        for(int i: digits){
            sum += std::pow(i, digits.size());
        }
        //Check if sum and original number are equal
        if(n == sum)
            return true;
        return false;
    }
}  // namespace armstrong_numbers
