# Introduction:

The following codes is an implementation of two of the catalan encryption methods outlined in Novel Encryption Schemes Based on Catalan Numbers (Kumar et al 2012). The goal of this code is to outline both the simplicity of these methods as well as their combinatorial robustness, that is, the difficulty to decrypt. At a high level, each method's script does the following: 

1) Node1 (user agent 1) uses a catalan encryption method to encrypt a message

2) Node2 is sent and decrypts the message

3) A man in the middle node "sniffs" the encrypted message

4) We display that the encrypted method can not be decrypted by typical tools

5) We discuss computational complexity of these methods and wether they could work in production as a robust security metric. 

# Method 1:
Method one consists of the following steps:

1) Nodes agree on an n value and compute C_n. In this code we are skipping this step and assuming n is given, and simply having node 1 compute C_n [see encrypt()]

2) The message to be sent is parsed into chunks of length k, where k is the number of digits in C_n. In this code this is acomplished via the parse_message() function, which returns the parsed message to encrypt().

3) 

# Method 2:

# Computational Complexity
