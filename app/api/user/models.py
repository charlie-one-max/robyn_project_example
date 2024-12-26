from tortoise import Model, fields


class User(Model):
    id = fields.IntField(primary_key=True)
    name = fields.CharField(max_length=50, null=False)
    account = fields.CharField(max_length=50, unique=True, null=False)
    password = fields.CharField(max_length=50, unique=True, null=False)
    is_active = fields.SmallIntField(default=1)
    is_superuser = fields.SmallIntField(default=0)
    created_by_id = fields.SmallIntField(null=False)
    updated_by_id = fields.SmallIntField(null=False)

    class Meta:
        table = "am_user"
        table_description = "user info"
        unique_together = [("account", "password")]
        indexes = [("is_active", "is_superuser")]

    def __str__(self):
        return self.name
