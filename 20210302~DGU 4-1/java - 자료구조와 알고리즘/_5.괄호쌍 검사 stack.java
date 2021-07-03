import java.util.*;
public class Main {
	static boolean check(String str) {
		char[] stack = new char[100];
		int top = -1;	
		for (int i = 0; i<str.length(); i++) {
			char c = str.charAt(i);
			if(c=='(' || c == '{' || c =='[') {
				stack[++top]= c;
			}
			else if (c==')' || c=='}'|| c==']') {
				if(top ==-1) return false;
				char v = stack[top--];
				if (c == ')' && v != '(') return false;
				if (c == '}' && v != '{') return false;
				if (c == ']' && v != '[') return false;
			}
		}
		return top == -1;
	}
	public static void main(String[] args) {
		Scanner scan = new Scanner(System.in);
		String str = "{((2+3)/(3-1)}+{3*(5-4)}";
		//String formula="{((2+3)/(3-1)}+{3*(5-4)}";
		//String formula="{((2+3)/(3-1)}+{3*(5-4)}";
		//String formula="{({(2+3)/(3-1)}+{3*(5-4)}";
		if(check(str)) {
			System.out.println("¼º°ø");
		}
		else {
			System.out.println("no");
		}
	}
}
