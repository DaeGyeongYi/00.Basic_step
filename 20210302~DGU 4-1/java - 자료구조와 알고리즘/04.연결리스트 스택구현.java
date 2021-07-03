import java.util.Scanner;
class Node {
	public int data;
	public Node next;
	Node(int e) { data = e; next =null;}
}
// head���� ���� ù��° ��带 �����ϰ� �־����. 
class Stack {
	Node head;

	Stack(){
		head = null; // ��� �� top�� ���� ���� 
	}
	void push(int e) {
		Node node = new Node(e);
		// e��� �����͸� ����ִ� ������
		node.next = head;
		// ���ο� ����� next(���� ��带 ����Ű�� ������)�� head�� ����Ű�� ���� ���� �Է�
		head = node; // head�� ���� ���� ������ ��带 ����Ŵ
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
