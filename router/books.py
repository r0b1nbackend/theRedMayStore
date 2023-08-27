from fastapi import FastAPI,APIRouter,status
from models.books import Book
from database.connection import collection_name
from schema.schemas import list_serial
from bson import ObjectId
from typing import Optional,List
book_router = APIRouter(
    tags=["books"]
)


@book_router.get("/")
async def get_books():
    books = list_serial(collection_name.find())
    return books


@book_router.post("/")
async def post_books(book:Book):
    collection_name.insert_one(dict(book))


@book_router.put("/{id}")
async def put_books(id:str,book:Book):
    collection_name.find_one_and_update({"_id":ObjectId(id)},{"$set":dict(book)})


@book_router.delete("/{id}")
async def delete_books(id:str):
    collection_name.find_one_and_delete({"_id":ObjectId(id)})