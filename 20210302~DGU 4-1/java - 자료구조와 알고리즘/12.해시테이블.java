import java.util.*;

//key value ¦������ Ŭ����
class Pair<K,V>{
	public K first;
	public V second;
	//������! k��� �ڷ��� , v��� �ڷ����� �����Կ�
	Pair(K key, V value){
		first = key;
		second = value;
	}
}

class HashTable{
	Pair<Integer, Integer>[] table;   //�ؽ����̺� �迭
	int M;  // �ؽ����̺� ������ ����
	Pair<Integer, Integer> deleted;
	HashTable(int m){
		//�ؽ����̺� ������
		table = new Pair[m];
		M = m;
		deleted = new Pair(null, 0);
	}
	//hash ������ ������
	int hash(Integer key){
		int h = key.hashCode() & 0x7fffffff; 
		//�� �տ��ִ� sign ��Ʈ�� 0���� ���༭ ���������
		return h%M;
	}
	int hash2(Integer key) {
		int h = key.hashCode() & 0x7fffffff; 
		return 7-(h%7);
	}
	
	//key���� ���� value ���� �����ϱ� ���� �Լ�
	void put(Integer key, int value){
		int h = hash(key), step =hash2(key);
		while(table[h] != null) {
			if (table[h] == deleted) break;
			h = (h+step)%M;
			
			System.out.println("collision: "+key);
		}
		table[h] = new Pair(key, value);
	}
	//key ���� ���� ���� �����Ѵٸ� �� ��ȯ, �׷��� ������ null ��ȯ
	Integer get(Integer key) {
		int h = hash(key), step =hash2(key);
		while(table[h] != null) {
			if(key.equals(table[h].first)) return table[h].second;
			
			h = (h+step) %M;
			
			
		}
		return null;
	}
	//key�� ���� �׸� ����
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
	//�ش� key���� ���� value�� �����ϴ��� �˻�
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


