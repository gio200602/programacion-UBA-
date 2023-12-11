package aed;

class Funciones {
    int cuadrado(int x) {
        return x*x;
    }

    double distancia(double x, double y) {
        double res=0.0;
        res = Math.sqrt( x*x + y*y);
        return res;
    }

    boolean esPar(int n) {
        return n % 2 == 0;
    }

    boolean esBisiesto(int n) {
        return ((n%4==0 && n%100!=0) || n%400==0);
    }

    int factorialIterativo(int n) {
        if (n<2){
            return 1;
        }
        int res =1;
        for (int i = 1;i <= n; i++ ){
            res = i * res;
        }
        return res;
    }

    int factorialRecursivo(int n) {
        int res = 0;
        if (n <= 1){
            res = 1;
        } else {
            res = n * factorialIterativo(n-1);
        }
        return res;
    }

    boolean esPrimo(int n) {
        if (n < 2){
            return false;
        }
        boolean esP = true;
        int i = 2;
        while (esP == true && i < n ){
            esP = (n%i != 0);
            i++;
        }
        return esP;
    }

    int sumatoria(int[] numeros) {
        int res = 0;
        for (int i = 0; i< numeros.length; i++){
            res = res + numeros[i];
        }
        return res;
    }

    int busqueda(int[] numeros, int buscado) {
        for (int i = 0; i< numeros.length; i++){
            if (numeros[i]== buscado) {
                return i;
            }
        }
        return numeros.length;
    }

    boolean tienePrimo(int[] numeros) {
        for (int i = 0; i< numeros.length; i++){
            if (esPrimo(numeros[i])) {
                return true;
            }
        }
        return false;
    }

    boolean todosPares(int[] numeros) {
        boolean sonPar = true;
        for (int i = 0; i< numeros.length; i++){
            if (esPar(numeros[i]) == false) {
                sonPar = false;
            }
        }
        return sonPar;
    }

    boolean esPrefijo(String s1, String s2) {
        boolean esPre = true;
        for (int i = 0; i < s1.length();i++){
            if (i >= s2.length() ||(s1.charAt(i) != s2.charAt(i))){
                esPre = false;
            }
        }
            
        return esPre;
    }

    boolean esSufijo(String s1, String s2) {
        boolean esSuf = true;
        for (int i = 0; i < s1.length();i++){
            if (i >= s2.length() || (s1.charAt(s1.length() - 1- i)!= s2.charAt(s2.length()-1 - i))){
                esSuf = false;
            }
        }
        return esSuf;
    }
}
