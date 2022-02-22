FROM ubuntu

ENV TZ=Europe/Minsk
RUN ln -snf "/usr/share/zoneinfo/$TZ" /etc/localtime
RUN echo "$TZ" > /etc/timezone

RUN apt-get update
RUN apt-get install -y tzdata
RUN apt-get install -y apt-utils vim curl apache2 apache2-utils 
RUN apt-get -y install python3 libapache2-mod-wsgi-py3 
RUN ln /usr/bin/python3 /usr/bin/python 
RUN apt-get -y install python3-pip
RUN pip3 install --upgrade pip 
ADD ./site-config.conf /etc/apache2/sites-available/000-default.conf
WORKDIR /var/www/html/mebel 
COPY . /var/www/html/mebel 
RUN pip3 install -r requirements.txt 
RUN chmod 664 /var/www/html/mebel/db.sqlite3 
RUN chmod 775 /var/www/html/mebel/mebel
RUN chown :www-data /var/www/html/mebel/db.sqlite3 
RUN chown :www-data /var/www/html/mebel/mebel
EXPOSE 80
CMD ["apache2ctl", "-D", "FOREGROUND"]


