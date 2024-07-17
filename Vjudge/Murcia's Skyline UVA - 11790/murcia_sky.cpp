#include <iostream>
#include <vector>

using namespace std;

int incremento(vector<int> &alturas,vector<int> &anchos,int i,int ult_max,vector<vector<int>> &M){
    if (i == alturas.size()){
        return 0;
    }
    if ( M[i][ult_max+1] != -1){
        return M[i][ult_max+1];
    }
    int sub_con = 0;
    if (ult_max == -1 || alturas[i] > alturas[ult_max] ){
        sub_con = incremento(alturas,anchos,i+1,i,M)+anchos[i];
    }
    M[i][ult_max+1] = max(incremento(alturas,anchos,i+1,ult_max,M),sub_con);
    return M[i][ult_max+1];
}

int decremento(vector<int> &alturas,vector<int> &anchos,int i,int ult_max,vector<vector<int>> &N){
    if (i == -1){
        return 0;
    }
    if ( N[i][ult_max-1] != -1){
        return N[i][ult_max-1];
    }
    int sub_con = 0;
    if (ult_max == anchos.size() || alturas[i] > alturas[ult_max] ){
        sub_con = decremento(alturas,anchos,i-1,i,N)+anchos[i];
    }
    N[i][ult_max-1] = max(decremento(alturas,anchos,i-1,ult_max,N),sub_con);
    return N[i][ult_max-1];
}

int main(){
    ios_base::sync_with_stdio(0);cin.tie(0);cout.tie(0);
    int casos;
    cin >> casos;
    for (int j = 0; j < casos; j++){
        int cant_edif;
        cin >> cant_edif;
        vector<int> alturas;
        vector<int> anchos;
        int a;
        for (int leer = 0; leer < cant_edif; leer++){
            cin >> a;
            alturas.push_back(a);
        }
        for (int leer = 0; leer < cant_edif; leer++){
            cin >> a;
            anchos.push_back(a);
        }
        vector<vector<int>> M (cant_edif,vector<int>(cant_edif,-1));
        int suma_arriba = incremento(alturas,anchos,0,-1,M);
        vector<vector<int>> N (cant_edif,vector<int>(cant_edif,-1));
        int suma_baja = decremento(alturas,anchos,cant_edif-1,cant_edif,N);
        cout << "Case " << j+1 << ". ";
        if (suma_arriba >= suma_baja){
            cout <<"Increasing (" << suma_arriba << ")." << " Decreasing (" << suma_baja << ")." << endl;
        } else {
            cout <<"Decreasing (" << suma_baja << ")." << " Increasing (" << suma_arriba << ")." << endl;
        }
    }
}