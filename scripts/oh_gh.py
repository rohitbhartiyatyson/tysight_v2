#!/usr/bin/env python3
"""
Tiny GitHub helper for REST operations used by microagents.
Usage: python scripts/oh_gh.py create_pr <owner> <repo> <head_branch> <base_branch> <title> <body>
Environment: expects GITHUB_TOKEN in env.
Timeouts: 15s per request.
"""
import os, sys, json, urllib.request, urllib.error, urllib.parse, time

def api_request(method, path, data=None, timeout=15):
    token = os.environ.get('GITHUB_TOKEN') or os.environ.get('github_token')
    if not token:
        print(json.dumps({'error': 'no_token'}))
        sys.exit(2)
    url = 'https://api.github.com' + path
    headers = {'Authorization': f'token {token}', 'Accept': 'application/vnd.github.v3+json', 'User-Agent': 'oh-gh-helper'}
    req = urllib.request.Request(url, data=(json.dumps(data).encode() if data else None), headers=headers, method=method)
    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            return json.load(resp)
    except urllib.error.HTTPError as e:
        try:
            return json.load(e)
        except Exception:
            return {'error': str(e), 'code': e.code}
    except Exception as e:
        return {'error': str(e)}

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print(json.dumps({'error': 'no_command'}))
        sys.exit(1)
    cmd = sys.argv[1]
    if cmd == 'create_pr':
        if len(sys.argv) < 8:
            print(json.dumps({'error': 'usage'}))
            sys.exit(1)
        owner, repo, head, base, title, body = sys.argv[2:8]
        path = f'/repos/{owner}/{repo}/pulls'
        data = {'title': title, 'head': head, 'base': base, 'body': body}
        out = api_request('POST', path, data=data)
        print(json.dumps(out))
    elif cmd == 'list_prs':
        if len(sys.argv) < 6:
            print(json.dumps({'error': 'usage'}))
            sys.exit(1)
        owner, repo, head, base = sys.argv[2:6]
        path = f'/repos/{owner}/{repo}/pulls?head={owner}:{head}&base={base}&state=open'
        out = api_request('GET', path)
        print(json.dumps(out))
    else:
        print(json.dumps({'error': 'unknown_cmd'}))
        sys.exit(1)
