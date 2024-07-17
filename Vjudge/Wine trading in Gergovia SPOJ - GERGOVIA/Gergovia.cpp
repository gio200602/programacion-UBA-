#include <iostream>
#include <vector>
using namespace std;
typedef long long abc;

abc total (vector<abc> vinos,abc casos){
    abc trabajo = 0;
    vector<abc> casa_compra;
    vector<abc> casa_vende;
    for(abc j = 0; j < casos; j++){
        if(vinos[j] > 0){
            casa_compra.push_back(j);
        }
        else if (vinos[j] < 0){
            casa_vende.push_back(j);
        }
    }
    if (casa_compra.size()==0 || casa_vende.size() == 0){
        return 0;
    }
    abc compra = 0;
    abc vende = 0;
    while (compra < casa_compra.size() && vende < casa_vende.size()){
        abc distancia= casa_vende[vende]-casa_compra[compra];
        if (distancia < 0){distancia = (-1)*distancia;}
        if (vinos[casa_compra[compra]]==vinos[casa_vende[vende]]*(-1)){
            trabajo = trabajo + vinos[casa_compra[compra]]*distancia;
            compra++;
            vende++;
        }else if (vinos[casa_compra[compra]]>vinos[casa_vende[vende]]*(-1)){
            trabajo = trabajo + distancia*vinos[casa_vende[vende]]*(-1);
            vinos[casa_compra[compra]]=vinos[casa_compra[compra]]+vinos[casa_vende[vende]];
            vinos[casa_vende[vende]]=0;
            vende++;
        }else{
            trabajo = trabajo + distancia*vinos[casa_compra[compra]];
            vinos[casa_vende[vende]] = vinos[casa_vende[vende]] + vinos[casa_compra[compra]];
            vinos[casa_compra[compra]] = 0;
            compra++;
        }
    }
    return trabajo;
}

int main(){
    ios_base::sync_with_stdio(false);
    abc casos;
    cin >> casos;
    vector<abc> respuestas;
    while (casos != 0){
        vector<abc> vinos(casos);
        for (abc i = 0; i < casos; i++){
            cin >> vinos[i];
        }
        abc res = total(vinos,casos);
        respuestas.push_back(res);
        cin >> casos;
    }
    for (abc k = 0; k < respuestas.size(); k++){
        cout << respuestas[k] << endl;
    }
    cout << endl;
}