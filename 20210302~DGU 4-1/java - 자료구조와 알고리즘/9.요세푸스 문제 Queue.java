import java.util.*;

public class Main {
	static void printJosepus(int n, int k) {
		int size = n+1;
		int[] queue = new int[size];
		int head =0, tail =0;
		
		for (int i =1; i<=n; i++) {
			queue[tail++] = i;
		}
		
		while(head != tail) {
		
			for(int i=0; i<k-1; i++) {
				int v = queue[head];
				head = (head+1)%size;
				queue[tail] = v;
				tail = (tail+1)%size;
				
			}
			int v = queue[head];
			head = (head+1)%size;
			System.out.println(v);
		}
		
		
		
		
	}

	
	
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		int k = sc.nextInt();
		printJosepus(n,k);
		

	}

}

