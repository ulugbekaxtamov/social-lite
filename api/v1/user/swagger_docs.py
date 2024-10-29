from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi


def profile_update_docs():
    return swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter(
                'name', openapi.IN_FORM, type=openapi.TYPE_STRING,
                description='Полное имя пользователя'
            ),
            openapi.Parameter(
                'avatar', openapi.IN_FORM, type=openapi.TYPE_FILE,
                description='Аватар пользователя'
            ),
        ]
    )
