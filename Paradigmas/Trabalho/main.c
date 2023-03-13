#include <stdio.h>
#include <stdlib.h>
#include <locale.h>

#define MAX_LENGTH 100
#define TAMANHO 5

int main(int argc, char *argv[]) {
	setlocale(LC_ALL, "portuguese");
	getchar();
	printf("\n//====//====/1/====//====//\n");
	exercicio1();
	getchar();
	printf("\n//====//====/2/====//====//\n");
	exercicio2();
	getchar();
	printf("\n//====//====/3/====//====//\n");
	exercicio3();
	getchar();
	printf("\n//====//====/4/====//====//\n");
	exercicio4();
	getchar();
	printf("\n//====//====/5/====//====//\n");
	exercicio5();
	getchar();
	printf("\n//====//====/6/====//====//\n");
	exercicio6();
	getchar();
	printf("\n//====//====/7/====//====//\n");
	exercicio7();
	getchar();
	printf("\n//====//====/8/====//====//\n");
	exercicio8();
	getchar();
	getchar();
	printf("\n//====//====/9/====//====//\n");
	exercicio9();
	getchar();
	printf("\n//====//====/10/====//====//\n");
	exercicio10();
	getchar();
	return 0;
}

void exercicio1() {
	int num = 10;
	int *ptr = &num;
	
	printf("O valor inicial de num é: %d\n", num);
	
	*ptr = 20;
	
	printf("O novo valor de num, alterado via ponteiro é: %d\n", num);
}

void exercicio2() {
	char c = 'a';
	char *ptr = &c;
	
	printf("O valor inicial de c é: %c\n", c);
	
	*ptr = 'b';
	
	printf("O novo valor de c, alterado via ponteiro é: %c\n", c);
}

void exercicio3() {
	double num = 3.14;
	double *ptr = &num;
	
	printf("O valor inicial de num é: %lf\n", num);
	
	*ptr = 2.71;
	
	printf("O novo valor de num, alterado via ponteiro é: %lf\n", num);
}

void exercicio4() {
	float num = 3.14f;
	float *ptr = &num;
	
	printf("O valor inicial de num é: %f\n", num);
	
	*ptr = 2.71f;
	
	printf("O novo valor de num, alterado via ponteiro é: %f\n", num);
}

void exercicio5() {
	long num = 123456789L;
	long *ptr = &num;
	
	printf("O valor inicial de num é: %ld\n", num);
	
	*ptr = 987654321L;
	
	printf("O novo valor de num, alterado via ponteiro é: %ld\n", num);
}

void exercicio6() {
	int a = 5, b = 7, c;
	int *ptr1 = &a, *ptr2 = &b, *ptr3 = &c;
	
	*ptr3 = *ptr1 + *ptr2;
	
	printf("A soma de %d e %d é: %d\n", a, b, c);
}

void exercicio7() {
	char str[MAX_LENGTH];
	char *ptr = str;
	
	printf("Digite uma string: ");
	fgets(str, 	MAX_LENGTH, stdin);
	
	printf("A string digitada foi %s\n", ptr);
}

void exercicio8() {
	double num1, num2, media;
	double *ptr;
	
	ptr = &num1;
	printf("Digite o primeiro número: ");
	scanf("%lf", ptr);
	
	ptr = &num2;
	printf("Digite o segundo número: ");
	scanf("%lf", ptr);
	
	media = (num1 + num2) / 2.0;
	printf("A média entre %.2lf e %.2lf é: %.2lf\n", num1, num2, media);
}

void exercicio9() {
	int numeros[TAMANHO] = {1, 2, 3, 4, 5};
	int *ptr;
	
	ptr = &numeros[0];
	int i;
	
	printf("Array antes das alterações: ");
	for (i = 0; i < TAMANHO; i++) {
		printf("%d ", numeros[i]);
	}
	printf("\n");
	
	for (i = 0; i < TAMANHO; i++) {
		*(ptr + i) = *(ptr + i) * 2;
	}
	
	printf("Array depois das alterações: ");
	for (i = 0; i < 5; i++) {
		printf("%d ", numeros[i]);
	}
	
	printf("\n");
}

void exercicio10() {
	int num1 = 10, num2 = 5;
	int *ptr1, *ptr2;
	
	ptr1 = &num1;
	ptr2 = &num2;
	
	int diferenca = *ptr1 - *ptr2;
	printf("A diferença entre %d e %d é: %d\n", *ptr1, *ptr2, diferenca); 
}



