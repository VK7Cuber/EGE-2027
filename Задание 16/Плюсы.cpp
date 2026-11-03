#include <iostream>

using namespace std;

float f(float n){
    if (n < 10) return n;
    return 3 * n + f(n-3);
}

int main(){
   cout << (f(6250) + 2*f(6244)) / f(6238);
   return 0;
}