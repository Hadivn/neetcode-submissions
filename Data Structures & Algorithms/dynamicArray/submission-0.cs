public class DynamicArray {
    
    private int capacity;
    private int length;
    private int[] arr;

    public DynamicArray(int capacity) {
        this.capacity = capacity;
        this.length = 0;
        this.arr = new int[capacity];
    }

    public int Get(int i) {
        return this.arr[i];
    }

    public void Set(int i, int n) {
        this.arr[i] = n;
    }

    public void PushBack(int n) {
        if (this.length == this.capacity) {
            Resize();
        }
        this.arr[this.length] = n;
        this.length++;
    }

    public int PopBack() {
        if (this.length > 0) {
            this.length--;
        }
        return this.arr[this.length];
    }

    private void Resize() {
        this.capacity *= 2;
        int[] newArr = new int[this.capacity];
        for (int i = 0; i < this.length; i++) {
            newArr[i] = this.arr[i];
        }
        this.arr = newArr;
    }

    public int GetSize() {
        return this.length;
    }

    public int GetCapacity() {
        return this.capacity;
    }
}