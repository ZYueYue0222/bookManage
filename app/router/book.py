from typing import Optional
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from sqlalchemy import or_
from app.get_db import get_db
from app.models import Book
from app.pydantic_model import BookCreate,BookRead,BookUpdate
from app.pageSettings import pagination


router=APIRouter()


# 渲染
@router.get("/list")
def getlist(
    keyword:Optional[str]=None,
    db:Session=Depends(get_db)
):
    res=db.query(Book).options(joinedload(Book.authors))
    if keyword:
        res=res.filter(or_(
            Book.bname.like(f"%{keyword}%")
        ))
    return res.all()


# 新增
@router.post("/add",status_code=status.HTTP_201_CREATED)
def add_book(form:BookCreate,db:Session=Depends(get_db)):
    res=Book(**form.model_dump())
    db.add(res)
    db.commit()
    db.refresh(res)
    return {"msg":"新增成功","data":res}


# 修改
@router.put("/edit/{id}")
def edit_book(id:int,form:BookUpdate,db:Session=Depends(get_db)):
    res=db.query(Book).get(id)
    if not res:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="未找到该数据,无法修改")
    info=form.model_dump(exclude_unset=True)
    for k,v in info.items():
        setattr(res,k,v)
    db.commit()
    db.refresh(res)
    return {"msg":"修改成功","data":res}


# 删除
@router.delete("/delete/{id}")
def delete_book(id:int,db:Session=Depends(get_db)):
    res=db.query(Book).get(id)
    if not res:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="未找到该数据")
    db.delete(res)
    db.commit()
    return {"msg":"删除成功"}



# 分类渲染
# @router.get("/list2")
# def getlist(
#     db:Session=Depends(get_db)
# ):
#     res=db.query(Author).options(joinedload(Author.books))
#     return res.all()


# 分类新增接口
# @router.post("/add_author",status_code=status.HTTP_201_CREATED)
# def add_book(form:AuthorCreate,db:Session=Depends(get_db)):
#     res=Author(**form.model_dump())
#     db.add(res)
#     db.commit()
#     db.refresh(res)
#     return {"msg":"新增成功","data":res}


# 根据ID查询单本书籍
@router.get("/get_one/{id}",response_model=BookRead)
def get_one(id:int,db:Session=Depends(get_db)):
    res=db.query(Book).get(id)
    if not res:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="未找到该数据")
    return res