//
//  ArrivalOfTheGeneral.cpp
//  
//
//  Created by Elwood Bolton on 11/29/14.
//
//

#include <stdio.h>
#include <iostream>
#include <algorithm>

using namespace std;

int main() {
    int n, i, min = 101, imin = 0, max = 0, imax = 0;
    cin >> n;
    int soldiers[n];
    
    for (i = 0; i < n; i++) cin >> soldiers[i];
    
    for (i = 0; i < n; i++) {
        if (soldiers[i] <= min) {
            min = soldiers[i];
            imin = i;
        }
        
        if (soldiers[i] > max) {
            max = soldiers[i];
            imax = i;
        }
    }
    
    if (imax < imin) {
        cout << (imax + (n - 1 - imin)) << endl;
    } else { //imax >= imin
        cout << (imax + (n - 1 - imin) - 1) << endl;
        
    }
    
    return 0;
}