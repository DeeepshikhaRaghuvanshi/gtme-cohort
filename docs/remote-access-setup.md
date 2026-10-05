# Remote access for Deepu: ON HOLD (paused 5 Oct 2026)

**Goal:** Deepu connects from her own machine to a terminal and file explorer on Abi's PC (WSL), scoped to her own folder, and runs Claude Code there.

**Chosen design (agreed 5 Oct):** a separate Linux user **`deepu`** inside Abi's WSL, running a **VS Code Remote Tunnel** (`saffron-gtm`) as the systemd service `code-tunnel-deepu`.
- She connects through vscode.dev or the VS Code app → Remote Explorer → Tunnels, signed in with her GitHub.
- She sees only `/home/deepu`, with her own clone at `/home/deepu/gtme-cohort`. Abi's home is 750, so his keys and client folders stay private.
- The two clones sync through the GitHub repo (pull before, push after).

## Progress
- [x] Design agreed (separate user, not a tunnel as `abim`)
- [x] `scripts/setup_remote_user.sh` written, syntax-checked and committed. It creates the user with password login locked, copies Deepu's GitHub SSH key, sets her git identity, clones the repo, installs the VS Code CLI and writes the systemd unit. The VS Code CLI download URL was verified (HTTP 200).
- [ ] **Nothing has been run on the machine yet.** No `deepu` user exists.

## Requirements
- Abi runs the sudo steps in his own WSL terminal; they need his password.
- Deepu's GitHub login for the tunnel, via a device code at github.com/login/device (no browser popup on Abi's PC).
- WSL systemd is enabled (it is). The Windows PC has to be on with WSL running for the tunnel to be reachable.
- Deepu's own Claude account for Claude Code inside the tunnel. She installs Claude Code in her user with the current one-line installer from Anthropic's docs.
- Optional for her user: `pip install --user python-docx openpyxl pillow`; `scripts/setup_video_tools.sh` (ffmpeg is already installed system-wide).

## Steps to resume
1. `cd ~/workspace/deepu/gtme-cohort && sudo bash scripts/setup_remote_user.sh`
2. `sudo -iu deepu code tunnel user login --provider github`, then Deepu enters the code at github.com/login/device.
3. `sudo systemctl enable --now code-tunnel-deepu`
4. Deepu: vscode.dev → "Open Remote Tunnel" → `saffron-gtm` → open `/home/deepu/gtme-cohort`; install and sign in to Claude Code there.

## Caveats
- Her session doesn't get Abi's global `~/.claude/CLAUDE.md`, his Claude memory, or his rclone Drive remotes. The repo's CLAUDE.md, HANDOFF.md and `docs/claude-memory/` carry the essentials.
- She shares the WSL VM's 16 GB RAM / 8 threads with Abi's Docker containers and sessions.
- To undo: `sudo systemctl disable --now code-tunnel-deepu`, then `sudo rm /etc/systemd/system/code-tunnel-deepu.service`, then `sudo userdel -r deepu`.
