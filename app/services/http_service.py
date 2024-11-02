from typing import Optional, Dict, Any
from app.repositories.http_repository import HttpRepository
from app.models.http_status import HttpStatus

class HttpService:
    def __init__(self, repository: HttpRepository):
        self.repository = repository

    def get_status_info(self, code: str) -> Optional[Dict[str, Any]]:
        """
        Obtiene la información formateada de un código de estado HTTP.
        """
        status = self.repository.get_status_code(code)
        if status:
            return status.to_dict()
        return None

    def get_status_by_type(self, type_name: str) -> list:
        """
        Obtiene todos los códigos de estado de un tipo específico.
        """
        all_codes = self.repository.get_all_codes()
        return [status.to_dict() for status in all_codes.values() 
                if status.type.lower() == type_name.lower()]