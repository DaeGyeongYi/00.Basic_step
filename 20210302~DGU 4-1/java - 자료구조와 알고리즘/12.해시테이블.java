import java.util.*;

//key value 짝지어줄 클래스
class Pair<K,V>{
	public K first;
	public V second;
	//생성자! k라는 자료형 , v라는 자료형을 받을게요
	Pair(K key, V value){
		first = key;
		second = value;
	}
}

class HashTable{
	Pair<Integer, Integer>[] table;   //해시테이블 배열
	int M;  // 해시테이블 사이즈 지정
	Pair<Integer, Integer> deleted;
	HashTable(int m){
		//해시테이블 생성자
		table = new Pair[m];
		M = m;
		deleted = new Pair(null, 0);
	}
	//hash 값으로 뭉개기
	int hash(Integer key){
		int h = key.hashCode() & 0x7fffffff; 
		//맨 앞에있는 sign 비트를 0으로 해줘서 양수만나옴
		return h%M;
	}
	int hash2(Integer key) {
		int h = key.hashCode() & 0x7fffffff; 
		return 7-(h%7);
	}
	
	//key값을 가진 value 값을 저장하기 위한 함수
	void put(Integer key, int value){
		int h = hash(key), step =hash2(key);
		while(table[h] != null) {
			if (table[h] == deleted) break;
			h = (h+step)%M;
			
			System.out.println("collision: "+key);
		}
		table[h] = new Pair(key, value);
	}
	//key 값을 가진 것이 존재한다면 값 반환, 그렇지 않으면 null 반환
	Integer get(Integer key) {
		int h = hash(key), step =hash2(key);
		while(table[h] != null) {
			if(key.equals(table[h].first)) return table[h].second;
			
			h = (h+step) %M;
			
			
		}
		return null;
	}
	//key값 가진 항목 삭제
	void remove(Integer key) {
		int h = hash(key), step = hash2(key);
		while(table[h] != null) {
			if(key.equals(table[h].first)) {
				table[h] = deleted;
				return;
			}
			h = (h+step) %M;
		}
	}
	//해당 key값을 가진 value가 존재하는지 검사
	boolean contains(Integer key) {
		int h = hash(key),step=hash2(key);
		while(table[h] != null) {
			if(key.equals(table[h].first)) return true;
			h = (h+step) % M;
		}
		return false;
	}
	
	void hashshow() {
		Integer i;
		for(i=0; i<M; i++) { 
			i = i.hashCode() & 0x7fffffff ;
			System.out.println(table[i]);
		}
	}
	
}


public class Main {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner scan = new Scanner(System.in);
		HashTable map = new HashTable(11);
		map.put(21,21);
		map.put(65,65);
		map.put(75,75);
		map.put(40,40);
		map.put(43,43);
		map.put(74,74);
		map.put(18,18);
		map.hashshow();
		//System.out.println("one is "+map.get("one"));
		//System.out.println("five is "+(map.contains("five")? "":"not ")+"in map");
		while(true) {

		
			System.out.println("ht > ");
			String cmd = scan.next();
			if(cmd.equals("quit")) break;
			if(cmd.equals("add")) {
				int key = scan.nextInt();
				int value = scan.nextInt();
				map.put(key, value);
			}
			else if(cmd.equals("find")) {
				int key = scan.nextInt();
				Integer value = map.get(key);
				if(value == null)
					System.out.println(key+" is not found.");
				else System.out.println("Value for "+key+" is "+ value+".");
				
				System.out.println(map.table[key]);
			}
			else if(cmd.equals("remove")) {
				int key = scan.nextInt();
				map.remove(key);
				}
			
			
		
		}
		
		
		}
	}


