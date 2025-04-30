# johnson-dso
## Configuração do Ambiente no Windows

Verifique se o Python 3.12.4 está instalado
Se não estiver, baixe e instale do site oficial: https://www.python.org/downloads/.

Certifique-se de marcar a opção "Add Python to PATH" durante a instalação.

### Crie e ative o ambiente virtual:

##### powershell

```
python -m venv venv
venv\Scripts\activate
```

### Instale as dependências:

##### powershell
```
pip install poetry
poetry install
```
### Integração com o SonarCloud no Windows

Instale o SonarQube Scanner:

##### powershell
```
pip install sonar-scanner
```
Crie o arquivo sonar-project.properties na raiz do projeto e adicione:

#### properties
```
sonar.projectKey=marrbo_johnson-dso
sonar.organization=marrbo
sonar.host.url=https://sonarcloud.io
sonar.login=SEU_TOKEN_SONARCLOUD
```
### Execute o scanner no Windows:

##### powershell
```
sonar-scanner.bat
```
### Baixe e instale o Docker Desktop:
https://www.docker.com/products/docker-desktop/

### Crie um arquivo docker-compose.yml (se necessário) e execute:

##### powershell
```
docker-compose up -d
```

### Rodar os testes Pytest:
##### powershell
```
pytest
```