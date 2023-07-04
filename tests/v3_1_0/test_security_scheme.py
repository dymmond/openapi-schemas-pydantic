from pydantic import AnyUrl

from openapi_schemas_pydantic.v3_1_0 import SecurityScheme


def test_security_scheme_issue_5() -> None:
    security_scheme_1 = SecurityScheme(
        type="openIdConnect", openIdConnectUrl="https://example.com/openIdConnect"
    )
    assert isinstance(security_scheme_1.openIdConnectUrl, (AnyUrl, str))
    assert security_scheme_1.model_dump_json(by_alias=True, exclude_none=True) == (
        '{"type":"openIdConnect","openIdConnectUrl":"https://example.com/openIdConnect"}'
    )

    security_scheme_2 = SecurityScheme(type="openIdConnect", openIdConnectUrl="/openIdConnect")
    assert isinstance(security_scheme_2.openIdConnectUrl, str)
    assert security_scheme_2.model_dump_json(by_alias=True, exclude_none=True) == (
        '{"type":"openIdConnect","openIdConnectUrl":"/openIdConnect"}'
    )

    security_scheme_3 = SecurityScheme(type="openIdConnect", openIdConnectUrl="openIdConnect")
    assert isinstance(security_scheme_3.openIdConnectUrl, str)
    assert security_scheme_3.model_dump_json(by_alias=True, exclude_none=True) == (
        '{"type":"openIdConnect","openIdConnectUrl":"openIdConnect"}'
    )
