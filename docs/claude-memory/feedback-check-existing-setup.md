---
name: feedback-check-existing-setup
description: "Check Abi's existing setup docs/config before installing tools or asking for credentials; GitHub is SSH via includeIf, never gh CLI"
metadata:
  node_type: memory
  type: feedback
  originSessionId: b2f209e2-18a4-4623-ad2e-e3a33a89146a
  modified: 2026-10-05T13:53:55.547Z
---

Before installing tooling or asking Abi for credentials, check what's already set up: `~/workspace/*.md` setup docs (e.g. `~/workspace/SSH-Multi-Account-Setup.md`), `~/.ssh/config` and `~/.gitconfig` with its `includeIf` files. GitHub access uses SSH keys per folder (`~/workspace/deepu/` → `~/.gitconfig-deepu` → `id_ed25519_deepu` + Deepu's identity). **No gh CLI**; Abi doesn't use it.

**Why:** On 2026-10-05 Claude installed gh and asked for a personal access token to push Deepu's repo. Abi pointed out that the SSH setup was already documented and working, and asked for gh to be removed so it wouldn't confuse future sessions.

**How to apply:** For any repo under `~/workspace/deepu/`, just use `git` with a `git@github.com:` remote. Identity and key resolve automatically. Never install or suggest gh. Related: [[deepu-gtme-catchup]]
