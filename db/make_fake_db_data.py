from db.crud import create
from db.database import drop_db, create_db
from db.models import Category

# Очищаю базу
# drop_db()
# create_db()

new = create(Category, {
    "shop": "dasdsa",
    "name": "ssssssss",
})

