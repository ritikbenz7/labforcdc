/*** Definition section ***/
%option noyywrap
%{
    #include <stdio.h>
    void display(int);
%}

%%
[A-Za-z]* {
    int flag=1;
		display(flag);
		return 1;
}
[0-9]* {int flag=0;
	display(flag);
	return 0;
    }

%%

/*** C Code section ***/
void display(int flag)
{
	if(flag==1)
		printf("The given character [%s] is alphabet\n",yytext);
	else
		printf("The given character [%s] is digit\n",yytext);		
}
int main(void)
{
    printf("Enter a character : ");
    yylex();
    return 0;
}