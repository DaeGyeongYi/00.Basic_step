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

char stackProp[100], stackOper[100];  //명제 스택, 연산자 스택
int  topProp, topOper;

int choice, n, x, i;

char  inputProp[80] = "PvQ^~R=P>Q^R@Q";  // 합성명제 키보드 입력받을 변수


topProp = -1; 
topOper = -1;
//연산자 우선순위 표를 배열로 작성
char priorityOper[7][7] = { {' ','~','^','>','v','@','='},
                            {'~','<','>','>','>','>','>'},
                            {'^','<','>','>','>','>','>'},
                            {'>','<','<','>','>','<','>'},
                            {'v','<','<','>','>','<','>'}, 
                            {'@','<','>','>','>','>','>'},
                            {'=','<','<','<','<','<','>'}};



int main(void)
{
    printf("국어교육과 2015112741 이대경");
    //1. 합성명제 키보드 입력
    //printf(" 합성명제 입력: ");
    //scanf("%s", inputProp); 
    //getchar(); // 엔터키 처리 코드
    
    


    //2. 합성명제 분리해서 출력
    for (i = 0; i < strlen(inputProp); i++) {
        printf("%c\n", inputProp[i]);

        //3. 명제 체크해서 스택에 Push
        if (inputProp[i] == 'P' || inputProp[i] == 'p' ||
            inputProp[i] == 'Q' || inputProp[i] == 'q' ||
            inputProp[i] == 'R' || inputProp[i] == 'r') {

            topProp++;
            stackProp[topProp] = inputProp[i];  //명제 스택 push
            printf("명제 스택에 %c  push 완료 \n\n", inputProp[i]);
            display();

        }  //end if

          //연산자 체크해서 연산자 스택에 push
        if (inputProp[i] == '^' || inputProp[i] == 'v' ||
            inputProp[i] == '~' || inputProp[i] == '=' ||
            inputProp[i] == '>' || inputProp[i] == '@') {


            //연산자 스택이 비어있는지 체크!
            if (topOper == -1) {//연산자 스택이 비어있는경우
                topOper++;
                stackOper[topOper] = inputProp[i];  //연산자스택 push
                printf("연산자 스택에 %c  push 완료 \n\n", inputProp[i]);
                display();
            }
            else {
                //연산자 스택이 비어있지 않은 경우
                //연산자 우선순위표를 확인해서 입력이 우선순위가 크면('<') 그냥 push
                //연산자 스택내의 연산자가 우선순위가 크면('>')다른 작업이 필요함.
                int row, find_row, col, find_col;

                //입력된 연산자가 연산자 우선순위표 어디에 있는 지 찾기(열)
                for (row = 1; row < 7; row++) {
                    if (inputProp[i] == priorityOper[0][row]) {
                        find_row = row;
                        break;
                    }
                }
                //연산자스택에 있는 연산자가 연산자 우선순위표 어디에 있는지 찾기(행)
                for (col = 1; col < 7; col++) {
                    if (stackOper[topOper] == priorityOper[col][0]) {
                        find_col = col;
                        break;
                    }
                }
                //priorityOper[find_col][find_row]의 값이 두 연산자의 우선순위를 보여줌
                printf("%c, %c 우선순위는 '%c'입니다.\n",stackOper[topOper],inputProp[i], priorityOper[find_col][find_row]);

                if (priorityOper[find_col][find_row] == '<') {
                    topOper++;
                    stackOper[topOper] = inputProp[i];  //연산자스택 push
                    printf("연산자 스택에 %c  push 완료 \n\n", inputProp[i]);
                    display();
                }
                else {//우선순위가 >인경우
                    //연산자 스택에서 POP
                    char oper;
                    oper = stackOper[topOper];
                    topOper--;
                    printf("연산자 스택에서 pop한 연산자는 %c 입니다\n", oper);
                    display();

                    //우선순위가 낮은 연산자는 연산자 스택에 PUSH
                    topOper++;
                    stackOper[topOper] = inputProp[i];  //연산자스택 push
                    printf("연산자 스택에 %c push 완료 \n\n", inputProp[i]);
                    display();

                    //연산자가 단항연산자, 이항연산자 체크
                    // ~: 단항연산자
                    // 단항연산자이면 명제스택에서 1개POP, \이항이면 2개 POP
                    operation(oper);
                }
            }
        }  //end if

    }//END FOR
    while (1) {
        //1.연산자 스택이 비어있는지 체크
        if (topOper == -1) {
            printf("연산자 스택이 비어있습니다. \n");
            //연산 결과는 명제스택에 들어있다.
            //명제스택에서 pop한다.

            char prop;
            prop = stackProp[topProp];
            topProp--;

            printf("합성명제 %s 의 연산결과는 ==> %c 입니다. \n", inputProp, prop);
            
            break;
        }
        else {//연산자 스택이 비어있지 않으면 계속 연산진행.
            char oper;
            oper = stackOper[topOper];
            topOper--;

            // 단항연산자이면 명제스택에서 1개POP, \이항이면 2개 POP
            operation(oper);
        }
    }//end while


    return 0;
}


void operation(char oper) {
    if (oper == '~') {//단항 연산자
        printf("%c는 단항연산자입니다.\n", oper);

        char prop;
        prop = stackProp[topProp];
        topProp--;

        printf("명제스택에서 pop한 명제는 %c 입니다 \n", prop);
        display();

        //~ 연산
        char result, cons;
        //P,Q,R 명제이면 TRUTH VALUE 는 T
        truthValue(prop, &cons);

        negation('T', &result);
        printf("~%c ==> %c \n", prop, result);
        //연산 결과를 명제 STACK에 PUSH
        topProp++;
        stackProp[topProp] = result;  //연산자스택 push
        printf("명제스택에 %c  push 완료 \n\n", result);
        display();

    }
    else { //이항연산자
        printf("%c는 이항연산자입니다.\n", oper);

        char prop1, prop2;
        prop2 = stackProp[topProp];
        topProp--;
        prop1 = stackProp[topProp];
        topProp--;

        printf("명제스택에서 pop한 명제는 %c, %c 입니다 \n", prop1, prop2);
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

        //연산 결과를 명제 STACK에 PUSH
        topProp++;
        stackProp[topProp] = result;  //연산자스택 push
        printf("명제스택에 %c  push 완료 \n\n", result);
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



void push(void)  // 명제인지 연산자인지 체크해서 스택에 Push
{
    if (topProp >= n - 1)
    {
        //printf("\n\tSTACK is over flow");
        printf("\n\tSTACK 오버플로우");

    }
    else
    {
        //for (int i = 0; i < strlen(inputProp); i++) {
        //    printf("inputProp[%d] = %c \n", i, inputProp[i]);  //합성명제 분리 출력


            //명제이면 명제 스택에 push
        if (inputProp[i] == 'P' || inputProp[i] == 'p' ||
            inputProp[i] == 'Q' || inputProp[i] == 'q' ||
            inputProp[i] == 'R' || inputProp[i] == 'r') {

            topProp++;
            stackProp[topProp] = inputProp[i];  //명제 스택 push
            printf("명제 스택에 push 완료 \n\n");

        }  //end if



       //연산자 이면 연산자 스택에 push
        if (inputProp[i] == '^' || inputProp[i] == 'v' ||
            inputProp[i] == '~' || inputProp[i] == '=' ||
            inputProp[i] == '>' || inputProp[i] == '@') {

            topOper++;
            stackOper[topOper] = inputProp[i];  //연산자스택 push
            printf("연산자 스택에 push 완료 \n\n");

        }  //end if




   // }  // end for
    //printf(" Enter a value to be pushed:");

    //printf(" PUSH할 데이타 입력: ");
    //scanf("%d", &x);  //정수 입력

   // top++;   //중요하다. 스택에 top = top +1

    //stack[top] = x;
    }
}

void pop()   // 스택에서 출력
{
    if (topProp <= -1)
    {
        //printf("\n\t Stack is under flow");
        printf("\n\t Stack 언더플로우");
    }
    else
    {
        //printf("\n\t The popped elements is %d", stack[top]);
        //   top--;  //스택에서 pop하면 top = top -1
    }
}

void display()
{
    printf("-------------------------------------------");
    //명제 스택 출력
    if (topProp >= 0)
    {
        printf("\n 1: 명제 STACK: ");
        for (int i = 0; i <=topProp; i++)
            printf(" %c", stackProp[i]);
        printf("\n");
    }
    else
    {
        //printf("\n The STACK is empty");
        printf("\n 1:명제 STACK이 비어있다");
    }
    //연산자 스택 출력
    if (topOper >= 0)
    {
        printf("\n 2: 연산자 STACK: ");
        for (int i = 0; i <= topOper; i++)
            printf(" %c", stackOper[i]);
        printf("\n");
    }
    else
    {
        //printf("\n The STACK is empty");
        printf("\n 2: 연산자 STACK이 비어있다\n");
    }
    printf("-------------------------------------------\n");


}



void truthValue(char a, char* cons) {
    if (a == 'P' || a == 'p' || a == 'R' || a == 'r') { *cons = 'T'; }
    else if (a == 'Q' || a == 'q') { *cons = 'F'; }
    else { *cons = a; }
}