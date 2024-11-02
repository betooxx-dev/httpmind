from typing import Optional
from app.models.http_status import HttpStatus
from data.http_codes import HTTP_CODES

class HttpRepository:
    @staticmethod
    def get_status_code(code: str) -> Optional[HttpStatus]:
        """
        Obtiene la información de un código de estado HTTP.
        """
        if code in HTTP_CODES:
            return HttpStatus.from_dict(HTTP_CODES[code], code)
        return None

    @staticmethod
    def get_all_codes() -> dict:
        """
        Obtiene todos los códigos HTTP disponibles.
        """
        return {code: HttpStatus.from_dict(data, code) 
                for code, data in HTTP_CODES.items()}