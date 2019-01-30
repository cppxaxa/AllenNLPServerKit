# AllenNLPServer

Introducing AllenNLPServer, exposing "flask_restful" REST API for invoking Machine Comprehension functionality featured in "allennlp"

This package is a modification kit targeting https://github.com/allenai/allennlp
Steps
1. Get hold of "bidaf-model-2017.09.15-charpad.tar.gz" which contains the ready to use model and weights
2. Just copy all the contents to "allennlp" clone and replace files if asked
3. Build the docker image on the modified allennlp clone by the slightly modified command inside the repo "docker build --no-cache -f Dockerfile.pip --tag allennlp/allennlp:custom ." (which includes the dot at end for current directory)
4. After the docker image is built, run startAllen.bat to run the server

API Calls steps
1. Do a get call to the link "http://localhost:5003/service" and it will result hello world message.
2. Load "AllenNLPServer.postman_collection_v21.json" to Postman. Try api calls and observe.


# Special Thanks
Magician (V. M.) for helping docker respond port in Windows 10. The workaround to expose the port from docker includes "expose" args and "host" args. The host is used to bind along with port inside docker image containing the "flask_restful" based python script.

# Troubleshooting

Q. My build is not completing because of some SSLErrors? 
A. Simple solution can be - try building multiple times after some time gaps and try changing internet source (Might solve firewall problems if inside corporate networks).
A. Or check if the problem is due to pip, then apply pip related fixes inside Dockerfile.pip. If the problem is "spacy" failing to download it's english language contents, either you can try different internet sources or just try after some times (Max. times, it works!)