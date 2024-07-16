#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
using namespace std;
struct jugador {
    string nombre;
    int ataque = 0;
    int defensa = 0;
};

bool compara_jug (jugador a,jugador b){
    if (a.ataque > b.ataque){return true;}
    if (a.ataque == b.ataque && a.defensa < b.defensa){return true;}
    if (a.ataque == b.ataque && a.defensa == b.defensa && a.nombre < b.nombre){return true;}
    return false;
}
bool compara_nombre (jugador a,jugador b){
    return a.nombre < b.nombre;
}


int main(){
    int casos;
    cin >> casos;
    vector<vector<jugador>> respuestas;
    for (int a = 0; a < casos; a++){
        vector<jugador> jugadores;
        jugador jugador;
        for (int i = 0; i < 10; i++){
            cin >> jugador.nombre >> jugador.ataque >> jugador.defensa;
            jugadores.push_back(jugador);
        }
        sort(jugadores.begin(),jugadores.end(),compara_jug);
        sort(jugadores.begin(),jugadores.begin()+5,compara_nombre);
        sort(jugadores.begin()+5,jugadores.begin()+10,compara_nombre);
        respuestas.push_back(jugadores);
    }
    for (int k = 0; k < casos; k++){
        cout << "Case " << k+1 <<":"<<endl;
        cout << "(";
        for (int j = 0; j < 5; j++){
            cout << respuestas[k][j].nombre;
            if (j<4){cout << ", " ;}
        }
        cout << ")"<<endl;
        cout << "(";
        for (int j = 5; j < 10; j++){
            cout << respuestas[k][j].nombre;
            if (j<9){cout << ", " ;}
        }
        cout << ")"<<endl;
    }
}