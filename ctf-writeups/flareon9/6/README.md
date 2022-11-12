# à la mode

- This challenge has both .NET and normal C in one. The .NET part doesn't really tell much

## Solution

- load the .dll in x64dbg and set EIP at `10001000`
- patch the call and je that crashes

![flag](https://user-images.githubusercontent.com/97342354/201475251-e4f917dc-cd44-42ae-8ebb-d5a992e6b960.png)
