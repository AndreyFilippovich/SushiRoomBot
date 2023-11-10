import os

from libcloud.storage.drivers.local import LocalStorageDriver
from sqlalchemy import Column, String, Text
from sqlalchemy_file import FileField, ImageField
from sqlalchemy_file.storage import StorageManager
from sqlalchemy_file.validators import SizeValidator

from app.core.db import Base


class Sale(Base):
    picture = Column(
        ImageField(
            upload_storage='default',
            thumbnail_size=(128, 128),
            validators=[SizeValidator(max_size='5000k')],
        )
    )
    text = Column(Text, nullable=False)
    link = Column(String(100), nullable=True)
    file = Column(
        FileField(
            upload_storage='default',
            validators=[SizeValidator(max_size='5000k')],
        )
    )


os.makedirs('./upload_dir/attachment', 0o777, exist_ok=True)
container = LocalStorageDriver('./upload_dir').get_container('attachment')
StorageManager.add_storage('default', container)