service "consul-test-consumer" {
  policy = "write"
}

service "consul-test-consumer-sidecar-proxy" {
  policy = "write"
}

service_prefix "" {
  policy = "read"
}

node_prefix "" {
  policy = "read"
}
