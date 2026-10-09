from fastapi import Query

def pagination(page:int=Query(1,ge=1),pageSize:int=Query(10,ge=1,le=100)):
    return {"page":page,"pageSize":pageSize}