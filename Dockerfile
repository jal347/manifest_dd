FROM alpine:latest
LABEL "path"="/tmp/annotations.zip"
LABEL "dump_command"="/usr/bin/wget https://biothings-data.s3.us-west-2.amazonaws.com/docker_test/annotations.zip -O /tmp/annotations.zip"
LABEL keep_container=true
LABEL desc=test
LABEL container_name=mydocker
