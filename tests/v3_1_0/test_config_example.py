from openapi_schemas_pydantic.v3_1_0 import (
    XML,
    Callback,
    Components,
    Contact,
    Discriminator,
    Encoding,
    Example,
    ExternalDocumentation,
    Header,
    Info,
    License,
    Link,
    MediaType,
    OAuthFlow,
    OAuthFlows,
    OpenAPI,
    Operation,
    Parameter,
    PathItem,
    Paths,
    Reference,
    RequestBody,
    Response,
    Responses,
    Schema,
    SecurityRequirement,
    SecurityScheme,
    Server,
    ServerVariable,
    Tag,
)


def test_config_example() -> None:
    all_types = [
        OpenAPI,
        Info,
        Contact,
        License,
        Server,
        ServerVariable,
        Components,
        Paths,
        PathItem,
        Operation,
        ExternalDocumentation,
        Parameter,
        RequestBody,
        MediaType,
        Encoding,
        Responses,
        Response,
        Callback,
        Example,
        Link,
        Header,
        Tag,
        Reference,
        Schema,
        Discriminator,
        XML,
        SecurityScheme,
        OAuthFlows,
        OAuthFlow,
        SecurityRequirement,
    ]
    for schema_type in all_types:
        if getattr(schema_type, "Config", None) and getattr(schema_type.Config, "schema_extra", None):  # type: ignore
            examples = schema_type.Config.schema_extra.get("examples")  # type: ignore
            for example_dict in examples:
                obj = schema_type(**example_dict)
                assert obj.__fields_set__
