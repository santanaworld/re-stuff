# anode

- this challenge uses nexe to convert the JavaScript code to an .exe 
- the code is easily extracted via text/hex editors
- the compiler/interpreter is different from normal JavaScript:
  - `Math.random()` isn't random
  - `BigInt` checks are modified
  
## Solution
  - first I instrumented the binary to return the flow of the switch statement
  - then I made it return the generated "random" numbers
  - I changed the script in visual studio code to make it work in reverse -> execute in the modified binary by changing the code to import the external .js file
  
  ![decimal_output](https://user-images.githubusercontent.com/97342354/201475661-7dc281f4-b90c-4e59-914b-506a9af76ddc.png)
  
  Decimal array converted to ascii: `n0t_ju5t_A_j4vaSCriP7_ch4l1eng3@flare-on.com`
