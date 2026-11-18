#!/usr/bin/env python3
"""Offline, conservative scalar merge for saved native exports. Never calls Instapage.

ip_preserve.py baseline.json current.json changes.json > candidate.json
changes: {"current_sha256": <canonical digest>, "changes": [{"path": [keys/indices], "value": scalar}]}
Use digest() to fingerprint the current parsed export. Arrays/objects are never replaced.
This proves preservation in JSON only, not native schema support or runtime behavior.
"""
import copy
import hashlib
import json
import sys


def digest(data):
    return hashlib.sha256(json.dumps(data, sort_keys=True, separators=(",", ":"), ensure_ascii=False, allow_nan=False).encode()).hexdigest()


def scalar(value):
    return value is None or type(value) in (str, int, float, bool)


def locate(data, path):
    if not isinstance(path, list) or not path:
        raise ValueError("non-empty path required")
    node = data
    for key in path:
        if isinstance(node, dict) and isinstance(key, str) and key in node:
            node = node[key]
        elif isinstance(node, list) and type(key) is int and 0 <= key < len(node):
            node = node[key]
        else:
            raise ValueError("path missing or structurally changed")
    return node


def merge(baseline, current, request):
    if request.get("current_sha256") != digest(current):
        raise ValueError("current export changed; resave, re-export and replan")
    changes = request.get("changes")
    if not isinstance(changes, list) or not changes:
        raise ValueError("explicit scalar changes required")
    out = copy.deepcopy(current)
    seen = set()
    for change in changes:
        path = change.get("path")
        before = locate(baseline, path)
        now = locate(current, path)
        key = json.dumps(path)
        if key in seen:
            raise ValueError("duplicate path")
        seen.add(key)
        if "value" not in change:
            raise ValueError("change value missing")
        desired = change["value"]
        if not all(scalar(v) for v in (before, now, desired)):
            raise ValueError("structure replacement forbidden; use native editor")
        # Numeric array addresses cannot safely survive reorder/insertion/deletion.
        for i, part in enumerate(path):
            if type(part) is int:
                old_array = baseline if i == 0 else locate(baseline, path[:i])
                new_array = current if i == 0 else locate(current, path[:i])
                if digest(old_array) != digest(new_array):
                    raise ValueError("array changed; resolve stable native IDs before applying")
        if digest(desired) == digest(before):
            continue  # no requested change; retain any editor edit
        if digest(now) not in (digest(before), digest(desired)):
            raise ValueError("conflict with saved editor edit")
        parent = out if len(path) == 1 else locate(out, path[:-1])
        parent[path[-1]] = desired
    return out


def main():
    try:
        if len(sys.argv) != 4:
            raise ValueError("usage: ip_preserve.py baseline.json current.json changes.json")
        data = [json.load(open(p, encoding="utf-8")) for p in sys.argv[1:]]
        result = merge(*data)
        print(json.dumps(result, indent=2, ensure_ascii=False, allow_nan=False))
    except (ValueError, TypeError, KeyError, OSError) as exc:
        print("BLOCKED: " + str(exc), file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
