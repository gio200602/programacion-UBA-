#include <iostream>

using namespace std;
//version recursivo
void collatz_recu(int n, int& cantPasos){
    if (n == 1){
        return;
    }
    cantPasos++;
    if (n % 2 == 0){
        collatz_recu(n/2,cantPasos);
    } else {
        collatz_recu(n*3+1,cantPasos);
    }    
}


//version iterativa
void collatz(int n, int& cantPasos){
    while (n != 1){
        if (n % 2 == 0){
            n = n/2;
        }else{
            n = n*3 +1; 
        }
        cantPasos++;
    }    
}

int main() {
    int n, cantPasos = 1;
    cin >> n;
    collatz(n,cantPasos);
    
    //Devuelvo la cantidad de pasos
    cout << "la cantidad de pasos de collatz es: " << cantPasos << endl;
    return 0;
}
