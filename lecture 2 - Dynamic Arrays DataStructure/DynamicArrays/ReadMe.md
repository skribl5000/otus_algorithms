Динамические массивы:

SingleArray:
  При необходимости расширить массив используется метод resize, создающий новый массив, на 1 ед. больше старого.
  В новый массив копируется старый, затем старый заменяется на новый
VectorArray:
  При расширении массива к нему прибавляется Vector - определенное фиксированное число элементов
FactorArray:
  При расширении используется множитель - фактор. Во столько раз растет массив при необходимости.
  
