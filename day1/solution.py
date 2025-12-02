



def unlock_safe(file_path):
    dial = 50
    zeros = 0
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            dir = line[0]
            val = int(line[1:])


            if dir=='L':
                dial = (dial-val)%100
            else:
                dial = (dial+val)%100
            
            if dial == 0:
                zeros += 1

    return zeros

if __name__=='__main__':
    ans = unlock_safe('day1/input.txt')
    print(ans)
        