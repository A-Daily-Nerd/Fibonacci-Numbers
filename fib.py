from time import time

def timer(func):
    # This function shows the execution time of
    # the function object passed
    def wrap_func(*args, **kwargs):
        t1 = time()
        result = func(*args, **kwargs)
        t2 = time()
        print(f'Function {func.__name__!r} executed in {(t2-t1):.4f}s')
        return result
    return wrap_func

def wtl(file_path, line_num, text_to_write):
    """Writes to a specific line in a file.

    Args:
        file_path: Path to the file.
        line_num: Line number to write to (1-based index).
        text_to_write: The text to write to the line.
    """
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()

        if 1 <= line_num <= len(lines):
            lines[line_num - 1] = text_to_write + '\n'

            with open(file_path, 'w') as file:
                file.writelines(lines)
        else:
             print(f"Line number {line_num} is out of range for file with {len(lines)} lines.")
    except FileNotFoundError:
        print(f"File not found: {file_path}")


cache = {0:0,
        1:1,}
@timer
def fib(n):
    if n in cache:
        return cache[n]
    if n == 1:
        return 1
    if n == 0:
        return 0
    else:
        if n-2 in cache and n-1 in cache:
            return cache[n-2]+cache[n-1]
        if n-1 in cache and n-2 not in cache:
            a = fib(n-2)
            cache[n-2] = a
            wtl("FibNum.txt",n-2,str(a))
            return cache[n-2]+cache[n-1]
        if n-2 in cache and n-1 not in cache:
            a = fib(n-1)
            cache[n-1] = a
            wtl("FibNum.txt",n-1,str(a))
            return cache[n-2]+cache[n-1]
        if n-2 not in cache and n-1 not in cache:
            a = fib(n-2)
            b = fib(n-1)
            cache[n-1] = b
            cache[n-2] = a
            wtl("FibNum.txt",n-1,str(b))
            wtl("FibNum.txt",n-2,str(a))
            return cache[n-2]+cache[n-1]
