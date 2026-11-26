#!/usr/bin/env python3
"""Static Bedrock pack audit; Python standard library only."""
import argparse,json,os,re,sys
from pathlib import Path

def strip_jsonc(s):
    out=[]; i=0; quote=None; esc=False
    while i<len(s):
        c=s[i]; n=s[i+1] if i+1<len(s) else ""
        if quote:
            out.append(c)
            if esc: esc=False
            elif c=="\\": esc=True
            elif c==quote: quote=None
            i+=1; continue
        if c in ('"',"'"): quote=c; out.append(c); i+=1; continue
        if c=="/" and n=="/":
            i+=2
            while i<len(s) and s[i] not in "\r\n": i+=1
            continue
        if c=="/" and n=="*":
            i+=2
            while i+1<len(s) and s[i:i+2]!="*/": i+=1
            i=min(len(s),i+2); continue
        out.append(c); i+=1
    s="".join(out); out=[]; i=0; quote=None; esc=False
    while i<len(s):
        c=s[i]
        if quote:
            out.append('"' if quote=="'" and c==quote else c)
            if esc: esc=False
            elif c=="\\": esc=True
            elif c==quote: quote=None
            i+=1; continue
        if c in ('"',"'"): quote=c; out.append('"'); i+=1; continue
        if c==",":
            j=i+1
            while j<len(s) and s[j].isspace(): j+=1
            if j<len(s) and s[j] in "}]": i+=1; continue
        out.append(c); i+=1
    return "".join(out)

def parse(p): return json.loads(strip_jsonc(p.read_text(encoding="utf-8-sig")))
def imports(pack):
    rx=re.compile(r'(?:\\bfrom\\s*|\\bimport\\s*)[\'"]([^\'"]+)[\'"]')
    count=0; missing=[]
    for p in (pack/"scripts").rglob("*") if (pack/"scripts").exists() else []:
        if p.suffix not in (".js",".mjs",".ts"): continue
        count+=1
        for spec in rx.findall(p.read_text(encoding="utf-8",errors="replace")):
            if not spec.startswith("."): continue
            q=p.parent/spec
            if not any(x.is_file() for x in (q,q.with_suffix(".js"),q.with_suffix(".mjs"),q.with_suffix(".ts"),q/"index.js",q/"index.ts")):
                missing.append((p.relative_to(pack).as_posix(),spec))
    return count,missing

def main():
    ap=argparse.ArgumentParser(); ap.add_argument("--project",default="."); ap.add_argument("--report",default="build/audit-report.json")
    a=ap.parse_args(); root=Path(a.project).resolve(); packs=[]
    for group in ("behavior_packs","resource_packs"):
        parent=root/group
        if not parent.exists(): continue
        for pack in parent.iterdir():
            if not pack.is_dir() or not (pack/"manifest.json").exists(): continue
            row={"pack":pack.name,"files":sum(x.is_file() for x in pack.rglob("*")),"json_files":0,"json_errors":[]}
            try: row["manifest"]=parse(pack/"manifest.json")
            except Exception as e: row["json_errors"].append(["manifest.json",str(e)])
            for p in pack.rglob("*.json"):
                row["json_files"]+=1
                try: parse(p)
                except Exception as e: row["json_errors"].append([p.relative_to(pack).as_posix(),str(e)])
            row["script_files"],row["missing_imports"]=imports(pack); packs.append(row)
    by_uuid={r.get("manifest",{}).get("header",{}).get("uuid") for r in packs if r.get("manifest")}
    for r in packs:
        for dep in r.get("manifest",{}).get("dependencies",[]):
            if isinstance(dep,dict) and dep.get("uuid") and dep["uuid"] not in by_uuid:
                r.setdefault("dependency_errors",[]).append(dep["uuid"])
    totals={"packs":len(packs),"files":sum(x["files"] for x in packs),"json_files":sum(x["json_files"] for x in packs),
      "json_errors":sum(len(x["json_errors"]) for x in packs),"missing_imports":sum(len(x["missing_imports"]) for x in packs),
      "dependency_errors":sum(len(x.get("dependency_errors",[])) for x in packs)}
    report={"project":str(root),"totals":totals,"packs":packs}; out=root/a.report; out.parent.mkdir(parents=True,exist_ok=True); out.write_text(json.dumps(report,indent=2),encoding="utf-8")
    print(json.dumps(totals,indent=2))
    for p in packs:
        for e in p["json_errors"][:25]: print("JSON ERROR",p["pack"],e)
        for e in p["missing_imports"][:25]: print("MISSING IMPORT",p["pack"],e)
        for e in p.get("dependency_errors",[]): print("MISSING DEPENDENCY",p["pack"],e)
    return 1 if any(totals[k] for k in ("json_errors","missing_imports","dependency_errors")) else 0
if __name__=="__main__": sys.exit(main())
