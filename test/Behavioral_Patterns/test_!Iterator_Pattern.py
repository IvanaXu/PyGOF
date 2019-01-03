# -*-coding:utf-8-*-
# @auth ivan
# @time 2016-10-21 18:41:32
# @goal test for Iterator Pattern


class Iterator:
    def __init__(self):
        return

    def hasNext(self):
        return

    def next(self):
        return


class Container:
    def __init__(self):
        return

    def getIterator(self):
        return


class NameRepository(Container):
    def __init__(self):
        Container.__init__(self)
        self.names = {"Robert", "John", "Julie", "Lora"}

    def getIterator(self):
        return

    class NameIterator(Iterator):
        def __init__(self):
            Iterator.__init__(self)
            self.index = 0
            print(self.names)

        def hasNext(self):
            if self.index < len(self.names):
                return True
            return False

        def next(self):
            if self.hasNext():
                return
            return
NameRepository().NameIterator()

"""
Iterator.java

public interface Iterator {
   public boolean hasNext();
   public Object next();
}

Container.java

public interface Container {
   public Iterator getIterator();
}


创建实现了 Container 接口的实体类。该类有实现了 Iterator 接口的内部类 NameIterator。

NameRepository.java

public class NameRepository implements Container {
   public String names[] = {"Robert" , "John" ,"Julie" , "Lora"};

   @Override
   public Iterator getIterator() {
      return new NameIterator();
   }

   private class NameIterator implements Iterator {

      int index;

      @Override
      public boolean hasNext() {
         if(index < names.length){
            return true;
         }
         return false;
      }

      @Override
      public Object next() {
         if(this.hasNext()){
            return names[index++];
         }
         return null;
      }
   }
}


IteratorPatternDemo.java

public class IteratorPatternDemo {

   public static void main(String[] args) {
      NameRepository namesRepository = new NameRepository();

      for(Iterator iter = namesRepository.getIterator(); iter.hasNext();){
         String name = (String)iter.next();
         System.out.println("Name : " + name);
      }
   }
}

"""



