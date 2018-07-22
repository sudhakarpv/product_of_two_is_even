# product_of_two_is_even
def main():
    pass
    user=input().split()
    n=user[0]
    m=user[1]
    k=(int(n)*int(m))
    if (k%2==0):
        print("even")
    else:
        print("odd")
if __name__ == '__main__':
    main()
