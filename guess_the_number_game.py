import sys
import random

while True:
    sys.stdout.buffer.write(b'Please enter two numbers, the minimum number (n) and the maximum number (m). Example:2 8:\n')
    sys.stdout.flush()
    n, m = map(int, sys.stdin.buffer.readline().split())
    if n <= m:
        break

correctAnswer = random.randint(n, m)

sys.stdout.buffer.write(b'The program generates a random number within the range from n to m.\n')
sys.stdout.flush()

while True:
    sys.stdout.buffer.write(b'Please guess the random number and enter it.\n')
    sys.stdout.flush()
    userAnswer = int(sys.stdin.buffer.readline())
    if correctAnswer == userAnswer:
        sys.stdout.buffer.write(b'Correct!\n')
        sys.stdout.flush()
        break
    else:
        sys.stdout.buffer.write(b'Incorrect.\n')
        sys.stdout.flush()