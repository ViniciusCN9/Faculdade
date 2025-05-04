import time
import sys
import threading

EXECUTION_TIME = 20
prime_count = 0

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def generate_primes(stop_event):
    global prime_count
    num = 0
    while not stop_event.is_set():
        if is_prime(num):
            prime_count += 1
        num += 1

if __name__ == "__main__":
    print(f"Iniciando a contagem de números primos por {EXECUTION_TIME} segundos...")
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