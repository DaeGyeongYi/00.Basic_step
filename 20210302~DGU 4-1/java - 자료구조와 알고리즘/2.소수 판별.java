package dslab5;
import java.util.*;

public class Main {
	static boolean isPrime(int p) {
		int dcount = 0;
		for(int i = 1; i<=p; i++) {
			if (p%i ==0) dcount ++;
		}
		return dcount ==2;
	}
	static boolean isPrime1(int p) {
		if (p ==1 ) return false;
		for (int i =2; i<p; i++) {
			if (p%i == 0 ) return false;
		}
		return true;
	}
	
	static boolean isPrime2(int p) {
		if (p ==1 ) return false;
		for (int i =2; i*i<=p; i++) {
			if (p%i == 0 ) return false;
		}
		return true;
	}
	
	static int pi(int n) {
		int pcount = 0;
		for (int i =1; i<=n; i++) {
			if(isPrime2(i)) pcount++;
		}
		return pcount;
	}
	
	
	
	public static void main(String[] args) {
		
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		long timestamp = System.currentTimeMillis();
		int pcount =  pi(n);
		long elapsed = System.currentTimeMillis() - timestamp;
		System.out.println("pi("+n+")="+pcount);
		
		System.out.println("Elapsed time is "+elapsed+" ms");
	}
}
