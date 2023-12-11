package aed;

import java.util.Scanner;
import java.util.Vector;
import java.io.PrintStream;

class Archivos {
    float[] leerVector(Scanner entrada, int largo) {
        float[] vector = new float [largo];
        for (int i=0;i < largo;i++){
            vector[i] = entrada.nextFloat();
        }
        return vector;
    }

    float[][] leerMatriz(Scanner entrada, int filas, int columnas) {
        float[][] matrix = new float[filas][columnas];
        for (int i=0;i < filas; i++){
            for (int j=0; j < columnas; j++){
                matrix [i][j] = entrada.nextFloat();
            }
        }
        return matrix;
    }

    void imprimirPiramide(PrintStream salida, int alto) {
        for (int i=0; i< alto ;i++){
            for (int a=0;a < alto - i-1  ;a++){
                salida.print(" ");
            }
            for (int b=0;b < (2*i)+1;b++){
                salida.print("*");
            }
            for (int c=0;c < alto - i-1 ;c++){
                salida.print(" ");
            }
            salida.print("\n");
        }
    }
}
