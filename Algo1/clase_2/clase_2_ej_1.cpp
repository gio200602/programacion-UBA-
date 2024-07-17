#include <iostream>
using namespace std;

//Repeticion controlada por un contador para 10 alumnos

int main(){
    double x;
    double suma = 0;
    int i = 0;
    while (i < 10){
        cout << "Ingrese nota de examen del 0 al 10. Alumno numero:  " << i+1 << endl;
        cin >> x;
        suma = suma + x;
        i++;
    }
    double promedio = suma/i;
    cout << "La suma total de las notas es: " << suma << endl;
    cout << "El promedio es: " << promedio << endl;
    return 0;
}