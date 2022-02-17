 setup:
 
 
   wget https://artifacts.elastic.co/downloads/elasticsearch/elasticsearch-7.13.2-linux-x86_64.tar.gz

    wget https://artifacts.elastic.co/downloads/elasticsearch/elasticsearch-7.13.2-linux-x86_64.tar.gz.sha512

    shasum -a 512 -c elasticsearch-7.13.2-linux-x86_64.tar.gz.sha512 

    tar -xzf elasticsearch-7.13.2-linux-x86_64.tar.gz

    cd elasticsearch-7.13.2/ 

    ./bin/elasticsearch

to run:

    cd elasticsearch-7.13.2/ 

    ./bin/elasticsearch
