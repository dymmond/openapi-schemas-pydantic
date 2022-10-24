from openapi_schemas_pydantic.v3_1_0 import Schema


def test_empty_schema() -> None:
    schema = Schema.parse_obj({})
    assert schema == Schema()
