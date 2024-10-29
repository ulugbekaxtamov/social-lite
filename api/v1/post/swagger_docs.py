from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema


def post_create_docs():
    return swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter(
                'content', openapi.IN_FORM, type=openapi.TYPE_FILE,
                description='File upload for post content'
            ),
            openapi.Parameter(
                'title', openapi.IN_FORM, type=openapi.TYPE_STRING,
                description='Title of the post'
            ),
            openapi.Parameter(
                'description', openapi.IN_FORM, type=openapi.TYPE_STRING,
                description='Description of the post'
            ),
        ]
    )


def post_like_toggle_docs():
    return swagger_auto_schema(
        operation_description="Toggle like on a post. Adds a like if none exists, or removes it if already liked.",
        responses={
            201: openapi.Response("Post liked", schema=openapi.Schema(
                type=openapi.TYPE_OBJECT,
                properties={
                    "liked": openapi.Schema(type=openapi.TYPE_BOOLEAN),
                    "likes_count": openapi.Schema(type=openapi.TYPE_INTEGER)
                }
            )),
            200: openapi.Response("Post unliked", schema=openapi.Schema(
                type=openapi.TYPE_OBJECT,
                properties={
                    "liked": openapi.Schema(type=openapi.TYPE_BOOLEAN),
                    "likes_count": openapi.Schema(type=openapi.TYPE_INTEGER)
                }
            )),
            404: "Post not found",
        }
    )
