#include <iostream>
using namespace std;

//Repeticion controlada por un centinela. Modificar el programa anterior para que 
//el numero de estudiantes sea arbitrario. Por ejemplo: Ingrese la nota (-1 para terminar):


int main(){
    int x = 0;
    double suma = 0;
    int i = 0;
    while (x != -1){
        cout << "Ingrese nota de examen del 0 al 10. -1 para terminar. Alumno numero  " << i+1 << endl;
        cin >> x;
        if (x != -1){
            i++;
            suma = suma + x;
        }
    }
    double promedio = suma/i;
    cout << "La suma total de las notas es: " << suma << endl;
    cout << "El promedio es: " << promedio << endl;
    return 0;
}