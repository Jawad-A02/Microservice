Microservice Implementation - Communication Contract

To request data from the file, a client socket must be created. It would need to connect with the Server port and address which are being run locally in the example for now. The function will ask the user if they would to check if a file exist with a specific name (this can be implemented to not ask the user as well), then it will send the file name to the server. The server will go ahead and check if a file exists with that name within the directory and it will send back True or False. 

Example: README.md

The server will send back True and the client code will print that the file exists within the directory.

The client can do anything with that information and inform the user however they would like.

![image](https://user-images.githubusercontent.com/107957117/237018076-aa2518f9-2c4e-47d5-b954-b354ef956778.png)
