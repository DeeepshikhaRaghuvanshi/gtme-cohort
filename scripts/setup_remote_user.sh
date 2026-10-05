#!/usr/bin/env bash
# Abi's WSL machine only. Creates a scoped Linux user "deepu" for Deepu's remote access via a VS Code tunnel.
# Run once:  sudo bash scripts/setup_remote_user.sh
# She sees only /home/deepu (Abi's home is 750). Her clone syncs with Abi's through the GitHub repo.
set -euo pipefail
[ "$(id -u)" -eq 0 ] || { echo "Run with sudo"; exit 1; }

U=deepu
H=/home/$U
SRC_KEY=/home/abim/.ssh/id_ed25519_deepu
REPO=git@github.com:DeeepshikhaRaghuvanshi/gtme-cohort.git
TUNNEL_NAME=saffron-gtm

# 1. User with no password login (access is only through the tunnel or sudo -iu deepu)
id "$U" >/dev/null 2>&1 || useradd -m -s /bin/bash "$U"
passwd -l "$U" >/dev/null

# 2. Her own copy of her GitHub SSH key, and her git identity
install -d -m 700 -o "$U" -g "$U" "$H/.ssh"
install -m 600 -o "$U" -g "$U" "$SRC_KEY" "$H/.ssh/id_ed25519"
install -m 644 -o "$U" -g "$U" "$SRC_KEY.pub" "$H/.ssh/id_ed25519.pub"
cat > "$H/.ssh/config" <<'EOF'
Host github.com
  HostName github.com
  User git
  IdentityFile ~/.ssh/id_ed25519
  IdentitiesOnly yes
  StrictHostKeyChecking accept-new
EOF
chown "$U:$U" "$H/.ssh/config"; chmod 600 "$H/.ssh/config"
sudo -u "$U" git config --global user.name "Deepshikha Raghuvanshi"
sudo -u "$U" git config --global user.email "ddeepshikha.raghuvanshi@gmail.com"
sudo -u "$U" git config --global pull.rebase true

# 3. Her clone of the repo
[ -d "$H/gtme-cohort/.git" ] || sudo -u "$U" -H git clone -q "$REPO" "$H/gtme-cohort"

# 4. VS Code CLI (standalone, no GUI)
install -d -o "$U" -g "$U" "$H/.local/bin"
if [ ! -x "$H/.local/bin/code" ]; then
  tmp=$(mktemp -d)
  curl -fsSL "https://code.visualstudio.com/sha/download?build=stable&os=cli-alpine-x64" -o "$tmp/cli.tgz"
  tar -xzf "$tmp/cli.tgz" -C "$tmp"
  install -m 755 -o "$U" -g "$U" "$tmp/code" "$H/.local/bin/code"
  rm -rf "$tmp"
fi
grep -q '.local/bin' "$H/.bashrc" || echo 'export PATH="$HOME/.local/bin:$PATH"' >> "$H/.bashrc"

# 5. systemd service for the tunnel (enabled only after the GitHub login step)
cat > /etc/systemd/system/code-tunnel-deepu.service <<EOF
[Unit]
Description=VS Code tunnel for Deepu ($TUNNEL_NAME)
After=network-online.target

[Service]
User=$U
WorkingDirectory=$H/gtme-cohort
ExecStart=$H/.local/bin/code tunnel --accept-server-license-terms --name $TUNNEL_NAME
Restart=on-failure
RestartSec=10

[Install]
WantedBy=multi-user.target
EOF
systemctl daemon-reload

cat <<EOF

Done. User '$U' is ready; her repo is at $H/gtme-cohort.
Next (needs Deepu's GitHub login, via a device code, no browser popup here):
  sudo -iu $U code tunnel user login --provider github
Then start the tunnel and keep it running with WSL:
  sudo systemctl enable --now code-tunnel-deepu
EOF
