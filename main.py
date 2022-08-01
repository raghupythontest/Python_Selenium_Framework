def birthdayCakeCandles(candles):
    # Write your code here
    n=len(candles)
    candles.sort(reverse=True)
    m_hight=candles[0]
    count=1
    for i in range(1,n):
        if candles[i]==m_hight:
            count +=1
        else:
            break
    return count
def timeConversion(s):
    # Write your code here
    last_two_char = s[-2] + s[-1]
    h = int(s[0:2])
    m = s[3:5]
    seconds = s[6:8]
    new_time = ""
    if h == 12 and last_two_char == "AM":
        return f"00:{m}:{seconds}"
    elif last_two_char == "PM" and h<12:
        h = h + 12
        if h < 10:
            new_time += f"{0}{h}"
        else:
            new_time += f"{h}"

        new_time += f":{m}:{seconds}"

        return new_time
    else:
        return s[0:-2]

s="12:45:54PM"
print(timeConversion(s))

# k=birthdayCakeCandles([3,2,1,3])
# print(k)