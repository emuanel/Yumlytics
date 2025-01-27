from fastapi import APIRouter, status
from starlette.responses import JSONResponse

router = APIRouter()


@router.get("/", status_code=status.HTTP_200_OK)
def health_check() -> JSONResponse:
    """
    Endpoint for checking health of API

    Returns:
        JSONResponse: status of API
    """
    return JSONResponse(content={"status": "healthy"}, status_code=status.HTTP_200_OK)
