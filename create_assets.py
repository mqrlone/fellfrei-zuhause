from pathlib import Path
import math, subprocess
assets=Path('/opt/data/fellfrei-zuhause-site/assets')
assets.mkdir(exist_ok=True)

def svg(name, content):
    (assets/name).write_text(content, encoding='utf-8')

base_defs='''<defs>
  <linearGradient id="sand" x1="0" x2="1" y1="0" y2="1"><stop offset="0" stop-color="#fbf5ec"/><stop offset=".58" stop-color="#d6c5ae"/><stop offset="1" stop-color="#bda78c"/></linearGradient>
  <linearGradient id="sage" x1="0" x2="1"><stop offset="0" stop-color="#a9c2af"/><stop offset="1" stop-color="#718d7a"/></linearGradient>
  <linearGradient id="bg" x1="0" x2="1" y1="0" y2="1"><stop offset="0" stop-color="#fbfaf7"/><stop offset="1" stop-color="#ede7de"/></linearGradient>
  <filter id="shadow" x="-20%" y="-20%" width="140%" height="150%"><feDropShadow dx="0" dy="26" stdDeviation="24" flood-color="#000" flood-opacity=".20"/></filter>
  <filter id="soft" x="-20%" y="-20%" width="140%" height="140%"><feGaussianBlur stdDeviation="18"/></filter>
</defs>'''

hairs = ''.join(f'<path d="M{220+(i*97)%930} {455+(i*53)%190} q {35-((i*9)%70)} {-24+((i*13)%45)} {82-((i*7)%40)} {10-((i*5)%25)}"/>' for i in range(34))

svg('product-hero.svg', f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1600 900" role="img" aria-label="Fellfrei Zuhause Tierhaar-Entferner Produktfoto">{base_defs}
<rect width="1600" height="900" fill="url(#bg)"/>
<ellipse cx="800" cy="670" rx="455" ry="70" fill="#000" opacity=".10" filter="url(#soft)"/>
<g filter="url(#shadow)" transform="translate(455 360) rotate(-8 350 90)">
  <rect x="0" y="0" width="720" height="178" rx="89" fill="url(#sand)"/>
  <rect x="76" y="47" width="428" height="84" rx="42" fill="#fff" opacity=".48"/>
  <rect x="526" y="38" width="128" height="102" rx="48" fill="url(#sage)" opacity=".95"/>
  <path d="M592 60c24 18 34 54 6 78" fill="none" stroke="#e9f2eb" stroke-width="16" stroke-linecap="round" opacity=".55"/>
</g>
<g opacity=".55" stroke="#b7b1aa" stroke-width="7" stroke-linecap="round"><path d="M350 315c60-18 100 18 142-10"/><path d="M1110 282c74 18 94-28 145 2"/><path d="M985 648c88-24 122 18 185-10"/></g>
</svg>''')

svg('sofa-before.svg', f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1400 900" role="img" aria-label="Sofa mit Tierhaaren vor der Reinigung">{base_defs}
<rect width="1400" height="900" fill="#eee5da"/>
<rect x="150" y="420" width="1100" height="260" rx="60" fill="#b99f87"/><rect x="105" y="600" width="1190" height="130" rx="55" fill="#9c7e63"/>
<rect x="210" y="340" width="360" height="220" rx="55" fill="#c9b19b"/><rect x="830" y="340" width="360" height="220" rx="55" fill="#c9b19b"/>
<g stroke="#f8f8f5" stroke-width="9" stroke-linecap="round" opacity=".92">{hairs}</g>
<text x="72" y="96" font-family="system-ui,-apple-system,Segoe UI,sans-serif" font-size="42" font-weight="700" fill="#1d1d1f">Vorher</text>
</svg>''')

svg('sofa-after.svg', f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1400 900" role="img" aria-label="Sauberes Sofa nach der Reinigung">{base_defs}
<rect width="1400" height="900" fill="#e7f0e7"/>
<rect x="150" y="420" width="1100" height="260" rx="60" fill="#b99f87"/><rect x="105" y="600" width="1190" height="130" rx="55" fill="#9c7e63"/>
<rect x="210" y="340" width="360" height="220" rx="55" fill="#c9b19b"/><rect x="830" y="340" width="360" height="220" rx="55" fill="#c9b19b"/>
<g fill="#fff" opacity=".86"><path d="M690 265l24 54 58 7-43 39 12 58-51-30-51 30 12-58-43-39 58-7z"/><circle cx="520" cy="280" r="13"/><circle cx="890" cy="325" r="10"/></g>
<text x="72" y="96" font-family="system-ui,-apple-system,Segoe UI,sans-serif" font-size="42" font-weight="700" fill="#1d1d1f">Nachher</text>
</svg>''')

svg('auto-seat.svg', f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1400 900" role="img" aria-label="Tierhaar-Entferner auf Autositz">{base_defs}
<rect width="1400" height="900" fill="#f6f3ee"/>
<path d="M350 180h520c70 0 120 55 110 124L905 800H265l-30-485c-5-76 42-135 115-135z" fill="#303235"/>
<path d="M430 235h360c52 0 90 41 84 92l-50 410H360l-25-405c-4-55 36-97 95-97z" fill="#484b50"/>
<g stroke="#d7d7d7" stroke-width="7" stroke-linecap="round" opacity=".72"><path d="M420 510c55-20 80 20 130-7"/><path d="M630 450c70 12 100-15 145 4"/><path d="M500 635c90-28 112 12 160-12"/></g>
<g filter="url(#shadow)" transform="translate(745 525) rotate(-15)"><rect width="360" height="92" rx="46" fill="url(#sand)"/><rect x="45" y="24" width="210" height="44" rx="22" fill="#fff" opacity=".45"/><rect x="264" y="18" width="64" height="56" rx="24" fill="url(#sage)"/></g>
<text x="76" y="104" font-family="system-ui,-apple-system,Segoe UI,sans-serif" font-size="42" font-weight="700" fill="#1d1d1f">Perfekt fürs Auto</text>
</svg>''')

svg('bundle.svg', f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1400 900" role="img" aria-label="2er Set Tierhaar-Entferner">{base_defs}
<rect width="1400" height="900" fill="url(#bg)"/><ellipse cx="700" cy="680" rx="460" ry="75" fill="#000" opacity=".10" filter="url(#soft)"/>
<g filter="url(#shadow)" transform="translate(305 360) rotate(-14)"><rect width="580" height="142" rx="71" fill="url(#sand)"/><rect x="58" y="36" width="330" height="70" rx="35" fill="#fff" opacity=".42"/><rect x="420" y="31" width="96" height="80" rx="34" fill="url(#sage)"/></g>
<g filter="url(#shadow)" transform="translate(560 410) rotate(9)"><rect width="580" height="142" rx="71" fill="url(#sand)"/><rect x="58" y="36" width="330" height="70" rx="35" fill="#fff" opacity=".42"/><rect x="420" y="31" width="96" height="80" rx="34" fill="url(#sage)"/></g>
<text x="76" y="104" font-family="system-ui,-apple-system,Segoe UI,sans-serif" font-size="42" font-weight="700" fill="#1d1d1f">Zuhause + Auto Set</text>
</svg>''')

# MP4 demo via generated PPM frames
frames=assets/'frames'; frames.mkdir(exist_ok=True)
W,H=1280,720

def rgb(hex):
    hex=hex.lstrip('#'); return tuple(int(hex[i:i+2],16) for i in (0,2,4))
def blend(c1,c2,t): return tuple(int(c1[i]*(1-t)+c2[i]*t) for i in range(3))
def draw_rect(pix,x0,y0,x1,y1,c):
    x0=max(0,int(x0)); y0=max(0,int(y0)); x1=min(W,int(x1)); y1=min(H,int(y1))
    for y in range(y0,y1):
        row=pix[y]
        for x in range(x0,x1): row[x]=c
def draw_circle(pix,cx,cy,r,c):
    cx=int(cx); cy=int(cy); r=int(r); r2=r*r
    for y in range(max(0,cy-r), min(H,cy+r+1)):
        dy=(y-cy)*(y-cy); row=pix[y]
        for x in range(max(0,cx-r), min(W,cx+r+1)):
            if (x-cx)*(x-cx)+dy<=r2: row[x]=c
def draw_line(pix,x0,y0,x1,y1,c,w=3):
    steps=max(abs(int(x1-x0)),abs(int(y1-y0)),1)
    for i in range(steps+1):
        t=i/steps; draw_circle(pix,x0+(x1-x0)*t,y0+(y1-y0)*t,w,c)
for f in range(90):
    pix=[]
    for y in range(H):
        pix.append([blend(rgb('#fbfaf7'), rgb('#ded2bf'), (y/H)*.55)]*W)
    draw_rect(pix,180,360,1100,535,rgb('#b99f87')); draw_rect(pix,135,500,1145,610,rgb('#9c7e63'))
    progress=f/89
    hair_positions=[(230+(i*83)%820,390+(i*47)%115, 280+(i*83)%820, 402+(i*31)%80) for i in range(28)]
    cutoff=180+progress*860
    for x0,y0,x1,y1 in hair_positions:
        if x0>cutoff-80: draw_line(pix,x0,y0,x1,y1,rgb('#f9f9f4'),3)
    tx=140+progress*790; ty=310+math.sin(progress*math.pi)*30
    draw_rect(pix,tx,ty,tx+300,ty+74,rgb('#d6c5ae')); draw_circle(pix,tx+37,ty+37,37,rgb('#d6c5ae')); draw_circle(pix,tx+263,ty+37,37,rgb('#d6c5ae'))
    draw_rect(pix,tx+46,ty+20,tx+205,ty+54,rgb('#f7f1e7')); draw_rect(pix,tx+220,ty+16,tx+270,ty+58,rgb('#8fa996'))
    if f>65:
        draw_circle(pix,640,240,8,rgb('#ffffff')); draw_circle(pix,720,265,5,rgb('#ffffff'))
    path=frames/f'frame_{f:03d}.ppm'
    with path.open('wb') as out:
        out.write(f'P6\n{W} {H}\n255\n'.encode())
        out.write(bytes([v for row in pix for px in row for v in px]))
subprocess.run(['ffmpeg','-y','-framerate','30','-i',str(frames/'frame_%03d.ppm'),'-c:v','libx264','-pix_fmt','yuv420p','-movflags','+faststart',str(assets/'tierhaar-demo.mp4')], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
for p in frames.glob('*.ppm'): p.unlink()
frames.rmdir()
print('assets_created', sorted(p.name for p in assets.iterdir()))
