# Flask App

A lightweight Flask app using SQLite and deployable to AWS EC2

See also: [reed/flask-app](https://cloud.docker.com/swarm/reedonly/repository/docker/reedonly/flask-app/general) on Docker Cloud

## Run API Server Locally in Docker

```bash
./launch build
```

## Make a Request

```bash
curl http://localhost:5000/version -i
```

## Run Tests

```bash
nosetests -v
```

## Run Linter

```bash
pylint flask_app tests
```

## Migrate Database

Do the following in the docker container.

1. Check that database is up to date.

    ```bash
    flask db upgrade
    ```
    
2. Modify [data models](flask_app/data_models.py) as needed.

3. Create a migration file.

    ```bash
    flask db migrate -m 'Useful message here'
    ```
    
4. Locate your [migration](flask_app/migrations/versions) and adjust as needed.

5. Test your migration.

    ```bash
    flask db upgrade
    ```

## Deploy to AWS

### Prerequisites

Ubuntu EC2 instance on AWS

### Install Docker

SSH into the EC2 instance and run the following ([ref1](https://www.digitalocean.com/community/tutorials/how-to-install-and-use-docker-on-ubuntu-16-04), [ref2](https://docs.docker.com/compose/install/#install-compose)):

```bash
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"
sudo apt-get update
apt-cache policy docker-ce
sudo apt-get install -y docker-ce
sudo usermod -a -G docker ubuntu
sudo curl -L https://github.com/docker/compose/releases/download/1.17.0/docker-compose-`uname -s`-`uname -m` -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose
```

### Run the deploy script

Provide your own credentials below.

```bash
export DOCKER_USERNAME=username
export DOCKER_PASSWORD=password
export KEY_FILE_PATH=/path/to/key/file
export EC2_HOST=ec2-xx-xxx-xxx-xxx.xxxxxx.compute.amazonaws.com
./deploy
```
