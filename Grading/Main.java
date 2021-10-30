import java.util.Scanner;
class Main{
    public static void main(String[] args){
        Scanner sc=new Scanner(System.in);
        int a=sc.nextInt();
        int b=sc.nextInt();
        int c=sc.nextInt();
        int score =a+b+c;
        if (score<=100 && score>=80){
            System.out.println("A");}
        else if(score<80 && score>=75){
            System.out.println("B+");
        }
        else if(score<75 && score>=70){
            System.out.println("B");
        }
        else if(score<70 && score>=65){
            System.out.println("C+");
        }
        else if(score<65 && score>=60){
            System.out.println("C");
        }
        else if(score<60 && score>=55){
            System.out.println("D+");
        }
        else if(score<55 && score>=50){
            System.out.println("D");
        }
        else{
            System.out.println("F");
        }

    }   
}
