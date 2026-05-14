import json
import jsonschema
from pathlib import Path


def load_schema(schema_name: str) -> dict:
    schema_path = Path(__file__).parent.parent / "schemas" / f"{schema_name}.json"
    with open(schema_path) as f:
        return json.load(f)


def validate_schema(response_body: dict, schema_name: str):
    schema = load_schema(schema_name)
    jsonschema.validate(instance=response_body, schema=schema)
