import model.*;

import java.util.Date;

public class Program {

    public static void main(String[] args) {
        IArray<Integer> test = new FactorArray<>();
        test.add(1);//0
        test.add(2);//1
        test.add(3);//2
        test.add(4);//3
        test.add(5);//4
        test.add(6);//5
        test.add(7);//6

        //"Test for insert" ;
        int item = 50;
        int index = 6;
        int old_item = test.get(index);
        test.insert(item, index);
        if (test.get(index) == item && test.get(index + 1) == old_item){
            System.out.println("Insert Test Passed");
        }
        else{
            System.out.println("Insert Test Failed");
        }

        // Test for remove
        test.remove(index);
        if (test.get(index) == old_item){
            System.out.println("Remove Test Passed");
        }
        else{
            System.out.println("Remove Test Failed");
        }
    }

//    private static void testAddArray(IArray data, int total) {
//        long start = System.currentTimeMillis();
//
//        for (int j = 0; j < total; j ++)
//            data.add(new Date());
//
//        System.out.println(data + " testAddArray: " +
//                (System.currentTimeMillis() - start));
//    }
}
