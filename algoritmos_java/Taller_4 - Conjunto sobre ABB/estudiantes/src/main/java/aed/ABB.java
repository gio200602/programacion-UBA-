package aed;

import java.util.*;

// Todos los tipos de datos "Comparables" tienen el método compareTo()
// elem1.compareTo(elem2) devuelve un entero. Si es mayor a 0, entonces elem1 > elem2
public class ABB<T extends Comparable<T>> implements Conjunto<T> {
    private int _cardinal;
    private Nodo _raiz;
    private class Nodo {
        T valor;
        Nodo izq;
        Nodo der;
        Nodo padre;
        Nodo(T v) { valor = v; izq = null; der = null; padre = null; }

    }

    public ABB() {
        _raiz = null;
        _cardinal = 0;
    }

    public int cardinal() {
        return _cardinal;
    }

    public T minimo(){
        Nodo actual = _raiz;
        while (actual.izq != null){
            actual = actual.izq;
        }
        return actual.valor;
    }

    public T maximo(){
        Nodo actual = _raiz;
        while (actual.der != null){
            actual = actual.der;
        }
        return actual.valor;
    }

    public void insertar(T elem){
        Nodo nuevo = new Nodo(elem);
        if (_raiz == null) {
            _raiz = nuevo;
            _cardinal++;
        } else if (pertenece(elem)==false) {
            Nodo actual =_raiz;
            boolean inserto = false;
            while (inserto == false){
                if (((actual.valor.compareTo(elem)) < 0) && (actual.der == null)) {
                    inserto = true;
                    actual.der = nuevo;
                    nuevo.padre = actual;
                    _cardinal++;
    
                } else if (((actual.valor.compareTo(elem)) > 0) && (actual.izq == null)) {
                    inserto = true;
                    actual.izq = nuevo;
                    nuevo.padre = actual;
                    _cardinal++;
                } else if (((actual.valor.compareTo(elem)) < 0) && (actual.der != null)) {
                    actual = actual.der;
                } else if (((actual.valor.compareTo(elem)) > 0) && (actual.izq != null)) {
                    actual = actual.izq;
                }
            }
        }
    }

    public boolean pertenece(T elem){
        Nodo actual = _raiz;
        boolean esta = false;
        while(actual != null) {
            if ((actual.valor.compareTo(elem))==0) {
                return true;
            } else if (actual.valor.compareTo(elem) < 0) {
                actual = actual.der;
            } else {
                actual = actual.izq;
            }
        }
        return esta;
    }

    public void eliminar(T elem){
        if (pertenece(elem) == false){
            return;
        }
        Nodo actual = _raiz;
        if ((_raiz.valor.compareTo(elem)) == 0 && _cardinal == 1){
            _raiz = null;
            _cardinal--;
            return;
        } else if ((_raiz.valor.compareTo(elem)) == 0 && _raiz.der == null && _raiz.izq != null){
            _raiz = actual.izq;
            actual.izq = null;
            _raiz.padre = null;
            _cardinal--;
            return;
        } else if ((_raiz.valor.compareTo(elem)) == 0 && _raiz.izq == null && _raiz.der != null) {
            _raiz = actual.der;
            actual.der = null;
            _raiz.padre = null;
            _cardinal--;
            return;
        } else if ((_raiz.valor.compareTo(elem)) == 0 && _raiz.izq != null && _raiz.der != null) {
            actual = actual.der;
            while (actual.izq != null) {
                actual = actual.izq;
            }
            T valor = actual.valor;
            eliminar(actual.valor);
            _raiz.valor = valor;
            return;
        }
        boolean elimino = false; 
        while (elimino == false && actual != null) {
            if ((actual.valor.compareTo(elem)) == 0 && actual.der == null && actual.izq == null) {
                if (actual.padre.der == actual) {
                    actual.padre.der = null;
                    actual.padre = null;
                } else {
                    actual.padre.izq = null;
                    actual.padre = null;
                }
                elimino = true;
            } else if ((actual.valor.compareTo(elem)) == 0 && actual.der == null && actual.izq != null){
                if (actual.padre.der == actual) {
                    actual.padre.der = actual.izq;
                    actual.izq.padre = actual.padre;
                    actual.padre = null;
                } else {
                    actual.padre.izq = actual.izq;
                    actual.izq.padre = actual.padre;
                    actual.padre = null;
                }
                elimino = true;
            } else if ((actual.valor.compareTo(elem)) == 0 && actual.der != null && actual.izq == null){
                if (actual.padre.der == actual) {
                    actual.padre.der = actual.der;
                    actual.der.padre = actual.padre;
                    actual.padre = null;
                } else {
                    actual.padre.izq = actual.der;
                    actual.der.padre = actual.padre;
                    actual.padre = null;
                }
                elimino = true;
            } else if ((actual.valor.compareTo(elem)) == 0 && actual.der != null && actual.izq != null) {
                Nodo siguiente = actual.der;
                while (siguiente.izq != null) {
                    siguiente = siguiente.izq;
                }
                T nuevo = siguiente.valor;
                eliminar(siguiente.valor);
                actual.valor = nuevo;
                _cardinal++;
                elimino = true;
            } else if (((actual.valor.compareTo(elem)) < 0) && elimino == false) {
                actual = actual.der;
            } else if (((actual.valor.compareTo(elem)) > 0) && elimino == false){
                actual = actual.izq;
            }
        }
        _cardinal--;
    }

    public String toString(){
        String s = new String();
        s = "{";
        Iterador<T> it = iterador();
        while (it.haySiguiente()==true){
            s = s + it.siguiente()+",";
        }
        s=s.substring(0, s.length() - 1);
        s = s + "}";
        return s;
    }

    private class ABB_Iterador implements Iterador<T> {
        private Nodo _actual;
        
        ABB_Iterador(){
            _actual = _raiz;
            while (_actual.izq != null){
                _actual = _actual.izq;
            }
        }
        public boolean haySiguiente() {            
            return _actual != null;
        }
    
        public T siguiente() {
            Nodo actual = _actual;
            Nodo hijo = _actual;
            T valor = actual.valor;
            if (actual.der != null){
                actual = actual.der;
                while (actual.izq != null) {
                    actual = actual.izq;
                }
            } else {
                actual = actual.padre;
                while (actual != null && actual.der == hijo ) {
                    hijo = actual;
                    actual = actual.padre;
                }
            }
            _actual = actual;
            return valor;
        }
    }

    public Iterador<T> iterador() {
        return new ABB_Iterador();
    }


}