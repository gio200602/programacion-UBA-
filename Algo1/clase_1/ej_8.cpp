#include <iostream>
using namespace std;
int fact(int a) {
    int prod = 1;
    for(int i=1;i<=a;i++) {
        prod=prod*i;
    }
    return prod;
}
int combinatorio (int n, int k) {
    if(n==k || k==0) {
        return 1;
    } else {
        return fact(n)/(fact(k)*fact(n-k));
    }
}

int main(){
    int n;
    int k;
    cout << "Ingrese un valor" << endl;
    cin >> n;
    while (n<0){
        cout << "Ingrese un valor positivo " << endl;
        cin >> n;
    }
    cout << "Ingrese otro valor" << endl;
    cin >> k;
    while (n<0){
        cout << "Ingrese un valor positivo " << endl;
        cin >> k;
    }
   
    int num = combinatorio(n,k);
    cout <<"el resultado combinatorio es "<< num <<endl;
    return 0;
}
