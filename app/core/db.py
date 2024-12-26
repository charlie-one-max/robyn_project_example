#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import logging
from tortoise import Tortoise

from app.core.config import settings

logger = logging.getLogger(__name__)


async def db_init():
    await Tortoise.init(
        db_url=f'mysql://{settings.MYSQL_USER}:{settings.MYSQL_PASSWORD}@{settings.MYSQL_HOST}:'
               f'{settings.MYSQL_PORT}/{settings.MYSQL_DATABASE}?charset={settings.MYSQL_CHARSET}',
        modules={'models': ['app.api.user.models']}
    )
    # Generate the schema
    await Tortoise.generate_schemas()
