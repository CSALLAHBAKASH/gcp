
## TOPIC
gcloud pubsub topics list

gcloud pubsub topics create myTopic

gcloud pubsub topics create Test1
gcloud pubsub topics create Test2

gcloud pubsub topics delete Test1

## SUBSCRIPTION
gcloud pubsub topics list-subscriptions myTopic
gcloud pubsub subscriptions create --topic myTopic mySubscription
gcloud pubsub subscriptions delete Test1

gcloud pubsub topics publish mytopic1 --message="Hello there"

gcloud pubsub subscriptions pull mytopic1-sub --auto-ack
gcloud pubsub subscriptions pull mySubscription --auto-ack --limit=3