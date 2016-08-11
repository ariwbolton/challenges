//
//  EvenOdds.cpp
//  
//
//  Created by Elwood Bolton on 11/29/14.
//
//

#include <stdio.h>
#include <iostream>

using namespace std;

int main() {
    int n, m;
    cin >> n >> m;
    int k = m - 1;
    
    /*
    if(n % 2 == 0) { // n is even
        if (k % 2 == 0) { // k is even
            cout << ((n / 2) + (k / 2))<< endl;
        } else { // k is odd
            cout << (k / 2) << endl;
        }
        
    } else { // n is odd
        if (k % 2 == 0) { // k is even
            cout << ((n / 2) + (k / 2) + 1)<< endl;
        } else { // k is odd
            cout << (k / 2) << endl;
        }
    }
    */
    if(n % 2 == 0) { // n is even
        if (k <= (n / 2)) { // k is odd
            cout << ((2 * k) + 1)<< endl;
        } else { // k is odd
            cout << (2 * (k - (n / 2)))<< endl;
        }
        
    } else { // n is odd
        if (k <= ((n / 2) + 1)) { // k is odd
            cout << ((2 * k) + 1)<< endl;
        } else { // k is odd
            cout << (2 * (k - (n / 2) + 1))<< endl;
        }
    }

    
    
    return 0;
}