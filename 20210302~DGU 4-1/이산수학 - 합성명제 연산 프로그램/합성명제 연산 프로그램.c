#include <stdio.h>
#include <string.h>
int negation(char a, char* result);
int disjunction(char a, char b, char* result);
int conjunction(char a, char b, char* result);
int implication(char a, char b, char* result);
void operation(char oper);
void truthValue(char a, char* cons);

void push(void);
void pop(void);
void display(void);

char stackProp[100], stackOper[100];  //���� ����, ������ ����
int  topProp, topOper;

int choice, n, x, i;

char  inputProp[80] = "PvQ^~R=P>Q^R@Q";  // �ռ����� Ű���� �Է¹��� ����


topProp = -1; 
topOper = -1;
//������ �켱���� ǥ�� �迭�� �ۼ�
char priorityOper[7][7] = { {' ','~','^','>','v','@','='},
                            {'~','<','>','>','>','>','>'},
                            {'^','<','>','>','>','>','>'},
                            {'>','<','<','>','>','<','>'},
                            {'v','<','<','>','>','<','>'}, 
                            {'@','<','>','>','>','>','>'},
                            {'=','<','<','<','<','<','>'}};



int main(void)
{
    printf("������� 2015112741 �̴��");
    //1. �ռ����� Ű���� �Է�
    //printf(" �ռ����� �Է�: ");
    //scanf("%s", inputProp); 
    //getchar(); // ����Ű ó�� �ڵ�
    
    


    //2. �ռ����� �и��ؼ� ���
    for (i = 0; i < strlen(inputProp); i++) {
        printf("%c\n", inputProp[i]);

        //3. ���� üũ�ؼ� ���ÿ� Push
        if (inputProp[i] == 'P' || inputProp[i] == 'p' ||
            inputProp[i] == 'Q' || inputProp[i] == 'q' ||
            inputProp[i] == 'R' || inputProp[i] == 'r') {

            topProp++;
            stackProp[topProp] = inputProp[i];  //���� ���� push
            printf("���� ���ÿ� %c  push �Ϸ� \n\n", inputProp[i]);
            display();

        }  //end if

          //������ üũ�ؼ� ������ ���ÿ� push
        if (inputProp[i] == '^' || inputProp[i] == 'v' ||
            inputProp[i] == '~' || inputProp[i] == '=' ||
            inputProp[i] == '>' || inputProp[i] == '@') {


            //������ ������ ����ִ��� üũ!
            if (topOper == -1) {//������ ������ ����ִ°��
                topOper++;
                stackOper[topOper] = inputProp[i];  //�����ڽ��� push
                printf("������ ���ÿ� %c  push �Ϸ� \n\n", inputProp[i]);
                display();
            }
            else {
                //������ ������ ������� ���� ���
                //������ �켱����ǥ�� Ȯ���ؼ� �Է��� �켱������ ũ��('<') �׳� push
                //������ ���ó��� �����ڰ� �켱������ ũ��('>')�ٸ� �۾��� �ʿ���.
                int row, find_row, col, find_col;

                //�Էµ� �����ڰ� ������ �켱����ǥ ��� �ִ� �� ã��(��)
                for (row = 1; row < 7; row++) {
                    if (inputProp[i] == priorityOper[0][row]) {
                        find_row = row;
                        break;
                    }
                }
                //�����ڽ��ÿ� �ִ� �����ڰ� ������ �켱����ǥ ��� �ִ��� ã��(��)
                for (col = 1; col < 7; col++) {
                    if (stackOper[topOper] == priorityOper[col][0]) {
                        find_col = col;
                        break;
                    }
                }
                //priorityOper[find_col][find_row]�� ���� �� �������� �켱������ ������
                printf("%c, %c �켱������ '%c'�Դϴ�.\n",stackOper[topOper],inputProp[i], priorityOper[find_col][find_row]);

                if (priorityOper[find_col][find_row] == '<') {
                    topOper++;
                    stackOper[topOper] = inputProp[i];  //�����ڽ��� push
                    printf("������ ���ÿ� %c  push �Ϸ� \n\n", inputProp[i]);
                    display();
                }
                else {//�켱������ >�ΰ��
                    //������ ���ÿ��� POP
                    char oper;
                    oper = stackOper[topOper];
                    topOper--;
                    printf("������ ���ÿ��� pop�� �����ڴ� %c �Դϴ�\n", oper);
                    display();

                    //�켱������ ���� �����ڴ� ������ ���ÿ� PUSH
                    topOper++;
                    stackOper[topOper] = inputProp[i];  //�����ڽ��� push
                    printf("������ ���ÿ� %c push �Ϸ� \n\n", inputProp[i]);
                    display();

                    //�����ڰ� ���׿�����, ���׿����� üũ
                    // ~: ���׿�����
                    // ���׿������̸� �������ÿ��� 1��POP, \�����̸� 2�� POP
                    operation(oper);
                }
            }
        }  //end if

    }//END FOR
    while (1) {
        //1.������ ������ ����ִ��� üũ
        if (topOper == -1) {
            printf("������ ������ ����ֽ��ϴ�. \n");
            //���� ����� �������ÿ� ����ִ�.
            //�������ÿ��� pop�Ѵ�.

            char prop;
            prop = stackProp[topProp];
            topProp--;

            printf("�ռ����� %s �� �������� ==> %c �Դϴ�. \n", inputProp, prop);
            
            break;
        }
        else {//������ ������ ������� ������ ��� ��������.
            char oper;
            oper = stackOper[topOper];
            topOper--;

            // ���׿������̸� �������ÿ��� 1��POP, \�����̸� 2�� POP
            operation(oper);
        }
    }//end while


    return 0;
}


void operation(char oper) {
    if (oper == '~') {//���� ������
        printf("%c�� ���׿������Դϴ�.\n", oper);

        char prop;
        prop = stackProp[topProp];
        topProp--;

        printf("�������ÿ��� pop�� ������ %c �Դϴ� \n", prop);
        display();

        //~ ����
        char result, cons;
        //P,Q,R �����̸� TRUTH VALUE �� T
        truthValue(prop, &cons);

        negation('T', &result);
        printf("~%c ==> %c \n", prop, result);
        //���� ����� ���� STACK�� PUSH
        topProp++;
        stackProp[topProp] = result;  //�����ڽ��� push
        printf("�������ÿ� %c  push �Ϸ� \n\n", result);
        display();

    }
    else { //���׿�����
        printf("%c�� ���׿������Դϴ�.\n", oper);

        char prop1, prop2;
        prop2 = stackProp[topProp];
        topProp--;
        prop1 = stackProp[topProp];
        topProp--;

        printf("�������ÿ��� pop�� ������ %c, %c �Դϴ� \n", prop1, prop2);
        display();


        char result, cons1, cons2;
        if (oper == '^') {
            truthValue(prop1, &cons1);
            truthValue(prop2, &cons2);

            conjunction(cons1, cons2, &result);

            printf("%c ^ %c ==> %c \n", prop1, prop2, result);
        }

        else if (oper == 'v') {
            truthValue(prop1, &cons1);
            truthValue(prop2, &cons2);

            disjunction(cons1, cons2, &result);

            printf("%c v %c ==> %c \n", prop1, prop2, result);
        }
        else if (oper == '>') {
            truthValue(prop1, &cons1);
            truthValue(prop2, &cons2);

            implication(cons1, cons2, &result);

            printf("%c > %c ==> %c \n", prop1, prop2, result);
        }
        else if (oper == '@') {
            truthValue(prop1, &cons1);
            truthValue(prop2, &cons2);

            xor(cons1, cons2, &result);

            printf("%c > %c ==> %c \n", prop1, prop2, result);

        }

        else if (oper == '=') {
            truthValue(prop1, &cons1);
            truthValue(prop2, &cons2);

            equv(cons1, cons2, &result);

            printf("%c > %c ==> %c \n", prop1, prop2, result);

        }

        //���� ����� ���� STACK�� PUSH
        topProp++;
        stackProp[topProp] = result;  //�����ڽ��� push
        printf("�������ÿ� %c  push �Ϸ� \n\n", result);
        display();
    }
}

int negation(char a, char* result) {
    
    if (a == 'T' || a == 't') {
        *result = 'F';
    }
    else {
        *result = 'T';
    }
    return 0;
}

int disjunction(char a, char b, char* result) {
    if ((a == 'F' || a == 'f') && (b== 'F' || b == 'f')){
        *result = 'F';
    }
    else {
        *result = 'T';
    }
    return 0;
}





int conjunction(char a, char b, char* result) {
    if ((a == 'T' || a == 't') && (b == 'T' || b == 't')) {
        *result = 'T';
    }
    else {
        *result = 'F';
    }
    return 0;

}

int implication(char a, char b, char* result) {
    if ((a == 'T' || a == 't') && (b == 'F' || b == 'f')) {
        *result = 'F';
    }
    else {
        *result = 'T';
    }
    return 0;
}

int xor(char a, char b, char* result) {
    if ((a == 'T' || a == 't') && (b == 'T' || b == 't')) {
        *result = 'F';
    }
    else {
        *result = 'T';
    }
    return 0;
}

int equv(char a, char b, char* result) {
    if ((a == 'T' || a == 't') && (b == 'F' || b == 'f')) {
        *result = 'T';
    }
    else {
        *result = 'F';
    }
    return 0;
}



void push(void)  // �������� ���������� üũ�ؼ� ���ÿ� Push
{
    if (topProp >= n - 1)
    {
        //printf("\n\tSTACK is over flow");
        printf("\n\tSTACK �����÷ο�");

    }
    else
    {
        //for (int i = 0; i < strlen(inputProp); i++) {
        //    printf("inputProp[%d] = %c \n", i, inputProp[i]);  //�ռ����� �и� ���


            //�����̸� ���� ���ÿ� push
        if (inputProp[i] == 'P' || inputProp[i] == 'p' ||
            inputProp[i] == 'Q' || inputProp[i] == 'q' ||
            inputProp[i] == 'R' || inputProp[i] == 'r') {

            topProp++;
            stackProp[topProp] = inputProp[i];  //���� ���� push
            printf("���� ���ÿ� push �Ϸ� \n\n");

        }  //end if



       //������ �̸� ������ ���ÿ� push
        if (inputProp[i] == '^' || inputProp[i] == 'v' ||
            inputProp[i] == '~' || inputProp[i] == '=' ||
            inputProp[i] == '>' || inputProp[i] == '@') {

            topOper++;
            stackOper[topOper] = inputProp[i];  //�����ڽ��� push
            printf("������ ���ÿ� push �Ϸ� \n\n");

        }  //end if




   // }  // end for
    //printf(" Enter a value to be pushed:");

    //printf(" PUSH�� ����Ÿ �Է�: ");
    //scanf("%d", &x);  //���� �Է�

   // top++;   //�߿��ϴ�. ���ÿ� top = top +1

    //stack[top] = x;
    }
}

void pop()   // ���ÿ��� ���
{
    if (topProp <= -1)
    {
        //printf("\n\t Stack is under flow");
        printf("\n\t Stack ����÷ο�");
    }
    else
    {
        //printf("\n\t The popped elements is %d", stack[top]);
        //   top--;  //���ÿ��� pop�ϸ� top = top -1
    }
}

void display()
{
    printf("-------------------------------------------");
    //���� ���� ���
    if (topProp >= 0)
    {
        printf("\n 1: ���� STACK: ");
        for (int i = 0; i <=topProp; i++)
            printf(" %c", stackProp[i]);
        printf("\n");
    }
    else
    {
        //printf("\n The STACK is empty");
        printf("\n 1:���� STACK�� ����ִ�");
    }
    //������ ���� ���
    if (topOper >= 0)
    {
        printf("\n 2: ������ STACK: ");
        for (int i = 0; i <= topOper; i++)
            printf(" %c", stackOper[i]);
        printf("\n");
    }
    else
    {
        //printf("\n The STACK is empty");
        printf("\n 2: ������ STACK�� ����ִ�\n");
    }
    printf("-------------------------------------------\n");


}



void truthValue(char a, char* cons) {
    if (a == 'P' || a == 'p' || a == 'R' || a == 'r') { *cons = 'T'; }
    else if (a == 'Q' || a == 'q') { *cons = 'F'; }
    else { *cons = a; }
}