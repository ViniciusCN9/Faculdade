import time
import sys
import threading

EXECUTION_TIME = 20
prime_count = 0

def sieve_of_sundaram(limit):
    n = (limit - 1) // 2
    sieve = [True] * (n + 1)
    for i in range(1, n + 1):
        j = i
        while i + j + 2 * i * j <= n:
            sieve[i + j + 2 * i * j] = False
            j += 1
    primes = [2] + [2 * i + 1 for i in range(1, n + 1) if sieve[i]]
    return primes

def generate_primes(stop_event):
    global prime_count
    limit = 100000  # Limite inicial para a Sieve of Sundaram
    while not stop_event.is_set():
        primes = sieve_of_sundaram(limit)
        prime_count = len(primes)
        limit *= 2  # Aumenta o limite para encontrar mais primos

if __name__ == "__main__":
    print(f"Iniciando a contagem de números primos por {EXECUTION_TIME} segundos usando o método de Sieve of Sundaram...")
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