import random
bilgisayar=random.choice(["taş","kagit","makas"])
kullanıcı=input("taş,kagit ya da makas yaz:")

if kullanıcı == bilgisayar:
    print("Berabere")
elif kullanıcı == "taş" and bilgisayar == "kagit":
    print("Kaybettin")
elif kullanıcı=="makas" and bilgisayar=="taş":
    print("Kaybettin")
elif kullanıcı=="taş" and bilgisayar=="makas":
    print("Kazandın")
elif kullanıcı=="makas" and bilgisayar=="kagit":
    print("Kazandın")
elif kullanıcı=="kagit" and bilgisayar=="taş":
    print("Kazandın")
elif kullanıcı=="kagit" and bilgisayar=="makas":
    print("Kaybettin")
