import time
import sys
import math
import threading

EXECUTION_TIME = 20
prime_count = 0

def sieve_of_atkin(limit):
    primes = [2, 3]
    sieve = [False] * (limit + 1)
    for x in range(1, int(math.sqrt(limit)) + 1):
        for y in range(1, int(math.sqrt(limit)) + 1):
            n = 4 * x**2 + y**2
            if n <= limit and (n % 12 == 1 or n % 12 == 5):
                sieve[n] = not sieve[n]
            n = 3 * x**2 + y**2
            if n <= limit and n % 12 == 7:
                sieve[n] = not sieve[n]
            n = 3 * x**2 - y**2
            if x > y and n <= limit and n % 12 == 11:
                sieve[n] = not sieve[n]
    for n in range(5, int(math.sqrt(limit)) + 1):
        if sieve[n]:
            for k in range(n**2, limit + 1, n**2):
                sieve[k] = False
    primes.extend([n for n in range(5, limit + 1) if sieve[n]])
    return primes

def generate_primes(stop_event):
    global prime_count
    limit = 100000  # Limite inicial para a Sieve of Atkin
    while not stop_event.is_set():
        primes = sieve_of_atkin(limit)
        prime_count = len(primes)
        limit *= 2  # Aumenta o limite para encontrar mais primos

if __name__ == "__main__":
    print(f"Iniciando a contagem de números primos por {EXECUTION_TIME} segundos usando o método de Sieve of Atkin...")
    start_time = time.time()
    stop_event = threading.Event()
    
    prime_thread = threading.Thread(target=generate_primes, args=(stop_event,))
    prime_thread.start()
    
    try:
        while True:
            current_time = time.time() - start_time
            if current_time >= EXECUTION_TIME:
                stop_event.set()
                break
            sys.stdout.write(f"\rTempo corrente: {current_time:.2f} segundos")
            sys.stdout.flush()
    except KeyboardInterrupt:
        stop_event.set()
    
    prime_thread.join()
    print(f"\nNúmeros primos encontrados em {int(current_time)} segundos: {prime_count}")