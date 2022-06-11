if __name__ == '__main__':
    b = int(input())
    s = ''
    arr = ['a', 'b', 'c', 'd', 'e']
    for i in range (2**b):
        a = input().split()
        if a[b] == '1':
            for j in range(b):
                if a[j] == '1':
                    s += arr[j]
                else:
                    s += '(' + '-' + arr[j] + ')'
                s += '^'
            s = s.rstrip('^').rstrip('+') + '+'
    print(s.strip('+'))