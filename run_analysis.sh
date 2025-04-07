# !/bin/bash

# Gerar relatório de testes
pytest --junitxml=tests/report.xml tests/

# Gerar relatório de cobertura
pytest --cov=rabbitmq_example --cov-report=xml tests/

# Executar pylint
pylint rabbitmq_example/ tests/ > pylint-report.txt || true

# Executar SonarScanner
sonar-scanner \
  -Dsonar.host.url=http://localhost:9000 \
  -Dsonar.token=${SONARQUBE_TOKEN}