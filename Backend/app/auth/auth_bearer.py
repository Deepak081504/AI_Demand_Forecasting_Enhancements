from fastapi import Request, HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from jose import jwt, JWTError
from app.config import SECRET_KEY, ALGORITHM


class JWTBearer(HTTPBearer):

    async def __call__(self, request: Request):

        credentials: HTTPAuthorizationCredentials = await super().__call__(request)

        if credentials:

            if not self.verify_jwt(credentials.credentials):
                raise HTTPException(
                    status_code=403,
                    detail="Invalid or Expired Token"
                )

            return credentials.credentials

        raise HTTPException(
            status_code=403,
            detail="Invalid Authorization Code"
        )

    def verify_jwt(self, token: str):

        try:
            payload = jwt.decode(
                token,
                SECRET_KEY,
                algorithms=[ALGORITHM]
            )

            return payload

        except JWTError:
            return False