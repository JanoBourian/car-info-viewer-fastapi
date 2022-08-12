from fastapi import APIRouter

router = APIRouter(tags = ["engine"], prefix = "/engine")

@router.get("/")
async def get_all_engines():
    return {"message": "engines"}