/*** Definition section ***/
%option noyywrap
%{
    #include <stdio.h>
    int count = 0;
%}

%%
. {
    count = count + 1;
}

\n {
    printf("The number of character in the given line is %d",count);
}
%%

/*** C Code section ***/
int main(void)
{
    yylex();
    return 0;
}