import json
from typing import Dict, Optional

from pydantic import ConfigDict, Field

from openapi_schemas_pydantic.v3_1_0 import OpenAPI, Operation, PathItem
from openapi_schemas_pydantic.v3_1_0 import Reference as Reference  # noqa


def test_swagger_openapi_v3() -> None:
    location = "tests/data/swagger_openapi_v3.0.1.json"
    with open(location) as loc:
        data = json.load(loc)

    open_api = ExtendedOpenAPI.model_validate(data)
    assert open_api


class ExtendedOperation(Operation):
    """Override classes to use "x-codegen-request-body-name" in Operation."""

    xCodegenRequestBodyName: Optional[str] = Field(
        default=None, alias="x-codegen-request-body-name"
    )

    model_config = ConfigDict(populate_by_name=True)


class ExtendedPathItem(PathItem):
    get: Optional[ExtendedOperation] = None
    put: Optional[ExtendedOperation] = None
    post: Optional[ExtendedOperation] = None
    delete: Optional[ExtendedOperation] = None
    options: Optional[ExtendedOperation] = None
    head: Optional[ExtendedOperation] = None
    patch: Optional[ExtendedOperation] = None
    trace: Optional[ExtendedOperation] = None


class ExtendedOpenAPI(OpenAPI):
    paths: Dict[str, ExtendedPathItem]  # type: ignore


ExtendedOpenAPI.model_rebuild()
