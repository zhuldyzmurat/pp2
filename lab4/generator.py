#ex1
def gen(N):
   for i in range(1, N+1):
     yield i * i
     
N=int(input())
squares_generator = gen(N)
for square in squares_generator:
    print(square)
#ex2
def gen(n):
   for i in range(1, n+1):
    if i % 2 == 0:
        yield i

n=int(input())
even_generator = gen(n)
for a in even_generator:
  print(a,end=', ')
#ex3
def gen(n):
   for i in range(0 , n+1):
      if i % 3 == 0 and i % 4 == 0:
       yield i

n = int(input())
it_generator = gen(n)
for a in it_generator:
     print(a)
#ex4
def gen(a,b):
   for i in range(a, b+1):
     yield i * i
     
a=int(input())
b=int(input())
squares_generator = gen(a,b)
for square in squares_generator:
    print(square)
#ex5
def gen(n):
   for i in range(n, -1, -1):
     yield i
     
n = int(input())
down_generator = gen(n)
for down in down_generator:
    print(down)
