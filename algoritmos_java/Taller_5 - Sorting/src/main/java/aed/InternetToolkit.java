package aed;
public class InternetToolkit {
    public InternetToolkit() {
    }

    public Fragment[] tcpReorder(Fragment[] fragments) {
        for (int i=1 ;i < fragments.length;i++) {
            Fragment clave = fragments[i];
            int j = i-1;
            while (j>=0 && fragments[j].compareTo(clave)>0) {
                fragments [j+1] = fragments[j];
                j--;
            }
            fragments[j+1] = clave;
        }
        return fragments;
    }

    public Router[] kTopRouters(Router[] routers, int k, int umbral) {
        MaxHeap heapRouters = new MaxHeap(routers);
        int i =0;                                                       //O(1)
        boolean cumple= true;                                           
        Router[] res = new Router[k];
        while (i<k && cumple==true) {                                   //O(k log(n))
            Router max = heapRouters.obtenerMaximo();
            if (max.getTrafico() < umbral) {
                cumple = false;
            } else {
                Router r= heapRouters.desencolar();
                res[i]=r;
            }
            i++;
        }
        return res;                                                     //O(n + k log(n))
    }

    public IPv4Address[] sortIPv4(String[] ipv4) {
        IPv4Address [] nuevo = new IPv4Address[ipv4.length];
        for (int i = 0; i < ipv4.length ; i++){
            IPv4Address ip = new IPv4Address(ipv4[i]);
            nuevo[i] = ip;
        }
        for (int i = 0; i < nuevo.length - 1; i++) {
            // Encuentra el mínimo del subarreglo no ordenado
            int minIndex = i;
            for (int j = i + 1; j < nuevo.length; j++) {
                if (comparaMin(nuevo[j], nuevo[minIndex]) < 0) {
                    minIndex = j;
                }
            }
            // Intercambia el mínimo con el elemento actual
            if (minIndex != i) {
                IPv4Address temp = nuevo[i];
                nuevo[i] = nuevo[minIndex];
                nuevo[minIndex] = temp;
            }
        }
        return nuevo;
    }

    public int comparaMin(IPv4Address a,IPv4Address b){
        for (int i = 0; i < 4; i++){
            if (a.getOctet(i) < b.getOctet(i)) {
                return -1;
            } else if (a.getOctet(i) > b.getOctet(i)) {
                return 1;
            }
        }
        // Los elementos son iguales
        return 0;
    }

}
