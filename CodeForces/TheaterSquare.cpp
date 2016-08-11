//
//  TheaterSquare.cpp
//  
//
//  Created by Elwood Bolton on 11/29/14.
//
//

#include <stdio.h>
#include <iostream>

using namespace std;

int main() {
    long long n, m, a;
    long long numN, numM;
    cin >> n >> m >> a;
    
    // (n / a) * a + (n % a)
    
    numN = (n / a) * a;
    numM = (m / a) * a;
    
    //cout << n << m << a << numN << numM << endl;
    
    if (numN < n) {
        numN /= a;
        numN++;
    } else {
        numN /= a;
    }
    
    if (numM < m) {
        numM /= a;
        numM++;
    } else {
        numM /= a;
    }
    //cout << numN << numM << endl;
    cout << numN * numM << endl;

    return 0;
}
