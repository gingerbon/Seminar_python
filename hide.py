def solution(phone_number):
    n = len(phone_number) # phone number의 길이
    hide = '*' * (n-4) + phone_number[n-4:n]
    return hide
