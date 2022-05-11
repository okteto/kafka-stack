# Deploy your Kafka Stack with Okteto

Click the button below to deploy Zookeeper, Kafka, and Kafdrop using Okteto.

[![Develop on Okteto](https://okteto.com/develop-okteto.svg)](https://cloud.okteto.com/deploy)

You can also do it from your terminal using the [Okteto CLI](https://github.com/okteto/okteto).

```
okteto up
```

Once you've deployed your stack, [login to Okteto Cloud](https://cloud.okteto.com) to see the state of your Okteto stack, logs, and endpoints. The stack includes:

- A REST API that receives a JSON payload and pushes it to a Kafka topic.
- A consumer process that consumes the messages from the topic and prints them out.  
- An instance of [Kafrop](https://github.com/obsidiandynamics/kafdrop), a web UI for viewing Kafka topics and browsing consumer groups. 

You can access the endpoints [from your Okteto Cloud dashboard](https://cloud.okteto.com).

## Try the App

To try it out, send a JSON message to the producer service, replacing the URL with your own:

```
curl -X POST https://producer-cindylopez.cloud.okteto.net -H "Content-Type: application/json" -d '{"message":"hello world!"}'
```

The consumer service will then pick up the message you posted and [log it in the dashboard](https://cloud.okteto.com).
