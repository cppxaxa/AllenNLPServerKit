docker kill "allennlp_customserver"

docker rm --force "allennlp_customserver"

docker run -h AllenServer --expose 5003 -p 5003:5003 --name "allennlp_customserver" allennlp/allennlp:custom

docker kill "allennlp_customserver"

docker rm --force "allennlp_customserver"
