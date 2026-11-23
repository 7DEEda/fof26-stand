import re
# Kleine SVG-Bibliothek fuer die Signallaufplaene
from xml.sax.saxutils import escape as E
COL={'eth':'#4a90ff','dmx':'#35c46a','kombi':'#ff9f1a','hyb':'#19c9b0','patt':'#b07cff','usb':'#9a9a9a','hdmi':'#ff4fa3',
     'cee':'#e5484d','han':'var(--sp-fg)','L1':'#c9853f','L2':'var(--sp-l2)','L3':'#7f95ad','sch':'#f2c230','pe':'#8bc34a',
     'nf':'#f2c230','lsa':'#ff8a3c','lsb':'#4fc3f7','T':'#1ec8ff','H':'#ffb020','Q':'#5fd870','C':'#b48cff','A':'#ffb45a','PL':'#ff6ad5'}
DASH={'hyb':'9 5','usb':'','pe':'10 4 2 4'}
def tw(s,size,bold=False): return len(s)*size*(0.585 if bold else 0.54)
class Svg:
    def __init__(s,w,h,title,sub1,sub2,idp):
        s.w=w;s.h=h;s.o=[];s.top=[];s.idp=idp
        s.o.append(f'<rect x="30" y="26" width="7" height="34" fill="#801624"/>')
        s.text(48,53,title,26,'t',w=900)
        s.text(w-30,40,sub1,13.5,'m',anchor='end');s.text(w-30,59,sub2,13.5,'m',anchor='end')
        s.o.append(f'<line class="hr" x1="30" y1="78" x2="{w-30}" y2="78"/>')
    def text(s,x,y,t,size=13,cls='t',anchor='start',w=400,ls=None,top=False):
        a='' if anchor=='start' else f' text-anchor="{anchor}"'
        l='' if ls is None else f' letter-spacing="{ls}"'
        (s.top if top else s.o).append(f'<text class="{cls}" x="{x}" y="{y}" font-size="{size}" font-weight="{w}"{a}{l}>{E(t)}</text>')
    def zone(s,x,y,w,h,label):
        s.o.append(f'<rect class="zone" x="{x}" y="{y}" width="{w}" height="{h}" rx="10"/>')
        lw=tw(label,11.5,True)+len(label)*0.9+16
        s.o.append(f'<rect class="bg" x="{x+12}" y="{y-9}" width="{lw}" height="18"/>')
        s.text(x+20,y+4,label,11.5,'m',w=800,ls='0.08em')
    def box(s,x,y,w,h,title,subs=(),dashed=False,accent=None):
        d=' stroke-dasharray="6 4"' if dashed else ''
        s.o.append(f'<rect class="dev" x="{x}" y="{y}" width="{w}" height="{h}" rx="8"{d}/>')
        if accent: s.o.append(f'<rect x="{x}" y="{y+8}" width="4" height="{h-16}" fill="{accent}"/>')
        ty=y+24 if subs else y+h/2+5
        s.text(x+14,ty,title,15,'t',w=700)
        for i,t in enumerate(subs): s.text(x+14,ty+19+i*17,t,12.5,'m')
    def chip(s,x,y,idt,sub,col,w=80,h=46):
        s.o.append(f'<rect class="chip" x="{x}" y="{y}" width="{w}" height="{h}" rx="6" stroke="{col}"/>')
        s.text(x+w/2,y+(20 if sub else h/2+5),idt,14.5,'t',anchor='middle',w=800)
        if sub: s.text(x+w/2,y+37,sub,11.5,'m',anchor='middle')
    def wire(s,pts,kind,width=3,label=None,lpos=None,arrow=True,sub=None):
        c=COL[kind];d=DASH.get(kind,'');da=f' stroke-dasharray="{d}"' if d else ''
        p=' '.join(f'{x},{y}' for x,y in pts)
        s.o.append(f'<polyline class="w" points="{p}" stroke="{c}" stroke-width="{width}"{da}/>')
        if arrow:
            (x1,y1),(x2,y2)=pts[-2],pts[-1];a=9
            if x2>x1: tri=f'{x2},{y2} {x2-a},{y2-5} {x2-a},{y2+5}'
            elif x2<x1: tri=f'{x2},{y2} {x2+a},{y2-5} {x2+a},{y2+5}'
            elif y2>y1: tri=f'{x2},{y2} {x2-5},{y2-a} {x2+5},{y2-a}'
            else: tri=f'{x2},{y2} {x2-5},{y2+a} {x2+5},{y2+a}'
            s.top.append(f'<polygon points="{tri}" fill="{c}"/>')
        if label:
            lx,ly=lpos;w=tw(label,12,True)+18
            s.top.append(f'<rect class="pill" x="{lx-w/2}" y="{ly-11}" width="{w}" height="22" rx="11" stroke="{c}"/>')
            s.text(lx,ly+4.5,label,12,'t',anchor='middle',w=700,top=True)
            if sub: s.text(lx,ly+27,sub,11.5,'m',anchor='middle',top=True)
    def legend(s,y,items):
        x=30
        s.text(x,y+4,'LEGENDE',11.5,'m',w=800,ls='0.08em');x+=90
        for kind,label,width in items:
            c=COL[kind];d=DASH.get(kind,'');da=f' stroke-dasharray="{d}"' if d else ''
            s.o.append(f'<line x1="{x}" y1="{y}" x2="{x+38}" y2="{y}" stroke="{c}" stroke-width="{width}" stroke-linecap="round"{da}/>')
            s.text(x+46,y+4.5,label,12.5,'t');x+=46+tw(label,12.5)+30
    def notes(s,x,y,w,title,items,cols=1,size=12.5,lh=17):
        s.text(x,y,title,11.5,'m',w=800,ls='0.08em')
        cw=(w-(cols-1)*30)/cols;maxc=int(cw/(size*0.52))
        per=(len(items)+cols-1)//cols;yy=[y+24]*cols
        for i,t in enumerate(items):
            c=i//per;cx=x+c*(cw+30)
            t=re.sub(r'(\d) (?=(W|A|m|kW|Hz|dB|dBu|Zoll|Ohm|x|s|V|t|mm|cm|Kanäle|Stück)\b|%)','\\1\u00a0',t);t=re.sub(r'\b(ID|Box|Kreis|Universum|Driver) (?=\d)','\\1\u00a0',t)
            words=t.split(' ');lines=[];cur=''
            for wd in words:
                if len(cur)+len(wd)+1>maxc-3: lines.append(cur);cur=wd
                else: cur=(cur+' '+wd).strip()
            lines.append(cur)
            s.text(cx,yy[c],str(i+1)+'.',size,'t',w=800)
            for l in lines: s.text(cx+20,yy[c],l,size,'t' );yy[c]+=lh
            yy[c]+=5
        return max(yy)
    def raw(s,x): s.o.append(x)
    def out(s):
        return (f'<svg class="sp" id="{s.idp}" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {s.w} {s.h}" role="img"><rect class="bg" x="0" y="0" width="{s.w}" height="{s.h}"/>'+''.join(s.o)+''.join(s.top)+'</svg>')
CSS='''.sp{font-family:"Helvetica Neue",Arial,sans-serif;display:block}
.sp .bg{fill:var(--sp-bg)}.sp .t{fill:var(--sp-fg)}.sp .m{fill:var(--sp-mut)}
.sp .hr{stroke:var(--sp-line);stroke-width:1.5}
.sp .dev{fill:var(--sp-panel);stroke:var(--sp-line);stroke-width:1.5}
.sp .chip{fill:var(--sp-panel);stroke-width:2}
.sp .zone{fill:none;stroke:var(--sp-zone);stroke-width:1.3;stroke-dasharray:6 5}
.sp .w{fill:none;stroke-linejoin:round;stroke-linecap:round}
.sp .pill{fill:var(--sp-bg);stroke-width:1.5}
.sp .barbg{fill:var(--sp-line)}
'''
DARK=':root{--sp-bg:#141414;--sp-panel:#212121;--sp-line:#3d3d3d;--sp-fg:#fafafa;--sp-mut:#b0b0b0;--sp-zone:#666;--sp-l2:#e6e6e6}'
LIGHT=':root{--sp-bg:#ffffff;--sp-panel:#f4f4f4;--sp-line:#bdbdbd;--sp-fg:#111111;--sp-mut:#555555;--sp-zone:#8a8a8a;--sp-l2:#222222}'
