"""while(True):
    try:
        a,b=list(map(int,input().split()))
        x = min(a,b)
        y = max(a,b)
        if(a<=0 or b<=0):
            break
        else:
            sum=0
            result = ''
            for i in range(x,y+1):
                result += str(i)+' '
                sum = sum + i
            result+= 'Sum=%d'
            print(result %sum)
    except EOFError:
        break"""
while True:
    # Read pair of values M and N
    M, N = map(int, input().split())

    # Check if any value is less than or equal to zero
    if M <= 0 or N <= 0:
        break

    # Determine the smaller and larger values
    smaller = min(M, N)
    larger = max(M, N)

    # Generate the sequence and calculate the sum
    sequence = list(range(smaller, larger + 1))
    sequence_sum = sum(sequence)

    # Print the sequence and its sum
    print(" ".join(map(str, sequence)), "Sum=" + str(sequence_sum))
