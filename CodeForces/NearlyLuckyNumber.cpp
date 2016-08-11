//
//  NearlyLuckyNumber.cpp
//  
//
//  Created by Elwood Bolton on 11/29/14.
//
//

#include <stdio.h>
#include <iostream>
#include <cctype>
#include <string>
#include <sstream>

using namespace std;

string to_string1(long long inp) {
    ostringstream ss;
    ss << inp;
    return ss.str();
}

bool isLucky(long long inp) {
    string str = to_string1(inp);
    int numLucky = 0;
    
    for (int i = 0; i < str.length(); i++) {
        if (str[i] == '4' || str[i] == '7') {
            numLucky++;
        }
    }
    
    return (numLucky == str.length());
}

long long numLuckyDigits(long long inp) {
    string str = to_string1(inp);
    long long numLuckyDigits = 0;
    
    for (int i = 0; i < str.length(); i++) {
        if (str[i] == '4' || str[i] == '7') {
            numLuckyDigits++;
        }
    }

    return numLuckyDigits;
    
}

int main() {
    long long num;
    long long numLucky;
    
    cin >> num;
    
    if(isLucky(numLuckyDigits(num))){
        cout << "YES" << endl;
    } else {
        cout << "NO" << endl;
    }
    
    
    return 0;
}
