%option noyywrap
%{
	/*To find whether given letter is a vowel or not*/
	void display(int);
%}

%%

[a|e|i|o|u|] {
		int flag=1;
		display(flag);
		return 1;
		}

.+ {
	int flag=0;
	display(flag);
	return 0;
	}
	
%%
void display(int flag)
{
	if(flag==1)
		printf("The given letter [%s] is a vowel\n",yytext);
	else
		printf("The given letter [%s] is NOT a vowel\n",yytext);		
}

void main()
{
	printf("Enter a letter to check if it is a vowel or not : ");
	yylex(); 
}