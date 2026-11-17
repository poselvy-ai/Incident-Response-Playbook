"""Render diagrams/src -> diagrams/*.png. Usage: python3 diagrams/src/render.py (from repo root)."""
import subprocess, pathlib
from playwright.sync_api import sync_playwright
src = pathlib.Path(__file__).parent; out = src.parent
for m in ["escalation-path", "incident-lifecycle"]:
    subprocess.run(["mmdc", "-i", str(src/f"{m}.mmd"), "-o", str(out/f"{m}.png"), "-c", str(src/"mmd-config.json"), "-b", "white", "-s", "2"], check=True)
with sync_playwright() as p:
    b = p.chromium.launch(executable_path="/usr/bin/google-chrome")
    pg = b.new_page(device_scale_factor=2, viewport={"width": 1300, "height": 900})
    for h in ["severity-matrix", "escalation-workflow"]:
        pg.goto((src/f"{h}.html").resolve().as_uri())
        box = pg.evaluate("(()=>{const r=document.body.getBoundingClientRect();const t=document.querySelector('table');const tr=t.getBoundingClientRect();const l=document.querySelector('.legend span:last-child');const lb=l?l.getBoundingClientRect():tr;return {w:Math.ceil(Math.max(tr.right,lb.right)+24),h:Math.ceil(Math.max(tr.bottom,lb.bottom)+24)}})()")
        pg.screenshot(path=str(out/f"{h}.png"), clip={"x":0,"y":0,"width":box["w"],"height":box["h"]})
    b.close()
print("rendered")
