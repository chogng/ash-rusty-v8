import json
from typing import Any, Dict, Mapping, Optional


def parse_cargo_message(line: str) -> Optional[Dict[str, Any]]:
    try:
        message = json.loads(line)
    except (json.JSONDecodeError, TypeError):
        return None
    return message if isinstance(message, dict) else None


def cargo_artifact_executable(
    message: Optional[Mapping[str, Any]], target_name: str, *, target_kind: str = "bin"
) -> Optional[str]:
    if message is None or message.get("reason") != "compiler-artifact":
        return None
    target = message.get("target")
    if not isinstance(target, dict) or target.get("name") != target_name:
        return None
    kinds = target.get("kind")
    executable = message.get("executable")
    if (
        not isinstance(kinds, list)
        or target_kind not in kinds
        or not isinstance(executable, str)
    ):
        return None
    return executable
