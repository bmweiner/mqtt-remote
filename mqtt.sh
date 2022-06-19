mosquitto_pub -h ha -p 8883\
    -u <username> -P <pwd>
    --cafile local/certs/ca.crt\
    --cert local/certs/client.crt\
    --key local/certs/client.key\
    -t remote/trigger -m "hello"\
    --insecure

# The mqtt host cert CN must match the -h name in the pub command
# however, the CN is localhost, which will not connect, using insecure mode
# since this will only run locally
