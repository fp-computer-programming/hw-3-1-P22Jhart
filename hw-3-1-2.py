#_author_= JH  (AMDG) 9/28/21

card1 = int(input("Input first card worth: "))
card2 = int(input("Input second card worth: "))

if card1 + card2 <=21:
    print("safe")
else:
    print("bust")