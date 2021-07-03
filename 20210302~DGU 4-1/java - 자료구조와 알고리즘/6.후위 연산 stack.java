
import java.util.*;
public class Main {
	static int error = -500;
	
	public static int postCalc(String expr) {
		int[]stack = new int[20];
		int top = -1;
		for(int i=0; i<expr.length();i++) {
			char c = expr.charAt(i);			
			
			if(c>='0' && c<='9') {
				stack[++top] = c -'0';
			}
			else if(c == '+' || c=='-' || c=='*' || c == '/') {
				if(top <1) return error;
				int b= stack[top--];
				int a = stack[top--];
				int r = error;
				
				if(c=='+') r =a+b;
				else if(c=='-') r=a-b;
				else if(c == '*') r=a*b;
				else r=a/b;
				
				stack[++top] = r;
			}
		}
		return top ==0? stack[top]:error;
	}
		
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner sc = new Scanner(System.in);
		String expr = sc.next();
		int r = postCalc(expr);
		System.out.println(expr + "="+r );
		
		
		
		
	}

}