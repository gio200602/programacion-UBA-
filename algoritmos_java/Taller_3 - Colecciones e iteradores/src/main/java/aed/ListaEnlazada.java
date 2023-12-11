package aed;

import java.util.*;

public class ListaEnlazada<T> implements Secuencia<T> {
    private int _size;
    private Nodo _prim;
    private Nodo _ulti;
    private class Nodo {
        T valor;
        Nodo sig;
        Nodo ant;
        Nodo(T v) { valor = v; ant = null; sig = null; }
    }

    public ListaEnlazada() {
        _prim = null;
        _ulti = null;
        _size = 0;
    }

    public int longitud() {
        return _size;
    }

    public void agregarAdelante(T elem) {
        Nodo nuevo = new Nodo(elem);
        if (_size == 0){
            _prim = nuevo;
            _ulti = nuevo;
        } else {
            nuevo.sig = _prim;
            nuevo.sig.ant = nuevo;
            _prim = nuevo;
        }
        _size++;
    }

    public void agregarAtras(T elem) {
        Nodo nuevo = new Nodo(elem);
        if (_size == 0){
            _prim = nuevo;
            _ulti = nuevo;
        } else {
            nuevo.ant = _ulti;
            nuevo.ant.sig= nuevo;
            _ulti = nuevo;
        }
        _size++;
    }

    public T obtener(int i) {
        Nodo actual = _prim;
        for (int a = 0; a < i ; a++){
            actual = actual.sig;
        }
        return actual.valor;
    }

    public void eliminar(int i) {
        Nodo actual = _prim;
        if(_size == 1){
            _prim = null;
            _ulti = null;

        } else if (i == 0) {
            _prim = actual.sig;
            actual.sig.ant = null;
        } else if (i == _size-1){
            actual = _ulti;
            _ulti = actual.ant;
            actual.ant.sig = null;
        } else {
            Nodo prev = _prim;
            for(int j=0;j < i;j++){
                prev = actual;
                actual = actual.sig;
            }
            prev.sig = actual.sig;
            actual.sig.ant = prev;
        }
        _size--;
    }

    public void modificarPosicion(int indice, T elem) {
        Nodo actual = _prim;
        for (int i = 0; i < indice; i++){
            actual = actual.sig;
        }
        actual.valor = elem;
    }

    public ListaEnlazada<T> copiar() {
        ListaEnlazada<T> l= new ListaEnlazada<T>();
        Nodo actual = this._prim;
        for (int i=0; i<_size; i++){
            l.agregarAtras(actual.valor);
            actual = actual.sig;
        }
        return l;
    }

    public ListaEnlazada(ListaEnlazada<T> lista) {
        ListaEnlazada<T> copy = lista.copiar();
        this._prim = copy._prim;
        this._size = copy._size;
        this._ulti = copy._ulti;
        
    }
    
    @Override
    public String toString() {
        String s = new String();
        s = "[";
        Nodo actual = _prim;
        while (actual != null){
            if (actual.sig == null){
                s=s + actual.valor;
            } else {
                s=s + actual.valor + ", ";
            }
            actual = actual.sig;
        }
        s = s + "]";
        return s;
    }

    private class ListaIterador implements Iterador<T> {
    	int pos;
        ListaIterador(){
            pos = 0;
            }
        public boolean haySiguiente() {
	        return pos < _size ;
        }
        
        public boolean hayAnterior() {
	        return pos > 0;
        }

        public T siguiente() {
	        int i = pos;
            pos = pos + 1;
            return obtener(i);
        }
        

        public T anterior() {
	        int i = pos;
            pos = pos - 1;
            return obtener(i-1);
        }
    }
    

    public Iterador<T> iterador() {
	    return new ListaIterador();

    }

}
