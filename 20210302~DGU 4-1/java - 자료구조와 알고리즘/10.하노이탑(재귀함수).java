import java.util.*;


public class Main {

	//하노이탑
	static void hanoi(int n, char a, char b, char c) {
		if(n==1) {
			System.out.println(a+"->"+b);
			return;
		}
		hanoi(n-1,a,c,b);
		hanoi(1,a,b,c);
		hanoi(n-1,c,b,a);
	}
	
	
	//피보나치 수열
	static int fib(int n) {
		if(n ==1 || n==2) return 1;
		
		return fib(n-1) + fib(n-2);
		
	}
	
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner scan = new Scanner(System.in);
		int n = scan.nextInt();
		hanoi(n,'a','b','c');
		

		
		System.out.println("fib("+n+") = "+fib(n));
	}

}
