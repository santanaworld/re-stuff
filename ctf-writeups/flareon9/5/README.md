# T8

- program generates random number -> send POST request to `flare-on.com`, the number is stored in the User-Agent
- receive response -> checks if its base 64 
- do something with the base64
- 2x but with no random number
- if everything is correct the strings turn into shellcode, which prints the flag

## Solution

- find where the number is generated and change it to the one given in the PCAP

![number](https://user-images.githubusercontent.com/97342354/201474121-83313fa1-dbd8-475e-99d3-f8a0f1010539.PNG)


- also change the response to the base64 strings in the PCAP (bp at WinHttpReadData)


![flag](https://user-images.githubusercontent.com/97342354/201474458-236f32b0-9a0c-421b-ae30-1a85bde80bb7.png)
