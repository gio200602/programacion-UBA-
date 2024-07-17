#include <iostream>
using namespace std;
int Fibonacci (int x){
    int f0 = 0;
    int f1 = 1;
    int fib= 0;
// se simplifica poniendo al final de todo solo return fib en vez de cada if, solo si devuelvo una misma variable
    if (x == 0) {
        fib=f0;
        return fib;
       
    } else if (x==1) {
        fib=f1;
        return fib;
       
    } else {
        while (x>=2){
            fib = f1+f0;
            f0=f1;
            f1=fib;
            x=x-1;
        }
        return fib;
    }
}

//version recursiva
int Fibonacci_recursivo(int x){
    if (x < 1){
        return 0;
    } else if (x <=2){
        return 1;
    } else {
        return Fibonacci_recursivo(x-2)+Fibonacci_recursivo(x-1);
    }    
}

int main(){
    int x;
    cout << "Ingrese un valor x mayor a 0 " << endl;
    cin >> x;
    while (x<0){
        cout << "Ingrese un valor x mayor a 0 " << endl;
        cin >> x;
    }
    int f=Fibonacci(x);
    cout << " El numero de Fibonacci en esa posicion es : " << f << endl ;
    return 0;
}