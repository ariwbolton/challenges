//
//  NewYorkHotel.cpp
//  
//
//  Created by Elwood Bolton on 11/30/14.
//
//

#include <stdio.h>
#include <iostream>
#include <cstdlib>

using namespace std;

struct hotel{
    int x;
    int y;
} ;

struct rest{
    int x;
    int y;
} ;

int calcDist(hotel h, rest restaurant){
    //int xDist, yDist;
    
    //xDist = abs(h.x - restaurant.x);
    //yDist = abs(h.y - restaurant.y);
    
    
    //return xDist + yDist;
    return abs(h.x - restaurant.x) + abs(h.y - restaurant.y);
}

int calcFurthest(hotel* hotels, int c, rest restaurant){
    int furthest = 0, tempFurthest;
    
    for (int i = 0; i < c; i++) {
        tempFurthest = calcDist(hotels[i], restaurant);
        
        if(tempFurthest > furthest) furthest = tempFurthest;
    }
    
    return furthest;
}

void findOptimum(int n, int m, hotel* hotels, int c, rest* rests, int h) {
    int minDist = n + m, minIndex = 0, tempDist;
    
    for (int i = 0; i < h; i++) {
        tempDist = calcFurthest(hotels, c, rests[i]);
        
        if(tempDist < minDist) {
            minDist = tempDist;
            minIndex = i;
        }
    }
    
    cout << minDist << endl;
    cout << ++minIndex << endl;
}

int main() {
    int n, m;
    
    cin >> n >> m;
    /*
    int** city;
    
    city = (int**)malloc(sizeof(int*) * n);
    for (int i = 0; i < n; i++) {
        city[i] = (int*)malloc(sizeof(int) * m);
    }
    */
    int c, h;
    
    cin >> c;
    
    hotel* hotels = (hotel*)malloc(sizeof(hotel)*c);
    
    for (int i = 0; i < c; i++) {
        cin >> hotels[i].x >> hotels[i].y;
    }
    
    cin >> h;
    rest* rests = (rest*)malloc(sizeof(rest)*h);
    
    for (int i = 0; i < h; i++) {
        cin >> rests[i].x >> rests[i].y;
    }
    
    //initialized, call code
    findOptimum(n, m, hotels, c, rests, h);
    
    /*
    for (int i = 0; i < n; i++) {
        free(city[i]);
    }
    
    free(city);
     */
    free(hotels);
    free(rests);
    
    return 0;
}