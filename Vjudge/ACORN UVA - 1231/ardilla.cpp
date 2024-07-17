#include <iostream>
#include <vector>
using namespace std;

int mejor(vector<vector<int>>& M,int vuelo,vector<int> cant_max_pos,int altura, int cant_arboles){
    for (int i = 0; i < altura; i++){
        int cant_mayor=0;
        for (int j = 0; j < cant_arboles; j++){
            if (i > 0){
                if (i-vuelo >= 0){
                    // caso si puedo volar entre arboles veo si es rentable comparando con la 
                    // posicion anterior a M
                    M[j][i]= max(M[j][i-1],cant_max_pos[i-vuelo])+M[j][i];
                    if (cant_mayor < M[j][i]){
                        cant_mayor = M[j][i];
                    }
                }else{
                    // si no se puede volar entonces es copiar y sumar con lo de abajo
                    M[j][i]=M[j][i]+M[j][i-1];
                    if (cant_mayor < M[j][i]){
                        cant_mayor = M[j][i];
                    }
                }  
            }else{
                //caso base osea en el piso
                if (cant_mayor < M[j][i]){
                    cant_mayor = M[j][i];
                }
            }
            
        }
        cant_max_pos.push_back(cant_mayor);
    }
    return cant_max_pos[altura-1];
}


int main(){
    std::ios_base::sync_with_stdio(false);
    int casos,cant_arboles,altura_arboles,vuelo;
    cin >> casos;


    vector<int> respuestas;
    // repito n = casos la cantidad de problemas a resolver
    for(int k=0;k < casos;k++){
        cin >> cant_arboles >> altura_arboles >> vuelo;


        //matriz de bellotas de [cantidad_arboles][altura_arboles]
        vector<vector<int>> M (cant_arboles,vector<int>(altura_arboles,0));
        //la cantidad maxima en esa altura del arbol
        vector<int> cant_max_pos;
        //matriz con la cantidad de bellotas en cada posicion

        
        for (int i = 0; i < cant_arboles; i++){
            int bellotas;
            int a;
            cin >> bellotas;
            for (int j = 0; j < bellotas; j++){
                cin >> a;
                M[i][a-1] = M[i][a-1]+1;
            }    
        }
        

        int res = mejor(M,vuelo,cant_max_pos,altura_arboles,cant_arboles);
        respuestas.push_back(res);
    }
    // int a;
    // cin >> a;
    // devuelvo la respuesta
    for (int a = 0; a < respuestas.size(); a++){
        cout << respuestas[a]<< endl;
    }
}