FROM python:3.9-slim

WORKDIR /app/

RUN apt-get update && apt-get install -y \
    build-essential

#On ajoute les fichiers nécessaire
ADD main.sh .
ADD main.py .
ADD requirements.txt .
ADD mongo_init.py .
ADD FIFA23.json .

#on donne les accès et on run main.sh
RUN chmod a+x main.sh

#on installe les requirements
RUN pip3 install -r requirements.txt

ENTRYPOINT ["./main.sh"]