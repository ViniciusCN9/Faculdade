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

// 1. Escreva um programa que leia dois números inteiros e exiba a soma deles.
void exercicio1() {
	int numero1, numero2;
	
	printf("Digite o primeiro número: ");
	scanf("%d", &numero1);
	
	printf("Digite o segundo número: ");
	scanf("%d", &numero2);
	
	printf("Os números digitados são %d e %d", numero1, numero2);
}

// 2. Escreva um programa que converta uma temperatura de graus Celsius para Fahrenheit.
void exercicio2() {
	double temperaturaCelsius, temperaturaFahrenheit;
	
	printf("Digite a temperatura em Celsius: ");
	scanf("%lf", &temperaturaCelsius);
	
	temperaturaFahrenheit = (temperaturaCelsius * 1.8) + 32;
	
	printf("A temperatura em Fahrenheit é: %lf", temperaturaFahrenheit);
}

// 3. Escreva um programa que calcule a área de um círculo, dado seu raio.
void exercicio3() {
	double PI = 3.1416;
	double raio;
	double area;
	
	printf("Digite o raio da circunferência: ");
	scanf("%lf", &raio);
	
	area = 2 * PI * raio;
	
	printf("A área calculada é: %lf", area);
}

// 4. Escreva um programa que leia três números e exiba o maior deles.
void exercicio4() {
	int entrada;
	int maior = 0;
	
	int i;
	for (i = 0; i < 3; i++) {
		printf("Digite um número: ");
		scanf("%d", &entrada);
		
		if (entrada > maior) {
			maior = entrada;
		}
	}
	
	printf("O maior número é: %d", maior);
}

// 5. Escreva um programa que determine se um número inteiro é par ou ímpar.
void exercicio5() {
	int entrada;
	
	printf("Digite um número: ");
	scanf("%d", &entrada);
	
	if (entrada%2 == 0) {
		printf("O número é par");
	} else {
		printf("O número é impar");
	}
}

// 6. Escreva um programa que leia um número inteiro e exiba a sua tabuada.
void exercicio6() {
	int entrada;
	
	printf("Digite um número: ");
	scanf("%d", &entrada);
	
	int i;
	for (i = 0; i <= 10; i++) {
		printf("%d X %d = %d\n", entrada, i, entrada * i);
	}
}

// 7. Escreva um programa que leia uma string e exiba o número de caracteres.
// 8. Escreva um programa que leia um vetor de 10 números inteiros e exiba a soma de todos os elementos.
// 9. Escreva um programa que leia um vetor de 5 números reais e exiba o maior e o menor valor.
// 10. Escreva um programa que leia um vetor de 10 números inteiros e exiba os elementos em ordem inversa.
// 11. Escreva um programa que leia um vetor de 10 números inteiros e calcule a média aritmética dos elementos.
// 12. Escreva um programa que leia um vetor de 10 números inteiros e determine quantos elementos são pares e quantos são ímpares.
// 13. Escreva um programa que gere 100 número aleatórios inteiros e armazene-os em um vetor, em seguida determine quantos são pares e quantos são ímpares.
// 14. Escreva um programa que implemente uma função para calcular o fatorial de um número inteiro.
// 15. Escreva um programa que implemente uma função para calcular o MDC (Máximo Divisor Comum) de dois números inteiros.
// 16. Escreva um programa que implemente uma função para verificar se um número inteiro é primo.
// 17. Escreva um programa que implemente uma função para calcular a potência de um número real (base) elevado a um número inteiro (expoente).
