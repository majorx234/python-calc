import sys
from add import add
from mul import mul

def calc(operation, a, b):
   if operation==0:
      return add.add(a,b)
   if operation==1:
      return mul.mul(a,b)
def main():
    if len(sys.argv) == 4:
        print(calc(int(sys.argv[1]),int(sys.argv[2]),int(sys.argv[3])))
    else:
        print("ERROR:",str(len(sys.argv)-1)," arguments given instead of 3")

if __name__ == "__main__":
    main()
