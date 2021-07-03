import java.util.Random;
import java.util.Scanner;
public class Main {

	static void insertionSort(int[] v, int n) {
		for(int i = 1; i<n; i++) {
			int t = v[i],last = i-1;
			while(last >= 0 && v[last] > t) {
				v[last+1]= v[last];
				last--;
			}
			v[last+1] = t;
		}
	}
	
	
	//��������
	static void selectionSort(int[]v, int from, int to) {
		for(int i=from; i<to; i++) {
			int indexofmin = i;// �������� ���� �����ִ� ����Ű�� ����
			//�ϴ� i�� min���� ������
			for(int j = i+1; j<=to; j++) {
				if(v[j]< v[indexofmin]) indexofmin = j;
			}
			//��¥ min���� �´��� if���� ���� ����
			int tmp = v[i];
			v[i] =v[indexofmin];
			v[indexofmin] =tmp;
			//��¥ min���� ��ȯ���� �̷��� �� �տ������� ���İ���
		}	
	}
	
	static void selectionSort(int[] v, int n) {
		selectionSort(v,0,n-1);
	}
	
	
	
	
	//�պ�����
	static int[] t; // ���ĵ� �͵��� ���ٳ��� �迭 �غ�
	static void mergeSort(int[] v, int from, int to) {
		// ����Լ��� Ż������
		//void�Լ����� return; ���ִϱ� �׳� ����.
		if (from == to) return; 
		int center = (from+to)/2;// ������ ������ �� �߰� index��ġ
		mergeSort(v,from,center); // ������ ���� �κ�
		mergeSort(v,center+1,to); // ������ ������ �κ�
		
		int i = from; // ���� �丷�� ù���� �ε���
		int j=center+1;//���� �丷�� ù��° �ε���, 
		int k=from;
		
		while(i<=center && j <=to) {
			if(v[i] <= v[j]) t[k++] = v[i++];
			else t[k++] = v[j++]; //�� �������� t[]�迭�� �����ϸ�, �ε����� ����Ű�� ������ �÷���
		}
		while(i<=center) {
			t[k++] = v[i++];
			
		}
		while(j<=to) {
			t[k++]=v[j++];
		}
		// v�迭���ٰ� ���Ľ��ѳ��� t�迭�� ������
		for(i = from; i<=to; i++) v[i] = t[i];	
	}
	
	static void mergeSort(int[] v, int n) {
		t= new int[n];
		mergeSort(v,0, n-1);
		t = null;
	}
	
	
	public static void main(String[] args) {
	Random rand = new Random(100);
	Scanner scan = new Scanner(System.in);

	int n = scan.nextInt();
	int[] v = new int[n];
	long ts = System.currentTimeMillis();
	
	for(int i = 0; i<n; i++) {
		v[i] = rand.nextInt(100);
	}
	mergeSort(v,n);
	ts =  System.currentTimeMillis() - ts;
	for (int i = 0; i<10; i++) System.out.println(v[i]);
	System.out.println("Elapsed time is "+ts+"ms.");
}
}