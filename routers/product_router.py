from fastapi import APIRouter, HTTPException, status
from typing import List
from schemas.product_schema import ProductCreate, ProductUpdate, ProductResponse
from services.product_service import ProductService

router = APIRouter(prefix="/productos", tags=["Productos"])

@router.get("/", response_model=List[ProductResponse], status_code=status.HTTP_200_OK)
def get_products():
    return ProductService.get_all()

@router.get("/{product_id}", response_model=ProductResponse, status_code=status.HTTP_200_OK)
def get_product(product_id: int):
    product = ProductService.get_by_id(product_id)
    if not product:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Producto no encontrado")
    return product

@router.post("/", response_model=ProductResponse, status_code=status.HTTP_201_CREATED)
def create_product(product_data: ProductCreate):
    return ProductService.create(product_data)

@router.put("/{product_id}", response_model=ProductResponse, status_code=status.HTTP_200_OK)
def update_product(product_id: int, product_data: ProductUpdate):
    updated_product = ProductService.update(product_id, product_data)
    if not updated_product:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Producto no encontrado")
    return updated_product

@router.delete("/{product_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_product(product_id: int):
    deleted = ProductService.delete(product_id)
    if not deleted:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Producto no encontrado")
    return None