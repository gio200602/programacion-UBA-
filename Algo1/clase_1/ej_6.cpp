#include <iostream>
using namespace std;
int sumaimpar(int n){
    int i = 1;
    int sum = 0;
    while (i<n){
        if (i % 2 !=0){
            sum = sum + i;
            i = i + 1;
        }else {
            i = i + 1;
        }
    }
    return sum;
}

//version recursiva
int sumaImpar_recursiva(int n){
    if (n==2){
        return 1;
    } else if (n<2){
        return 0;
    } else {
        if ((n-1) % 2 == 1){
            return sumaImpar_recursiva(n-1)+(n-1);
        } else {
            return sumaImpar_recursiva(n-1);
        }    
    }
}

int main(){
    //Escribir la funcion que dado n ∈ N devuelve la suma de todos los numeros impares menores que n.
    int x;
    cout << "Ingrese un valor positivo para sumar" << endl;
    cin >> x;
    //si no hay una precondicion
    while (x<0){
        cout << "Ingrese un valor positivo para sumar " << endl;
        cin >> x;
    }
    //int num = sumaimpar(n);
    int num = sumaImpar_recursiva(x);
    cout <<"el resultado de la suma de sus impares menores es "<< num <<endl;
    return 0;
}