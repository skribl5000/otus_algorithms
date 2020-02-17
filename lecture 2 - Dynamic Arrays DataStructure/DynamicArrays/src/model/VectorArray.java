package model;

public class VectorArray<T> implements IArray<T> {

    private Object[] array;
    private int vector;
    private int size;

    public VectorArray(int vector) {
        this.vector = vector;
        array = new Object[0];
        size = 0;
    }

    public VectorArray() {
        this(10);
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

        Object[] newArray = new Object[size()];
        for (int j = 0; j < newArray.length; j++){
            if(j < index){
                newArray[j] = array[j];
            }
            else{
                newArray[j] = array[j+1];
            }
        }
        array = newArray;
        check_size();

        return removed_item;
    }

    private void check_size(){
        if (size() - array.length >= vector){
            Object[] newArray = new Object[size() - vector];
            System.arraycopy(array, 0, newArray, 0, size() - vector);
            array = newArray;
        }
    }

    private void resize() {
        Object[] newArray = new Object[array.length + vector];
        System.arraycopy(array, 0, newArray, 0, array.length);
        array = newArray;
    }
}
