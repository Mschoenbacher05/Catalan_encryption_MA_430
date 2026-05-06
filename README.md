# Introduction:

The following codes is an implementation of two of the catalan encryption methods outlined in Novel Encryption Schemes Based on Catalan Numbers (Kumar et al 2012). The goal of this code is to outline both the simplicity of these methods as well as their combinatorial robustness, that is, the difficulty to decrypt. At a high level, each method's script does the following: 

1) Node1 (user agent 1) uses a catalan encryption method to encrypt a message

2) Node2 is sent and decrypts the message

3) We display that the encrypted method can not be decrypted by typical tools

4) We discuss computational complexity of these methods and wether they could work in production as a robust security metric. 

# Method 1:
Method one consists of the following steps:

1) Nodes agree on an n value and compute C_n. In this code we are skipping this step and assuming n is given, and simply having node 1 compute C_n [see encrypt()]

2) The message to be sent is parsed into chunks of length k, where k is the number of digits in C_n. In this code this is accomplished via the parse_message() function, which returns the parsed message to encrypt().

3) After the message is parsed, a bit swap is performed on every character in the message. In each character 2 bits are swapped corresponding to that characters index in it's chunk applied to the catalan number, e.g if we are encrypting 'ABC' with the catalan key 429, we will swap the letter A using the number 4. Swaps are done according to the following scheme: 

First bit to swap: catalan value mod 8
Second bit to swap: catalan value + 4 mod 8

So for the letter A (in binary 01100001) we will swap the 4th and 0th bits. The resulting binary will be 01000000 converted back to ascii as @.

4) The message is sent ciphered

5) THe message is decrypted by re applying the encryption step and reversing the binary back to how it was. 

# Method 2:

1) Steps 1 and 2 above are completed in the same way

2) Once again we pull a digit from the catalan number that is at the same index of the letter we are encrypting. This time however, rather than converting this into a full byte, we convert it to only a 4 digit binary number, and then append that binary to itself once again to form a full byte. From here we perform another XOR on the byte containing the character and this new catalan byte. 

3) Steps 4 and 5 take place again as before


# Computational Complexity



# Citations:

https://www.sjoerdlangkemper.nl/2019/04/24/bits-bytes-in-python-2-3/ 

https://www.geeksforgeeks.org/python/python-bitwise-operators/ 