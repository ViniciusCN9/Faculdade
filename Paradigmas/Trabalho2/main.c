#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>
#include <locale.h>
#include <time.h>

/* run this program using the console pauser or add your own getch, system("pause") or input loop */

int main(int argc, char *argv[])
{
	setlocale(LC_ALL, "portuguese");
	printf("\n//====//====/1/====//====//\n");
	exercicio1();
	getchar();
	printf("\n//====//====/2/====//====//\n\n");
	exercicio2();
	getchar();
	printf("\n//====//====/3/====//====//\n\n");
	exercicio3();
	getchar();
	printf("\n//====//====/4/====//====//\n\n");
	exercicio4();
	getchar();
	printf("\n//====//====/5/====//====//\n\n");
	exercicio5();
	getchar();
	printf("\n//====//====/6/====//====//\n\n");
	exercicio6();
	getchar();
	printf("\n//====//====/7/====//====//\n\n");
	exercicio7();
	getchar();
	printf("\n//====//====/8/====//====//\n\n");
	exercicio8();
	getchar();
	printf("\n//====//====/9/====//====//\n\n");
	exercicio9();
	getchar();
	printf("\n//====//====/10/====//====//\n\n");
	exercicio10();
	getchar();
	printf("\n//====//====/11/====//====//\n\n");
	exercicio11();
	getchar();
	printf("\n//====//====/12/====//====//\n\n");
	exercicio12();
	getchar();
	printf("\n//====//====/13/====//====//\n\n");
	exercicio13();
	getchar();
	printf("\n//====//====/14/====//====//\n\n");
	exercicio14();
	getchar();
	printf("\n//====//====/15/====//====//\n\n");
	exercicio15();
	getchar();
	printf("\n//====//====/16/====//====//\n\n");
	exercicio16();
	getchar();
	printf("\n//====//====/17/====//====//\n\n");
	exercicio17();
	getchar();

	return 0;
}

// 0. Auxiliares
int obterFatorial(int numero)
{
	if (numero == 0)
	{
		return 1;
	}
	else
	{
		return numero * obterFatorial(numero - 1);
	}
}

int obterMaximoDivisorComum(int numero1, int numero2)
{
	if (numero2 == 0)
	{
		return numero1;
	}
	else
	{
		return obterMaximoDivisorComum(numero2, numero1 % numero2);
	}
}

bool verificarPrimo(int numero)
{
	int i;

	if (numero <= 1)
	{
		return false;
	}
	for (i = 2; i <= numero / 2; i++)
	{
		if (numero % i == 0)
		{
			return false;
		}
	}
	return true;
}

float calcularPotencia(float base, int expoente)
{
	float resultado = 1;
	int i;

	if (expoente == 0)
	{
		return 1;
	}
	else if (expoente < 0)
	{
		for (i = 1; i <= -expoente; i++)
		{
			resultado /= base;
		}
	}
	else
	{
		for (i = 1; i <= expoente; i++)
		{
			resultado *= base;
		}
	}

	return resultado;
}

// 1. Escreva um programa que leia dois números inteiros e exiba a soma deles.
void exercicio1()
{
	int numero1, numero2, soma;

	printf("Digite o primeiro número: ");
	scanf("%d", &numero1);

	printf("Digite o segundo número: ");
	scanf("%d", &numero2);

	soma = numero1 + numero2;

	printf("A soma dos números digitados é %d", soma);
}

// 2. Escreva um programa que converta uma temperatura de graus Celsius para Fahrenheit.
void exercicio2()
{
	double temperaturaCelsius, temperaturaFahrenheit;

	printf("Digite a temperatura em Celsius: ");
	scanf("%lf", &temperaturaCelsius);

	temperaturaFahrenheit = (temperaturaCelsius * 1.8) + 32;

	printf("A temperatura em Fahrenheit é: %lf", temperaturaFahrenheit);
}

// 3. Escreva um programa que calcule a área de um círculo, dado seu raio.
void exercicio3()
{
	double PI = 3.1416;
	double raio;
	double area;

	printf("Digite o raio da circunferência: ");
	scanf("%lf", &raio);

	area = PI * raio * raio;

	printf("A área calculada á: %lf", area);
}

// 4. Escreva um programa que leia três números e exiba o maior deles.
void exercicio4()
{
	int entrada;
	int maior = 0;

	int i;
	for (i = 0; i < 3; i++)
	{
		printf("Digite um número: ");
		scanf("%d", &entrada);

		if (entrada > maior)
		{
			maior = entrada;
		}
	}

	printf("O maior número é: %d", maior);
}

// 5. Escreva um programa que determine se um número inteiro é par ou ímpar.
void exercicio5()
{
	int entrada;

	printf("Digite um número: ");
	scanf("%d", &entrada);

	if (entrada % 2 == 0)
	{
		printf("O número é par");
	}
	else
	{
		printf("O número é impar");
	}
}

// 6. Escreva um programa que leia um número inteiro e exiba a sua tabuada.
void exercicio6()
{
	int entrada;

	printf("Digite um número: ");
	scanf("%d", &entrada);

	int i;
	for (i = 0; i <= 10; i++)
	{
		printf("%d X %d = %d\n", entrada, i, entrada * i);
	}
}

// 7. Escreva um programa que leia uma string e exiba o número de caracteres.
void exercicio7()
{
	char texto[100];
	int quantidade;

	printf("Digite o texto: ");
	fgets(texto, 100, stdin);

	quantidade = strlen(texto) - 1;
	printf("O número de caracteres é: %d", quantidade);
}

// 8. Escreva um programa que leia um vetor de 10 números inteiros e exiba a soma de todos os elementos.
void exercicio8()
{
	int vetor[10];
	int i, soma = 0;

	for (i = 0; i < 10; i++)
	{
		printf("Digite o %dº número: ", i + 1);
		scanf("%d", &vetor[i]);
	}

	for (i = 0; i < 10; i++)
	{
		soma += vetor[i];
	}

	printf("A soma dos elementos do vetor é: %d\n", soma);
}

// 9. Escreva um programa que leia um vetor de 5 números reais e exiba o maior e o menor valor.
void exercicio9()
{
	float vetor[5];
	float maior, menor;
	int i;

	for (i = 0; i < 5; i++)
	{
		printf("Digite o %dº número: ", i + 1);
		scanf("%f", &vetor[i]);
	}

	maior = vetor[0];
	menor = vetor[0];

	for (i = 1; i < 5; i++)
	{
		if (vetor[i] > maior)
		{
			maior = vetor[i];
		}
		if (vetor[i] < menor)
		{
			menor = vetor[i];
		}
	}

	printf("O maior número do vetor é: %.2f\n", maior);
	printf("O menor número do vetor é: %.2f\n", menor);
}

// 10. Escreva um programa que leia um vetor de 10 números inteiros e exiba os elementos em ordem inversa.
void exercicio10()
{
	int vetor[10];
	int i;

	for (i = 0; i < 10; i++)
	{
		printf("Digite o %dº número: ", i + 1);
		scanf("%d", &vetor[i]);
	}

	printf("O vetor em ordem inversa é: ");
	for (i = 9; i >= 0; i--)
	{
		printf("%d ", vetor[i]);
	}
}

// 11. Escreva um programa que leia um vetor de 10 números inteiros e calcule a média aritmética dos elementos.
void exercicio11()
{
	int vetor[10];
	float media = 0;
	int i;

	for (i = 0; i < 10; i++)
	{
		printf("Digite o %dº número: ", i + 1);
		scanf("%d", &vetor[i]);
		media += vetor[i];
	}

	media /= 10;

	printf("A média dos elementos do vetor é: %.2f", media);
}

// 12. Escreva um programa que leia um vetor de 10 números inteiros e determine quantos elementos são pares e quantos são ímpares.
void exercicio12()
{
	int vetor[10];
	int i, pares = 0, impares = 0;

	for (i = 0; i < 10; i++)
	{
		printf("Digite o %dº número: ", i + 1);
		scanf("%d", &vetor[i]);
	}

	for (i = 0; i < 10; i++)
	{
		if (vetor[i] % 2 == 0)
		{
			pares++;
		}
		else
		{
			impares++;
		}
	}

	printf("O vetor contém %d número(s) par(es) e %d número(s) ímpar(es).", pares, impares);
}

// 13. Escreva um programa que gere 100 número aleatórios inteiros e armazene-os em um vetor, em seguida determine quantos são pares e quantos são ímpares.
void exercicio13()
{
	int vetor[100];
	int i, pares = 0, impares = 0;

	// Inicializa o gerador de números aleatórios com a hora atual do sistema
	srand(time(NULL));

	// Preenche o vetor com 100 números aleatórios entre 0 e 99
	for (i = 0; i < 100; i++)
	{
		vetor[i] = rand() % 100;
	}

	for (i = 0; i < 100; i++)
	{
		if (vetor[i] % 2 == 0)
		{
			pares++;
		}
		else
		{
			impares++;
		}
	}

	printf("O vetor contém %d número(s) par(es) e %d número(s) ímpar(es).", pares, impares);
}

// 14. Escreva um programa que implemente uma função para calcular o fatorial de um número inteiro.
void exercicio14()
{
	int entrada, fatorial;

	printf("Digite um número inteiro: ");
	scanf("%d", &entrada);

	fatorial = obterFatorial(entrada);

	printf("O fatorial de %d é %d.", entrada, fatorial);
}

// 15. Escreva um programa que implemente uma função para calcular o MDC (Máximo Divisor Comum) de dois números inteiros.
void exercicio15()
{
	int entrada1, entrada2, resultado;

	printf("Digite dois números inteiros: ");
	scanf("%d %d", &entrada1, &entrada2);

	resultado = obterMaximoDivisorComum(entrada1, entrada2);

	printf("O máximo divisor comum entre %d e %d é %d.", entrada1, entrada2, resultado);
}

// 16. Escreva um programa que implemente uma função para verificar se um número inteiro é primo.
void exercicio16()
{
	int entrada;

	printf("Digite um número inteiro: ");
	scanf("%d", &entrada);

	if (verificarPrimo(entrada))
	{
		printf("%d é primo!", entrada);
	}
	else
	{
		printf("%d não é primo!", entrada);
	}
}

// 17. Escreva um programa que implemente uma função para calcular a potência de um número real (base) elevado a um número inteiro (expoente).
void exercicio17()
{
	float base, resultado;
	int expoente;

	printf("Digite a base (real separdo com ','): ");
	scanf("%f", &base);

	printf("Digite o expoente (inteiro): ");
	scanf("%d", &expoente);

	resultado = calcularPotencia(base, expoente);

	printf("%.2f elevado a %d é igual a %.2f", base, expoente, resultado);
}
