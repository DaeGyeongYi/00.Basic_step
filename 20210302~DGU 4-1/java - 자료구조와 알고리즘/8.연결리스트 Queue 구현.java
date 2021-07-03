import java.util.Scanner;

class Node {
	public Node prev, next;
	public int data;
	Node(int e){ data = e; prev = next = this;}
}


class Queue {
	Node root;
	Queue(){
		root = new Node(0);
		}
		
		void add(int e) {
			Node node = new Node(e);
			node.next = root;
			node.prev = root.prev;
			root.prev.next = node;
			root.prev = node;
		};
		void remove() {
			Node node = root.next;
			node.next.prev = root;
			root.next = node.next;
		};
		int peek() {
			
			return root.next.data;
}
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
