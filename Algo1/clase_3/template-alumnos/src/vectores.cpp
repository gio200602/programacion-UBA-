#include "vectores.h"

// Función para probar en main.cpp si este módulo fue cargado correctamente
void holaModuloVectores(){
    cout << "El módulo vectores fue cargado correctamente" << endl;
}


//Ejercicio
bool divide(vector<int> v, int a){
	// Dados un vector v y un int a, decide si a divide a todos los numeros de v.
	bool res = true;
	int i = 0;
	while (res == true && i < v.size()){
		if (v[i] % a != 0){
			res = false;
		}
		i++;
	}
	
}

//Ejercicio
int mayor(vector<int> v){
	// Dado un vector v, devuelve el valor maximo encontrado.
}

//Ejercicio
vector<int> reverso(vector<int> v){
	// Dado un vector v, devuelve el reverso.
}

//Ejercicio
vector<int> rotar(vector<int> v, int k){
	vector<int> w;
    int i = 0;
    while (i < v.size()){
        if ((i+k) >= v.size()) {
            w.push_back((v.at(((i+k) - (v.size())))));
            i = i+1;
        }
        else {
            w.push_back(v.at((i+k)));
            i = i+1;
        }
    }
    return w;
}

//Ejercicio
vector<int> factoresPrimos(int n){
	//que dado un entero devuelve un vector con los factores primos del mismo
}

//Ejercicio
void mostrarVector(vector<int> v){
	//que dado un vector de enteros muestra por la salida estándar, el vector
	// Ejemplo: si el vector es <1, 2, 5, 65> se debe mostrar en pantalla [1, 2, 5, 65]
}
