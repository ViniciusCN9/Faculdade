#include <stdio.h>
#include <stdlib.h>
#include <locale.h>

/* run this program using the console pauser or add your own getch, system("pause") or input loop */

int main(int argc, char *argv[]) {
	setlocale(LC_ALL, "portuguese");
	printf("\n//====//====/1/====//====//\n");
	//exercicio1();
	//getchar();
	printf("\n//====//====/2/====//====//\n");
	//exercicio2();
	//getchar();
	printf("\n//====//====/3/====//====//\n");
	//exercicio3();
	//getchar();
	printf("\n//====//====/4/====//====//\n");
	//exercicio4();
	//getchar();
	printf("\n//====//====/5/====//====//\n");
	//exercicio5();
	//getchar();
	printf("\n//====//====/6/====//====//\n");
	//exercicio6();
	//getchar();
	
	return 0;
}

// 1. Escreva um programa que leia dois n�meros inteiros e exiba a soma deles.
void exercicio1() {
	int numero1, numero2;
	
	printf("Digite o primeiro n�mero: ");
	scanf("%d", &numero1);
	
	printf("Digite o segundo n�mero: ");
	scanf("%d", &numero2);
	
	printf("Os n�meros digitados s�o %d e %d", numero1, numero2);
}

// 2. Escreva um programa que converta uma temperatura de graus Celsius para Fahrenheit.
void exercicio2() {
	double temperaturaCelsius, temperaturaFahrenheit;
	
	printf("Digite a temperatura em Celsius: ");
	scanf("%lf", &temperaturaCelsius);
	
	temperaturaFahrenheit = (temperaturaCelsius * 1.8) + 32;
	
	printf("A temperatura em Fahrenheit �: %lf", temperaturaFahrenheit);
}

// 3. Escreva um programa que calcule a �rea de um c�rculo, dado seu raio.
void exercicio3() {
	double PI = 3.1416;
	double raio;
	double area;
	
	printf("Digite o raio da circunfer�ncia: ");
	scanf("%lf", &raio);
	
	area = 2 * PI * raio;
	
	printf("A �rea calculada �: %lf", area);
}

// 4. Escreva um programa que leia tr�s n�meros e exiba o maior deles.
void exercicio4() {
	int entrada;
	int maior = 0;
	
	int i;
	for (i = 0; i < 3; i++) {
		printf("Digite um n�mero: ");
		scanf("%d", &entrada);
		
		if (entrada > maior) {
			maior = entrada;
		}
	}
	
	printf("O maior n�mero �: %d", maior);
}

// 5. Escreva um programa que determine se um n�mero inteiro � par ou �mpar.
void exercicio5() {
	int entrada;
	
	printf("Digite um n�mero: ");
	scanf("%d", &entrada);
	
	if (entrada%2 == 0) {
		printf("O n�mero � par");
	} else {
		printf("O n�mero � impar");
	}
}

// 6. Escreva um programa que leia um n�mero inteiro e exiba a sua tabuada.
void exercicio6() {
	int entrada;
	
	printf("Digite um n�mero: ");
	scanf("%d", &entrada);
	
	int i;
	for (i = 0; i <= 10; i++) {
		printf("%d X %d = %d\n", entrada, i, entrada * i);
	}
}

// 7. Escreva um programa que leia uma string e exiba o n�mero de caracteres.
// 8. Escreva um programa que leia um vetor de 10 n�meros inteiros e exiba a soma de todos os elementos.
// 9. Escreva um programa que leia um vetor de 5 n�meros reais e exiba o maior e o menor valor.
// 10. Escreva um programa que leia um vetor de 10 n�meros inteiros e exiba os elementos em ordem inversa.
// 11. Escreva um programa que leia um vetor de 10 n�meros inteiros e calcule a m�dia aritm�tica dos elementos.
// 12. Escreva um programa que leia um vetor de 10 n�meros inteiros e determine quantos elementos s�o pares e quantos s�o �mpares.
// 13. Escreva um programa que gere 100 n�mero aleat�rios inteiros e armazene-os em um vetor, em seguida determine quantos s�o pares e quantos s�o �mpares.
// 14. Escreva um programa que implemente uma fun��o para calcular o fatorial de um n�mero inteiro.
// 15. Escreva um programa que implemente uma fun��o para calcular o MDC (M�ximo Divisor Comum) de dois n�meros inteiros.
// 16. Escreva um programa que implemente uma fun��o para verificar se um n�mero inteiro � primo.
// 17. Escreva um programa que implemente uma fun��o para calcular a pot�ncia de um n�mero real (base) elevado a um n�mero inteiro (expoente).
