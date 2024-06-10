from app.models.producto_model import Producto


def test_get_products_as_user(test_client, user_auth_headers):
    # El usuario con el rol de "user" debería poder obtener la lista de productos
    response = test_client.get("/api/products", headers=user_auth_headers)
    assert response.status_code == 200
    assert response.json == []


def test_create_product_as_user(test_client, user_auth_headers):
    # El usuario con el rol de "user" no debería poder crear un producto
    data = {"name": "Laptop", "description": "High-end gaming laptop", "price": 1500.0, "stock": 10}
    response = test_client.post("/api/products", json=data, headers=user_auth_headers)
    assert response.status_code == 403


def test_get_product_as_user(test_client, user_auth_headers):
    # Crear un producto antes de intentar obtenerlo
    new_product = Producto(name="Producto de prueba", description="Descripción de prueba", price=10.0, stock=5)
    new_product.save()

    # Ahora intenta obtener el producto
    response = test_client.get(f"/api/products/{new_product.id}", headers=user_auth_headers)
    assert response.status_code == 200
    assert "name" in response.json
    assert "description" in response.json
    assert "price" in response.json
    assert "stock" in response.json

def test_update_product_as_user(test_client, user_auth_headers):
    # El usuario con el rol de "user" no debería poder actualizar un producto
    data = {"name": "Laptop", "description": "Updated description", "price": 1600.0, "stock": 5}
    response = test_client.put("/api/products/1", json=data, headers=user_auth_headers)
    assert response.status_code == 403


def test_delete_product_as_user(test_client, user_auth_headers):
    # El usuario con el rol de "user" no debería poder eliminar un producto
    response = test_client.delete("/api/products/1", headers=user_auth_headers)
    assert response.status_code == 403