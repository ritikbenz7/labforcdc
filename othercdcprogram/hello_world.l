%option noyywrap
%{
	#include <stdio.h>
%}

%%
[\n] {
	printf("Hello World\n");	
}	
%%
//code prints hello world when enter key is pressed
int main(){ 
yylex();
return 0;
}