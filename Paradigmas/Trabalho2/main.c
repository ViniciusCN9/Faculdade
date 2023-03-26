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
	printf("\n\n//====//====/1/====//====//\n\n");
	exercicio1();
	getchar();
	printf("\n\n//====//====/2/====//====//\n\n");
	exercicio2();
	getchar();
	printf("\n\n//====//====/3/====//====//\n\n");
	exercicio3();
	getchar();
	printf("\n\n//====//====/4/====//====//\n\n");
	exercicio4();
	getchar();
	printf("\n\n//====//====/5/====//====//\n\n");
	exercicio5();
	getchar();
	printf("\n\n//====//====/6/====//====//\n\n");
	exercicio6();
	getchar();
	printf("\n\n//====//====/7/====//====//\n\n");
	exercicio7();
	getchar();
	printf("\n\n//====//====/8/====//====//\n\n");
	exercicio8();
	getchar();
	printf("\n\n//====//====/9/====//====//\n\n");
	exercicio9();
	getchar();
	printf("\n\n//====//====/10/====//====//\n\n");
	exercicio10();
	getchar();
	printf("\n\n//====//====/11/====//====//\n\n");
	exercicio11();
	getchar();
	printf("\n\n//====//====/12/====//====//\n\n");
	exercicio12();
	getchar();
	printf("\n\n//====//====/13/====//====//\n\n");
	exercicio13();
	getchar();
	printf("\n\n//====//====/14/====//====//\n\n");
	exercicio14();
	getchar();
	printf("\n\n//====//====/15/====//====//\n\n");
	exercicio15();
	getchar();
	printf("\n\n//====//====/16/====//====//\n\n");
	exercicio16();
	getchar();
	printf("\n\n//====//====/17/====//====//\n\n");
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

	printf("Digite o primeiro n�mero: ");
	scanf("%d", &numero1);

	printf("Digite o segundo n�mero: ");
	scanf("%d", &numero2);

	soma = numero1 + numero2;

	printf("A soma dos n�meros digitados � %d", soma);
}

// 2. Escreva um programa que converta uma temperatura de graus Celsius para Fahrenheit.
void exercicio2()
{
	double temperaturaCelsius, temperaturaFahrenheit;

	printf("Digite a temperatura em Celsius: ");
	scanf("%lf", &temperaturaCelsius);

	temperaturaFahrenheit = (temperaturaCelsius * 1.8) + 32;

	printf("A temperatura em Fahrenheit �: %lf", temperaturaFahrenheit);
}

// 3. Escreva um programa que calcule a �rea de um c�rculo, dado seu raio.
void exercicio3()
{
	double PI = 3.1416;
	double raio;
	double area;

	printf("Digite o raio da circunfer�ncia: ");
	scanf("%lf", &raio);

	area = PI * raio * raio;

	printf("A �rea calculada �: %lf", area);
}

// 4. Escreva um programa que leia tr�s n�meros e exiba o maior deles.
void exercicio4()
{
	int entrada;
	int maior = 0;

	int i;
	for (i = 0; i < 3; i++)
	{
		printf("Digite um n�mero: ");
		scanf("%d", &entrada);

		if (entrada > maior)
		{
			maior = entrada;
		}
	}

	printf("O maior n�mero �: %d", maior);
}

// 5. Escreva um programa que determine se um n�mero inteiro � par ou �mpar.
void exercicio5()
{
	int entrada;

	printf("Digite um n�mero: ");
	scanf("%d", &entrada);

	if (entrada % 2 == 0)
	{
		printf("O n�mero � par");
	}
	else
	{
		printf("O n�mero � impar");
	}
}

// 6. Escreva um programa que leia um n�mero inteiro e exiba a sua tabuada.
void exercicio6()
{
	int entrada;

	printf("Digite um n�mero: ");
	scanf("%d", &entrada);

	int i;
	for (i = 0; i <= 10; i++)
	{
		printf("%d X %d = %d\n", entrada, i, entrada * i);
	}
}

// 7. Escreva um programa que leia uma string e exiba o n�mero de caracteres.
void exercicio7()
{
	char texto[100];
	int quantidade;

	printf("Digite o texto: ");
	fgets(texto, 100, stdin);

	quantidade = strlen(texto) - 1;
	printf("O n�mero de caracteres �: %d", quantidade);
}

// 8. Escreva um programa que leia um vetor de 10 n�meros inteiros e exiba a soma de todos os elementos.
void exercicio8()
{
	int vetor[10];
	int i, soma = 0;

	for (i = 0; i < 10; i++)
	{
		printf("Digite o %d� n�mero: ", i + 1);
		scanf("%d", &vetor[i]);
	}

	for (i = 0; i < 10; i++)
	{
		soma += vetor[i];
	}

	printf("A soma dos elementos do vetor �: %d\n", soma);
}

// 9. Escreva um programa que leia um vetor de 5 n�meros reais e exiba o maior e o menor valor.
void exercicio9()
{
	float vetor[5];
	float maior, menor;
	int i;

	for (i = 0; i < 5; i++)
	{
		printf("Digite o %d� n�mero: ", i + 1);
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

	printf("O maior n�mero do vetor �: %.2f\n", maior);
	printf("O menor n�mero do vetor �: %.2f\n", menor);
}

// 10. Escreva um programa que leia um vetor de 10 n�meros inteiros e exiba os elementos em ordem inversa.
void exercicio10()
{
	int vetor[10];
	int i;

	for (i = 0; i < 10; i++)
	{
		printf("Digite o %d� n�mero: ", i + 1);
		scanf("%d", &vetor[i]);
	}

	printf("O vetor em ordem inversa �: ");
	for (i = 9; i >= 0; i--)
	{
		printf("%d ", vetor[i]);
	}
}

// 11. Escreva um programa que leia um vetor de 10 n�meros inteiros e calcule a m�dia aritm�tica dos elementos.
void exercicio11()
{
	int vetor[10];
	float media = 0;
	int i;

	for (i = 0; i < 10; i++)
	{
		printf("Digite o %d� n�mero: ", i + 1);
		scanf("%d", &vetor[i]);
		media += vetor[i];
	}

	media /= 10;

	printf("A m�dia dos elementos do vetor �: %.2f", media);
}

// 12. Escreva um programa que leia um vetor de 10 n�meros inteiros e determine quantos elementos s�o pares e quantos s�o �mpares.
void exercicio12()
{
	int vetor[10];
	int i, pares = 0, impares = 0;

	for (i = 0; i < 10; i++)
	{
		printf("Digite o %d� n�mero: ", i + 1);
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

	printf("O vetor cont�m %d n�mero(s) par(es) e %d n�mero(s) �mpar(es).", pares, impares);
}

// 13. Escreva um programa que gere 100 n�mero aleat�rios inteiros e armazene-os em um vetor, em seguida determine quantos s�o pares e quantos s�o �mpares.
void exercicio13()
{
	int vetor[100];
	int i, pares = 0, impares = 0;

	// Inicializa o gerador de n�meros aleat�rios com a hora atual do sistema
	srand(time(NULL));

	// Preenche o vetor com 100 n�meros aleat�rios entre 0 e 99
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

	printf("O vetor cont�m %d n�mero(s) par(es) e %d n�mero(s) �mpar(es).", pares, impares);
}

// 14. Escreva um programa que implemente uma fun��o para calcular o fatorial de um n�mero inteiro.
void exercicio14()
{
	int entrada, fatorial;

	printf("Digite um n�mero inteiro: ");
	scanf("%d", &entrada);

	fatorial = obterFatorial(entrada);

	printf("O fatorial de %d � %d.", entrada, fatorial);
}

// 15. Escreva um programa que implemente uma fun��o para calcular o MDC (M�ximo Divisor Comum) de dois n�meros inteiros.
void exercicio15()
{
	int entrada1, entrada2, resultado;

	printf("Digite dois n�meros inteiros: ");
	scanf("%d %d", &entrada1, &entrada2);

	resultado = obterMaximoDivisorComum(entrada1, entrada2);

	printf("O m�ximo divisor comum entre %d e %d � %d.", entrada1, entrada2, resultado);
}

// 16. Escreva um programa que implemente uma fun��o para verificar se um n�mero inteiro � primo.
void exercicio16()
{
	int entrada;

	printf("Digite um n�mero inteiro: ");
	scanf("%d", &entrada);

	if (verificarPrimo(entrada))
	{
		printf("%d � primo!", entrada);
	}
	else
	{
		printf("%d n�o � primo!", entrada);
	}
}

// 17. Escreva um programa que implemente uma fun��o para calcular a pot�ncia de um n�mero real (base) elevado a um n�mero inteiro (expoente).
void exercicio17()
{
	float base, resultado;
	int expoente;

	printf("Digite a base (real separdo com ','): ");
	scanf("%f", &base);

	printf("Digite o expoente (inteiro): ");
	scanf("%d", &expoente);

	resultado = calcularPotencia(base, expoente);

	printf("%.2f elevado a %d � igual a %.2f", base, expoente, resultado);
}
