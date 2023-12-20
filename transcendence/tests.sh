#!/bin/bash
coverage3 run --source='.' manage.py test && coverage3 report && coverage3 xml
docker run --rm --network=42-transcendence_sonarnet -e SONAR_HOST_URL="http://sonarqube:9000" -e SONAR_SCANNER_OPTS="-Dsonar.projectKey=transcendence -Dsonar.python.coverage.reportPaths=./coverage.xml" -e SONAR_TOKEN="sqp_6aee245adabd88c65873fa18803ff5f10474df50" -v ".:/usr/src" sonarsource/sonar-scanner-cli