from typing import Union

from pydantic import BaseModel, Field
from typing_extensions import Literal

from openapi_schemas_pydantic.utils.utils import (
    OpenAPI310PydanticSchema,
    construct_open_api_with_schema_class,
)
from openapi_schemas_pydantic.v3_1_0 import (
    Discriminator,
    Info,
    MediaType,
    OpenAPI,
    Operation,
    PathItem,
    Reference,
    RequestBody,
    Response,
    Schema,
)


def test_pydantic_discriminator_openapi_generation() -> None:
    open_api = construct_open_api_with_schema_class(construct_base_open_api())
    json_schema = open_api.components.schemas["RequestModel"]  # type: ignore
    assert json_schema.properties == {
        "data": Schema(
            oneOf=[
                Reference(
                    ref="#/components/schemas/DataAModel",
                    summary=None,
                    description=None,
                ),
                Reference(
                    ref="#/components/schemas/DataBModel",
                    summary=None,
                    description=None,
                ),
            ],
            title="Data",
            discriminator=Discriminator(
                propertyName="kind",
                mapping={
                    "a": "#/components/schemas/DataAModel",
                    "b": "#/components/schemas/DataBModel",
                },
            ),
        )
    }


def construct_base_open_api() -> OpenAPI:
    return OpenAPI(
        info=Info(
            title="My own API",
            version="v0.0.1",
        ),
        paths={
            "/ping": PathItem(
                post=Operation(
                    requestBody=RequestBody(
                        content={
                            "application/json": MediaType(
                                media_type_schema=OpenAPI310PydanticSchema(
                                    schema_class=RequestModel
                                )
                            )
                        }
                    ),
                    responses={"200": Response(description="pong")},
                )
            )
        },
    )


class DataAModel(BaseModel):
    kind: Literal["a"]


class DataBModel(BaseModel):
    kind: Literal["b"]


class RequestModel(BaseModel):
    data: Union[DataAModel, DataBModel] = Field(discriminator="kind")
