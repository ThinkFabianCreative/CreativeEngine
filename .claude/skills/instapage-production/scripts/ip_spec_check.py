#!/usr/bin/env python3
"""Lint a Figma annotation snapshot; explicit repetition, never implicit inheritance.
Snapshot format: {policy:'explicit-repeat',desktop:[{name,annotations:[{category,label}],text}],mobile:[...]}
This checks annotation/ID parity, not approved copy or Instapage implementation.
"""
import html
import json
import re
import sys


def identity(name):
    match = re.match(r'^(B\d+(?:\.C\d+(?:\.S)?)?|E\d+)\b', name)
    if match:
        return match.group(1)
    return name if name.startswith(('Field ·', 'Submit ·')) else None


def lint(data):
    errors=[]
    if data.get('policy')!='explicit-repeat':
        errors.append('policy must be explicit-repeat; inheritance is not implemented')
    maps={}
    for device in ('desktop','mobile'):
        nodes=data.get(device,[]); indexed={}
        if not nodes: errors.append(device+': missing nodes')
        for node in nodes:
            key=identity(node.get('name',''))
            if not key:
                errors.append(device+': missing stable ID');continue
            if key in indexed: errors.append(device+': duplicate '+key)
            indexed[key]=node
        maps[device]=indexed
    d,m=maps['desktop'],maps['mobile']
    if set(d)!=set(m): errors.append('device IDs differ: '+str(sorted(set(d)^set(m))))
    blocks=lambda a:[k for k in a if re.fullmatch(r'B\d+',k)]
    if blocks(d)!=blocks(m): errors.append('block order differs')
    for key in d.keys() & m.keys():
        shared={(a.get('category'),html.unescape(a.get('label',''))) for a in d[key].get('annotations',[])}
        repeated={(a.get('category'),html.unescape(a.get('label',''))) for a in m[key].get('annotations',[])}
        if not shared<=repeated: errors.append(key+': shared annotations missing or changed on mobile')
        if (key.startswith(('E','Field ·','Submit ·')) and d[key].get('text')!=m[key].get('text')):
            errors.append(key+': content differs; requires explicit approved device copy mapping')
    return errors


if __name__=='__main__':
    try:
        errors=lint(json.load(open(sys.argv[1],encoding='utf-8')))
    except (IndexError,ValueError,OSError,TypeError) as exc:
        errors=[str(exc)]
    print(json.dumps({'pass':not errors,'errors':errors},indent=2))
    sys.exit(bool(errors))
