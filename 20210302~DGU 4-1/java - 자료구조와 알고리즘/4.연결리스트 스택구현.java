import java.util.Scanner;
class Node {
	public int data;
	public Node next;
	Node(int e) { data = e; next =null;}
}
// head에서 가장 첫번째 노드를 참조하고 있어야함. 
class Stack {
	Node head;

	Stack(){
		head = null; // 사실 상 top과 같은 역할 
	}
	void push(int e) {
		Node node = new Node(e);
		// e라는 데이터를 담고있는 노드생성
		node.next = head;
		// 새로운 노드의 next(다음 노드를 가리키는 포인터)에 head가 가리키던 곳의 값을 입력
		head = node; // head는 이제 새로 생성된 노드를 가리킴
	}
	void pop () {
		head = head.next;
	}
	int top() {
		return head.data;
	}
	
	boolean empty() {
		return head == null;
	}
	
}
	
	
public class Main {
	public static void main(String[] args) {
		Stack stack = new Stack();
		stack.push(30);
		stack.push(20);
		stack.push(10);
		System.out.print("top-> ");
		for(int i =0; i<3; i++) {
			System.out.print(stack.top()+" ");
		}
		stack.pop();
		stack.pop();
		System.out.print("top-> ");
		while(stack.empty()==true) {
			System.out.print(stack.top());
		}
	}

}
