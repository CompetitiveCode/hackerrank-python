# Answer to Time Conversion
# https://www.hackerrank.com/challenges/time-conversion/problem


def timeConversion(s):
    hr, mn, sc = s.split(':')
    mnsc = ':'+mn+':'+sc[0:2]
    if 'AM' in sc:
        if hr == '12':
            hr = '00'
    else:
        if hr != '12':
            hr = str(int(hr)+12)
    return hr+mnsc


if __name__ == '__main__':
    print(timeConversion(input()))
