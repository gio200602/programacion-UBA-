#include <iostream>
using namespace std;
int sumaDivisores(int n){
    int i = 2;
    int sum = 1;
    while (i<=n){
        if (n % i !=0){
           
            i = i + 1;
        }else {
            sum = sum + i;
            i = i + 1;
        }
    }
    return sum;
}

//version recursiva
int sumaDivisores_recursiva(int n){
    
}

int main(){
    int x;
    cout << "Ingrese un valor" << endl;
    cin >> x;
    while (x<0){
        cout << "Ingrese un valor positivo " << endl;
        cin >> x;
    }
    int num = sumaDivisores(x);
    cout <<"el resultado de la suma de sus divisores es "<< num <<endl;
    return 0;
}