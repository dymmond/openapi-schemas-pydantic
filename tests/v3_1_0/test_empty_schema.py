from openapi_schemas_pydantic.v3_1_0 import Schema


def test_empty_schema() -> None:
    schema = Schema.model_validate({})
    assert schema == Schema()
