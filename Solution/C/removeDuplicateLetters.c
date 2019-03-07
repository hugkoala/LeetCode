#define MAXSTACK 1000
char stack[MAXSTACK] = {'\0'};

int top = -1;
int isEmpty();
void push(char);
char pop();
char top_data();

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

char* removeDuplicateLetters(char* s) {
    while(!isEmpty()){
        pop();
    }
    int count[26] = {0};
    int visited[26] = {0};
    for(int i = 0; i < strlen(s); i++){
        if(s[i] == '\0'){
            break;
        }
        int num = 0;
        num = (int)s[i] - (int)'a';
        ++count[num];
    }

    for(int i = 0; i < strlen(s); i++){
        if(s[i] == '\0'){
            break;
        }
        int num = 0;
        num = (int)s[i] - (int)'a';

        --count[num];
        if(visited[num] == 1){
            continue;
        }
        while(!isEmpty() && count[((int)top_data() - (int)'a')] > 0 && num < ((int)top_data() - (int)'a')){
            visited[((int)top_data() - (int)'a')] = 0;
            pop();
        }
        push(s[i]);
        visited[num] = 1;
    }
    return stack;
}