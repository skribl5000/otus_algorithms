package model;

import java.util.logging.ErrorManager;

public class SingleArray<T> implements IArray<T> {

    private Object[] array;

    public SingleArray () {
        array = new Object[0];
    }

    @Override
    public int size() {
        return array.length;
    }

    @Override
    public void add(T item) {
        resize();
        array[size() - 1] = item;
    }

    @Override
    @SuppressWarnings("unchecked")
    public T get(int index) {
        return (T)array[index];
    }

    @Override
    public void insert(T item, int index){
        if (index > size()){
            throw new IllegalArgumentException("Index out of range");
        }
        resize();
        for (int j = array.length - 1; j > index; j --){
            array[j] = array[j-1];
        }
        array[index] = item;
    }

    @Override
    public T remove(int index){
        if (index > size()){
            throw new IllegalArgumentException("Index out of range");
        }
        T removed_item = get(index);
        Object[] newArray = new Object[size() - 1];
        for (int j = 0; j < newArray.length; j ++) {
            if (j < index) {
                newArray[j] = array[j];
            } else {
                newArray[j] = array[j + 1];
            }
        }
        array = newArray;
        return removed_item;
    }

    private void resize() {
        Object[] newArray = new Object[size() + 1];
        System.arraycopy(array, 0, newArray, 0, size());
//        for (int j = 0; j < size(); j ++)
//            newArray[j] = array[j];
        array = newArray;
    }
}
