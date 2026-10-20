# github-pipeline-blueprint

Minimal Flask app used to demo a GitHub Actions quality gate: tests, Trivy vulnerability/secret scanning, Docker build, and push to DockerHub.

## Run locally

```bash
pip install -r requirements.txt
pytest
python app.py   # http://localhost:8080
```

## Pipeline

`.github/workflows/ci.yml`:

1. **test** – installs deps, runs pytest
2. **build-scan-push** (needs test)
   - Trivy fs scan (vuln + secret + misconfig + license, severity HIGH,CRITICAL, exit-code 1)
   - Docker build
   - Trivy image scan (vuln + secret + license, HIGH,CRITICAL, exit-code 1)
   - Push to DockerHub

## Setup

1. Create a GitHub repo and push this code.
2. Add repo secrets: `DOCKER_USERNAME`, `DOCKER_TOKEN` (DockerHub access token).
3. SonarQube Cloud (optional job):
   - Sign up at sonarcloud.io with your GitHub account (free for **public** repos)
   - Import the repo; when asked for the analysis method, choose **CI-based** (or disable "Automatic Analysis" under Administration → Analysis Method)
   - Create a token: My Account → Security → Generate Token
   - Add GitHub secret `SONAR_TOKEN`
   - Fill in `sonar.organization` and `sonar.projectKey` in `sonar-project.properties` (values shown in the SonarCloud project)

## Testing failure scenarios

| Scenario | How to trigger | Expected result |
|---|---|---|
| Old base image CVEs | Change Dockerfile base to `python:3.9.18-slim-bullseye` | Trivy image scan fails the pipeline |
| Vulnerable dependency | Add e.g. `requests==2.19.0` to requirements.txt | Trivy fs scan fails the pipeline |
| Pushed secret | Commit a fake secret, e.g. `AWS_ACCESS_KEY_ID = "AKIAIOSFODNN7EXAMPLE"` in any file | Trivy secret scan fails the pipeline |
