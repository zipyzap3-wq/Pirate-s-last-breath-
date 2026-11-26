#!/usr/bin/env python3
"""Create .mcpack files and a correctly nested .mcaddon."""
import argparse,zipfile
from pathlib import Path

def pack(src,out):
    if not (src/"manifest.json").is_file(): raise SystemExit(f"Missing {src}/manifest.json")
    with zipfile.ZipFile(out,"w",zipfile.ZIP_DEFLATED,compresslevel=9) as z:
        for p in sorted(src.rglob("*")):
            if p.is_file(): z.write(p,p.relative_to(src).as_posix())

def main():
    ap=argparse.ArgumentParser(); ap.add_argument("--project",default="."); ap.add_argument("--output",default="build"); a=ap.parse_args()
    root=Path(a.project).resolve(); out=root/a.output; out.mkdir(parents=True,exist_ok=True)
    bp=[p for p in (root/"behavior_packs").iterdir() if p.is_dir() and (p/"manifest.json").exists()]
    rp=[p for p in (root/"resource_packs").iterdir() if p.is_dir() and (p/"manifest.json").exists()]
    if len(bp)!=1 or len(rp)!=1: raise SystemExit(f"Expected exactly one BP and RP; found {len(bp)} BP, {len(rp)} RP")
    b=out/(bp[0].name+".mcpack"); r=out/(rp[0].name+".mcpack"); addon=out/"Pirates_Breath_Test.mcaddon"
    pack(bp[0],b); pack(rp[0],r)
    with zipfile.ZipFile(addon,"w",zipfile.ZIP_DEFLATED,compresslevel=9) as z: z.write(b,b.name); z.write(r,r.name)
    with zipfile.ZipFile(addon) as z:
        if sorted(z.namelist())!=sorted([b.name,r.name]): raise SystemExit("MCAddon layout check failed")
    print(b); print(r); print(addon)
if __name__=="__main__": main()
