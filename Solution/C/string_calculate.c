#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#define MAXSTACK 100
char stack[MAXSTACK] = {'\0'};
char postfix[MAXSTACK] = {'\0'};
int postfix_size = -1;
int top = -1;
int isEmpty();
void push(char);
char pop();
char top_data();
int add(int, int);
int abs(int, int);
int mul(int, int);
int di(int, int);
int postfix_adj(char);
int priority(char);

int isEmpty(){
    if(top == -1){
        return 1;
    }else{
        return 0;
    }
}

void push(char data){
    stack[++top] = data;
}

char pop(){
    char data = stack[top];
    stack[top--] = '\0';
    return data;
}

char top_data(){
    return stack[top];
}

int add(int num1, int num2){
    return (num1 + num2);
}

int abs(int num1, int num2){
    return (num1 - num2);
}

int mul(int num1, int num2){
    return (num1 * num2);
}

int di(int num1, int num2){
    return (num1 / num2);
}

int priority(char op){
    switch (op)
    {
        case '+': case '-': return 1;
        case '*': case '/': return 2;
        default: return 0;
    }
}

void postfix_adj(char *infix){
    int cnt = -1;
    char num[MAXSTACK];
    for(int i = 0; i < strlen(infix); i++){
        char OP = infix[i];
        printf("OP:%c\n", OP);
        
        switch (OP)
        {
            case '(':
                push(OP);
                break;
            case ')':
                while(top_data() != '('){
                    postfix[++postfix_size] = pop();
                }
                pop();
                break;
            case '+': case '-':  case '*': case '/':
                postfix[++postfix_size] = '\'';
                if(priority(top_data()) > priority(OP)){
                    postfix[++postfix_size] = pop();
                }
                push(OP);
                break;
            default:
                postfix[++postfix_size] = OP;
        }
        printf("%s\n", stack);
        printf("%s\n\n", postfix);
    }
    if(!isEmpty()){
        postfix[++postfix_size] = pop();
    }
    printf("%s\n", stack);
    printf("%s\n\n", postfix);
}

int main(){
    // char pattern[200];
    // printf("Please input:");
    // scanf("%s", pattern);
    // postfix_adj(pattern);
    // int sum = 0;

    
    

    return 0;
}