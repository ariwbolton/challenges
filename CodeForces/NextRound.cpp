//
//  NextRound.cpp
//  
//
//  Created by Elwood Bolton on 11/29/14.
//
//

#include <stdio.h>
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    int n, k, num = 0, isTied = 0;
    
    cin >> n >> k;
    int array[n];
    
    for (int i = 0; i < n; i++) {
        cin >> array[i];
        //cout << array[i] << " " ;
    }
    
    num = k - 1;
    int i;
    
    if(array[num] == 0) {
        for(i = num; (array[i] == 0) && i >= 0; i--);
        if (i < num) {
            cout << ++i << endl;
            return 0;
        }
    }
    
    
    for(i = 1; (array[num + i] == array[num + i - 1]) && i + num < n; i++);
    
    num += i;
    /*
    while((num < k || isTied) && array[num] > 0){
        if(num < k) {
            num++;
            continue;
        }
        
        if (array[num] == array[num - 1]) {
            num++;
            isTied = 1;
            continue;
        } else {
            isTied = 0;
            continue;
        }
        
        break;
    }
    */
    cout << num << endl;
    
    
    return 0;
}
