from dotenv import load_dotenv
import os
from os.path import join, dirname

dotenv_path = join(dirname(__file__), ".env.dev")
load_dotenv(dotenv_path)

# External API keys
OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")

# Redis configuration
REDIS_HOST = os.environ.get("REDIS_HOST")
REDIS_PORT = os.environ.get("REDIS_PORT")

# All Postgres configuration
POSTGRES_HOST = os.environ.get("POSTGRES_HOST")
POSTGRES_PORT = os.environ.get("POSTGRES_PORT")

# Observability
OTEL_COLLECTOR_HOST = os.environ.get("OTEL_COLLECTOR_HOST")
OTEL_COLLECTOR_HTTP_PORT = os.environ.get("OTEL_COLLECTOR_HTTP_PORT")
OTEL_COLLECTOR_GRPC_PORT = os.environ.get("OTEL_COLLECTOR_GRPC_PORT")

# Feature Flag Variables
FEATURE_FLAG_SERVICE_PORT = os.environ.get("FEATURE_FLAG_SERVICE_PORT")
FEATURE_FLAG_GRPC_SERVICE_PORT = os.environ.get("FEATURE_FLAG_GRPC_SERVICE_PORT")

# OpenTelemetry Collector
OTEL_COLLECTOR_HOST = os.environ.get("OTEL_COLLECTOR_HOST")
OTEL_COLLECTOR_PORT_GRPC = os.environ.get("OTEL_COLLECTOR_PORT_GRPC")
OTEL_COLLECTOR_PORT_HTTP = os.environ.get("OTEL_COLLECTOR_PORT_HTTP")
OTEL_EXPORTER_OTLP_ENDPOINT = os.environ.get("OTEL_EXPORTER_OTLP_ENDPOINT")
PUBLIC_OTEL_EXPORTER_OTLP_TRACES_ENDPOINT = os.environ.get("PUBLIC_OTEL_EXPORTER_OTLP_TRACES_ENDPOINT")

# OpenTelemetry Resource Definitions
OTEL_RESOURCE_ATTRIBUTES = os.environ.get("OTEL_RESOURCE_ATTRIBUTES")

# Metrics Temporality
OTEL_EXPORTER_OTLP_METRICS_TEMPORALITY_PREFERENCE = os.environ.get("OTEL_EXPORTER_OTLP_METRICS_TEMPORALITY_PREFERENCE")

# ********************
# Telemetry Components
# ********************
# Grafana
GRAFANA_SERVICE_PORT = os.environ.get("GRAFANA_SERVICE_PORT")
GRAFANA_SERVICE_HOST = os.environ.get("GRAFANA_SERVICE_HOST")

# Jaeger
JAEGER_SERVICE_PORT = os.environ.get("JAEGER_SERVICE_PORT")
JAEGER_SERVICE_HOST = os.environ.get("JAEGER_SERVICE_HOST")

# Prometheus
PROMETHEUS_SERVICE_PORT = os.environ.get("PROMETHEUS_SERVICE_PORT")
PROMETHEUS_SERVICE_HOST = os.environ.get("PROMETHEUS_SERVICE_HOST")
PROMETHEUS_ADDR = os.environ.get("PROMETHEUS_ADDR")
