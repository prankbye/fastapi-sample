from fastapi import APIRouter

router = APIRouter()


@router.get("/movie/")
async def read_movie():
    return [{"movie_name": "Spider Man"}, {"movie_name": "Iron Man"}]
