//
//  VanyaAndCubes.cpp
//  
//
//  Created by Elwood Bolton on 12/1/14.
//
//

#include <stdio.h>
#include <iostream>

using namespace std;

int main() {
    int n;
    
    cin >> n;
    
    int array[100];
    
    for (int i = 0; i < 100; i++) {
        array[i] = (i * (i + 1)) / 2;
    }
    
    for(int i = 1; i < 100; i++) {
        array[i] += array[i - 1];
    }
    
    int i;
    for (i = 0; array[i] <= n; i++) ;
    
    cout << --i << endl;
    
    return 0;
}