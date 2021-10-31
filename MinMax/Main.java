import  java.util.*;
class Main{
    public static void main(String[] args){
        Scanner sc=new Scanner(System.in);
        int num=sc.nextInt();
        List<Integer> list=new ArrayList<Integer>();
        for (int i=0;i<num;i++){
            int n=sc.nextInt();
            list.add(n);
        }
        Collections.sort(list);
        System.out.println(list.get(0));
        System.out.println(list.get(num-1));
    }
}