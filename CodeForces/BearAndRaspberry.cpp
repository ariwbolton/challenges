//
//  BearAndRaspberry.cpp
//  
//
//  Created by Elwood Bolton on 11/30/14.
//
//

#include <stdio.h>
#include <iostream>

using namespace std;

int main() {
    int n, c, max = 0, maxi = 0;
    
    cin >> n >> c;
    
    int values[n];
    
    for (int i = 0; i < n; i++) {
        cin >> values[i];
    }
    
    for (int i = 0; i < n - 1; i++) {
        if ((values[i] - values[i + 1] - c) > max) {
            max = values[i] - values[i + 1] - c;
            maxi = i;
        }
    }
    
    cout << max << endl;
    
    return 0;
}