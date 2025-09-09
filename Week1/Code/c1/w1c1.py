import multiprocessing
import time
text = "python multiprocessing makes parallel text processing faster." *100000
def count_vowels(chunks):
    vowels = "aeiouAEIOU"
    return sum(1 for char in chunks if char in vowels)

if __name__ == "__main__":
    num_processes =4
    chunk_size = len(text) // num_processes
    chunks = [text[i:i + chunk_size] for i in range(0, len(text), chunk_size)]
    start =time.time()
    with multiprocessing.Pool(processes=num_processes) as pool:
        results = pool.map(count_vowels, chunks)
    total= sum(results)
    end =time.time()
    print("parallel result:", total)
    print("time taken (parallel):", end - start, "seconds")