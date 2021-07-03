import java.util.*;

class Queue {
		int N = 100;
		int[] data;
		int head, tail;
		
		Queue(){
			data = new int[N];
			head = 0; 
			tail = N-1;
		}
		
		void add(int e) {
			tail = (tail+1)%N;
			data[tail] =e;
			
			
		};
		void remove() {
			head = (head+1) %N;
		};
		int peek() {
			
			return data[head];};	
}

public class Main {
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner scan = new Scanner(System.in);
		Queue queue = new Queue();

		while(true) {
			int v =scan.nextInt();
			if(v==-1) break;
			if(v == 0) {
				System.out.println(queue.peek());
				queue.remove();
			}
			else queue.add(v);
		}	
	}

}
