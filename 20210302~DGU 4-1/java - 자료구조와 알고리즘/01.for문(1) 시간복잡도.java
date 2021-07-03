package dslab4;
import java.util.*;

public class Main {
	static long sum(int n) {
		long sum = 0;
		for(int i = 1; i<=n; i++) sum += i;
		
		return sum;
	}
	
	// advanced algorithm for summing from 1 to n.
	static long advSum(int n) {
		
		
		long sum = (long)n*(n+1)/2;
		
		return sum;
		
	}
	
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		long timeStamp = System.currentTimeMillis();
		long result = advSum(n);
		
		long elapsedTime = System.currentTimeMillis() - timeStamp;
		System.out.println("sum from 1 to "+n+" is "+result);
		System.out.println("Elapsed time is "+elapsedTime+"ms");
		
	}

}
