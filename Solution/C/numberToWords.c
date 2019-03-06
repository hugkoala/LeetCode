void helper(int a, char* result) {
    const char *one_arr[12] = {"\0","One","Two","Three","Four","Five","Six","Seven","Eight","Nine"};
    const char *ten_arr[12] = {"\0","Ten","Twenty","Thirty","Forty","Fifty","Sixty","Seventy","Eighty","Ninety"};
    const char *oneten_arr[12] = {"\0","Eleven","Twelve","Thirteen","Fourteen","Fifteen","Sixteen","Seventeen","Eighteen","Nineteen"};
    // char* result[200] = {"\0"};
    
    int num = 0;
    if(a / 100 > 0) {
        num = a / 100;
        sprintf(result, strcat(result, one_arr[num]));
        if (a % 100 == 0) {
            sprintf(result, strcat(result, " Hundred"));
        } else {
            sprintf(result, strcat(result, " Hundred "));    
        }
        
        a %= 100;
    }
    if(a > 10 && a < 20) {
        sprintf(result, strcat(result, oneten_arr[a % 10]));
    } else if(a < 10) {
        sprintf(result, strcat(result, one_arr[a]));
    } else {
        num = a / 10;
        int num1 = a % 10;
        if(num1 == 0) {
            sprintf(result, "%s%s", result, ten_arr[num]);
        } else {
            sprintf(result, "%s%s %s", result, ten_arr[num], one_arr[num1]);   
        }
    }
    
    // printf("%s \n", result);
    
    // return result;
}

char* numberToWords(int num) {
    if(num == 0) {
        return "Zero";
    }
    char* a = calloc(200, sizeof(char));
    int ss[4] = {0};
    
    for(int i = 0; i < 4; i++) {
        if(num % 1000 > 0) {
            ss[i] = num % 1000;
        }
        num /= 1000;
    }

    if(ss[3] != 0) {
        helper(ss[3], a);
        if(ss[2] != 0 || ss[1] != 0 || ss[0] != 0) {
            sprintf(a, strcat(a, " Billion "));    
        } else {
            sprintf(a, strcat(a, " Billion"));
        }
        
    }
    if(ss[2] != 0) {
        helper(ss[2], a);
        if(ss[1] != 0 || ss[0] != 0) {
            sprintf(a, strcat(a, " Million "));
        } else {
            sprintf(a, strcat(a, " Million"));
        }
        
    }
    if(ss[1] != 0) {
        helper(ss[1], a);
        if(ss[0] != 0) {
            sprintf(a, strcat(a, " Thousand "));    
        } else {
            sprintf(a, strcat(a, " Thousand"));    
        }
        
    }
    if(ss[0] != 0) {
        helper(ss[0], a);  
    }
    return a;
    
}


