/*** Definition section ***/
%option noyywrap
%{
#include <stdio.h>
int flag = 0;
%}

%%

[(] {flag = flag + 1;}
[)] {flag = flag -1;}
[a-zA-Z0-9+*-/]+ 
[\n] {
     if (flag==0){
        printf("Parenthesis has been closed properly.\n");
    }
    else{
        printf("Parenthesis hasn't been closed properly.\n");
    }
    if(flag>0){
        printf("The statement has extra parenthesis '(' or missing ')' parenthesis\n");
    }
    else if(flag<0)
    {
        printf("THe statement extra parenthesis ')' or missing '(' parenthesis\n");
    }
    flag = 0;
}

%%

/*** C Code section ***/
int main(void)
{
    printf("Enter a string bounded by parenthesis : ");
    yylex();
    return 0;
}

