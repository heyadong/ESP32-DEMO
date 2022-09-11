import network, time 
import usocket as socket
from machine import Pin
led = Pin(2,Pin.OUT)
wlan = network.WLAN(network.STA_IF)
wlan.active(True)
while not wlan.isconnected():
  led.value(1)
  time.sleep(0.5)
  led.value(0)
  time.sleep(0.5)
  if not wlan.isconnected():
    wlan.connect('CMCC-16-7','xkgy1607')
    time.sleep(5)

if wlan.isconnected():
   print('success connect')
   print(wlan.ifconfig())
   led.value(1)
   s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)  #地址簇 : AF_INET (IPv4) 类型: SOCK_STREAM (使用 TCP 传输控制协议)，UDP ：SOCK_DGRAM
   host = wlan.ifconfig()[0]
   port = 52052
   try: 
     print(host)
     s.bind((host,port))
     print('bind success')
   except:
     print("error")
   s.listen(10)
   print("Socket is listening")
   conn, addr = s.accept()
   print(addr[0],addr[1])
while True:
  ret = conn.recv(1024)
  print('hello')
  print(ret)
  if ret == b'bye':
    conn.send(b'bye')
    break
  if ret == b'o':
    led.value(0)
  if ret == b'n':
    led.value(1)
conn.close()
s.close()

  
