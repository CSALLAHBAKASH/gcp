echo -n "my super secret data" | gcloud secrets create my-secret \
    --replication-policy="automatic" \
    --data-file=-


# access secret
gcloud secrets versions access 1 --secret="my-secret"

# access secret
gcloud secrets versions access latest --secret="my-secret"
