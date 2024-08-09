#### Crear entorno virtual
```python
python -m venv .env
```

#### Activamos el entorno virtual
```shell
.\env\Scripts\activate
source .env/bin/activate
```

#### Instalar Flask
```python
pip install Flask
```

#### Mostrar paquetes instalados
```python
pip freeze
pip freeze > paquetes.txt
```

#### En caso de recrear el proyecto
```
pip install -r paquetes.txt
```

#### Traer cambios del repositorio
```
git pull
```

#### Crear ramas hijas
```
git checkout -b rama-hija
```