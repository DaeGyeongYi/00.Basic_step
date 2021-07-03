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
	
	
	//선택정렬
	static void selectionSort(int[]v, int from, int to) {
		for(int i=from; i<to; i++) {
			int indexofmin = i;// 가장작은 값을 갖고있는 가리키는 변수
			//일단 i를 min으로 설정함
			for(int j = i+1; j<=to; j++) {
				if(v[j]< v[indexofmin]) indexofmin = j;
			}
			//진짜 min값이 맞는지 if문을 통해 검증
			int tmp = v[i];
			v[i] =v[indexofmin];
			v[indexofmin] =tmp;
			//진짜 min값과 교환해줌 이러면 맨 앞에서부터 정렬가능
		}	
	}
	
	static void selectionSort(int[] v, int n) {
		selectionSort(v,0,n-1);
	}
	
	
	
	
	//합병정렬
	static int[] t; // 정렬된 것들을 갖다놓을 배열 준비
	static void mergeSort(int[] v, int from, int to) {
		// 재귀함수의 탈출조건
		//void함수에서 return; 해주니까 그냥 끝남.
		if (from == to) return; 
		int center = (from+to)/2;// 나누는 기준이 될 중간 index위치
		mergeSort(v,from,center); // 기준의 왼쪽 부분
		mergeSort(v,center+1,to); // 기준의 오른쪽 부분
		
		int i = from; // 앞쪽 토막의 첫번쨰 인덱스
		int j=center+1;//뒤쪽 토막의 첫번째 인덱스, 
		int k=from;
		
		while(i<=center && j <=to) {
			if(v[i] <= v[j]) t[k++] = v[i++];
			else t[k++] = v[j++]; //더 작은쪽은 t[]배열에 복사하며, 인덱스를 가리키는 변수를 늘려줌
		}
		while(i<=center) {
			t[k++] = v[i++];
			
		}
		while(j<=to) {
			t[k++]=v[j++];
		}
		// v배열에다가 정렬시켜놓은 t배열을 복사함
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