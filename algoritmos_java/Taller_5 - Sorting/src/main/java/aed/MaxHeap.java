package aed;
import java.util.Arrays;
public class MaxHeap {
        private Router[] heap;
        private int size;
    
        public MaxHeap(Router[] routers) {
            this.heap = Arrays.copyOf(routers, routers.length);
            this.size = routers.length;
            buildHeap();
        }
    
        public Router desencolar() {
            Router max = heap[0];
            heap[0] = heap[size - 1];
            size--;
            heapifyDown(0);
    
            return max;
        }
    
        private void heapifyDown(int index) {
            int largest = index;
            int leftChild = 2 * index + 1;
            int rightChild = 2 * index + 2;
    
            if (leftChild < size && heap[leftChild].getTrafico() > heap[largest].getTrafico()) {
                largest = leftChild;
            }
    
            if (rightChild < size && heap[rightChild].getTrafico() > heap[largest].getTrafico()) {
                largest = rightChild;
            }
    
            if (largest != index) {
                swap(index, largest);
                heapifyDown(largest);
            }
        }
    
        private void buildHeap() {
            for (int i = size / 2 - 1; i >= 0; i--) {
                heapifyDown(i);
            }
        }
    
        private void swap(int i, int j) {
            Router temp = heap[i];
            heap[i] = heap[j];
            heap[j] = temp;
        }
        public Router obtenerMaximo() {
            return heap[0];
        }
    }