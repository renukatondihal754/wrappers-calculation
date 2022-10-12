amount=int(input("enter amount you  have \n"))
price_per_choc=1
wrappers_per_choc=2
choclate=amount//price_per_choc
wrappers=choclate
while wrappers>=wrappers_per_choc:
    new_choclate,wrappers=divmod(wrappers,wrappers_per_choc)
    choclate+=new_choclate
    wrappers+=new_choclate

print(choclate)