from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from keycloak import KeycloakOpenIDConnection
from keycloak import KeycloakAdmin
from keycloak import keycloak_openid
import os

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

KEYCLOAK_SERVER_URL = os.getenv("KEYCLOAK_SERVER_URL", "https://sso.sefaz.ba.gov.br/auth")
KEYCLOAK_CLIENT_ID = os.getenv("KEYCLOAK_CLIENT_ID", "johnson-dso")
KEYCLOAK_REALM = os.getenv("KEYCLOAK_REALM", "saml")
KEYCLOAK_CLIENT_SECRET = os.getenv("KEYCLOAK_CLIENT_SECRET", "uBi3G2jl4XMzkWamrJuV9prl9GjT84Wq")

# keycloak_openid = KeycloakOpenID(
#     server_url=KEYCLOAK_SERVER_URL,
#     client_id=KEYCLOAK_CLIENT_ID,
#     realm_name=KEYCLOAK_REALM,
#     client_secret_key=KEYCLOAK_CLIENT_SECRET
# )

keycloak_connection = KeycloakOpenIDConnection(
                        server_url=KEYCLOAK_SERVER_URL,
                        username='abarreto',
                        password='',
                        realm_name="master",
                        user_realm_name=KEYCLOAK_REALM,
                        client_id=KEYCLOAK_CLIENT_ID,
                        client_secret_key=KEYCLOAK_CLIENT_SECRET,
                        verify=True)

keycloak_admin = KeycloakAdmin(connection=keycloak_connection)

async def get_current_user(token: str = Depends(oauth2_scheme)):
    try:
        user_info = keycloak_openid.introspect(token)
        if not user_info.get("active"):
            raise HTTPException(status_code=401, detail="Token inválido ou expirado")
        return user_info
    except Exception:
        raise HTTPException(status_code=401, detail="Erro na autenticação")
