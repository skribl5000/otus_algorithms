package model;

public class FactorArray<T> implements IArray<T> {

    private Object[] array;
    private int factor;
    private int size;

    public FactorArray(int factor, int initLength) {
        this.factor = factor;
        array = new Object[initLength];
        size = 0;
    }

    public FactorArray() {
        this(50, 10);
    }

    @Override
    public int size() {
        return size;
    }

    @Override
    public void add(T item) {
        if (size() == array.length)
            resize();
        array[size] = item;
        size++;
    }

    @Override
    @SuppressWarnings("unchecked")
    public T get(int index) {
        return (T)array[index];
    }

    @Override
    public void insert(T item, int index){
        if (index >= array.length){
            throw new IllegalArgumentException("Index out of range");
        }
        if (size() == array.length)
            resize();
        for (int j = array.length - 1; j > index; j --){
            array[j] = array[j-1];
        }
        array[index] = item;
    }

    @Override
    public T remove(int index){
        if (index >= array.length){
            throw new IllegalArgumentException("Index out of range");
        }
        T removed_item = get(index);
        Object[] newArray = new Object[array.length];
        for (int j = 0; j < array.length - 1; j++) {
            if (j < index)
                newArray[j] = array[j];
            else
                newArray[j] = array[j+1];
        }
        array = newArray;
        return removed_item;
    }


    private void resize() {
        Object[] newArray = new Object[array.length + array.length * factor / 100];
        System.arraycopy(array, 0, newArray, 0, array.length);
        array = newArray;
    }
}
