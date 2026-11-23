import sys;sys.path.insert(0,'/tmp/plan')
from lib import *
SUB1='FoF 2026, TSE Stand, STATION Berlin, Halle 1'
SUB2='Auftrag 177433, Stand 23.11.2026, Material laut Packliste vom 21.11.2026'

def licht():
    s=Svg(1600,1131,'SIGNALLAUFPLAN LICHT',SUB1,SUB2,'spLicht')
    # Regie
    s.zone(30,104,300,470,'REGIE AN DER BAR')
    s.box(50,134,260,70,'Stream Deck+',['14 Stimmungen, 4 Drehregler'])
    s.box(50,262,260,108,'Show-Rechner',['Showcontrol, Art-Net mit 40 Hz','IP 2.0.0.10, Maske 255.0.0.0','sendet Universum 1, 2 und 3'],accent='#801624')
    s.box(50,440,260,62,'Switch A',['8 Port, an der Bar'])
    s.wire([(180,204),(180,262)],'usb',label='USB',lpos=(180,233))
    s.wire([(180,370),(180,440)],'eth',label='Cat5 1 m',lpos=(180,405))
    s.box(50,604,280-20,84,'AsteraBox ART7',['nur zum Adressieren der Astera:','Bluetooth zum Rechner, Funk zur Lampe'],dashed=True)
    # Technikpunkt
    s.zone(400,104,300,470,'TECHNIKPUNKT LINKE TRAVERSE OBEN')
    s.box(440,134,240,62,'Switch B',['8 Port'])
    s.box(440,250,240,120,'Titan PowerBox 1',['IP 2.0.0.21, Universum 1','Röhren: 8 von 10 Ausgängen','XLR IN frei lassen'],accent=COL['kombi'])
    s.box(440,424,240,120,'Titan PowerBox 2',['IP 2.0.0.22, Universum 2','Röhren: 6 von 10 Ausgängen','XLR IN frei lassen'],accent=COL['kombi'])
    s.wire([(310,462),(346,462),(346,156),(440,156)],'eth',label='Cat5 20 m',lpos=(346,318),sub=None)
    s.wire([(500,196),(500,250)],'eth',label='Cat5 1 m',lpos=(500,223))
    s.wire([(440,180),(424,180),(424,484),(440,484)],'eth',label='Cat5 1 m',lpos=(424,600),arrow=True) if False else s.wire([(440,180),(424,180),(424,484),(440,484)],'eth')
    s.text(432,400,'Cat5',10.5,'m',w=700);s.text(432,413,'1 m',10.5,'m',w=700)
    # Reihe 1: Lange Seite vorn
    s.text(790,116,'LANGE SEITE VORN, von der Ecke vorn links',11.5,'m',w=800,ls='0.08em')
    s.text(1570,116,'Kombikabel: T1 1,5 m, T2 bis T4 je 5 m, T5 bis H1 je 10 m',12.5,'m',anchor='end')
    ids=[('T1','1'),('T2','49'),('T3','97'),('T4','145'),('T5','193'),('T6','241'),('T7','289'),('H1','337')]
    for i,(n,a) in enumerate(ids):
        x=790+i*100;s.wire([(x+40,134),(x+40,154)],'kombi',arrow=True,width=2.5)
        s.chip(x,154,n,'Adr. '+a,COL['H' if n[0]=='H' else 'T'])
    s.wire([(680,290),(735,290),(735,134),(1530,134)],'kombi',arrow=False)
    # Reihe 2: Cluster
    s.text(790,262,'VORDERE TRAVERSE, von links',11.5,'m',w=800,ls='0.08em')
    s.text(1570,262,'DMX-Kette Universum 1: 8 x DMX 3 m',12.5,'m',anchor='end')
    for i in range(8):
        x=790+i*100
        if i: s.wire([(x-20,301),(x,301)],'dmx',arrow=False)
        s.chip(x,278,'C%d'%(i+1),'Adr. %d'%(361+19*i),COL['C'])
    s.wire([(680,340),(755,340),(755,301),(790,301)],'dmx')
    s.text(686,333,'DMX OUT',10.5,'m',w=700)
    s.text(686,283,'Röhren',10.5,'m',w=700)
    # Reihe 3: PB2 Roehren
    s.text(790,404,'HÖHE AM VORDEREN LINKEN BEIN, von oben',11.5,'m',w=800,ls='0.08em')
    s.text(1190,404,'TIEFE LINKS OBEN, von vorn',11.5,'m',w=800,ls='0.08em')
    grp=[(790,[('T8','1'),('T9','49'),('T10','97')]),(1190,[('T11','145'),('T12','193'),('H2','241')])]
    for x0,l in grp:
        for i,(n,a) in enumerate(l):
            x=x0+i*100;s.wire([(x+40,422),(x+40,442)],'kombi',width=2.5)
            s.chip(x,442,n,'Adr. '+a,COL['H' if n[0]=='H' else 'T'])
    s.wire([(680,464),(735,464),(735,422),(1430,422)],'kombi',arrow=False)
    s.text(790,508,'Kombikabel: T8 1,5 m, T9 und T10 je 5 m',12.5,'m');s.text(1190,508,'Kombikabel: T11 und T12 je 1,5 m, H2 5 m',12.5,'m')
    s.text(686,457,'Röhren',10.5,'m',w=700);s.text(686,507,'DMX OUT',10.5,'m',w=700)
    # Reihe 4: QuikSpots
    s.text(790,566,'QUIKSPOTS AUF DEN ROHREN P1 BIS P5, in Steckfolge',11.5,'m',w=800,ls='0.08em')
    s.text(1570,566,'DMX-Kette Universum 2, Adresse im Spot',12.5,'m',anchor='end')
    s.text(790,684,'Im Rohr: Hybridkabel 1,5 m (8 Stück). Rohrwechsel: DMX 3 m (4 Stück) und TRUE1 3 m.',12.5,'m')
    s.text(790,702,'Zwischen P3 und P4 nur DMX, P4 hat eine eigene Einspeisung.',12.5,'m')
    s.text(748,572,'DMX 5 m',11.5,'m',anchor='end')
    pipes=[[3,2,1],[4,5],[8,7,6],[9,10],[13,12,11]];x=790;first=True
    for pi,l in enumerate(pipes):
        x0=x
        for jn,n in enumerate(l):
            if not first: s.wire([(x-14,621),(x,621)],'hyb' if jn else 'dmx',arrow=False,width=3)
            first=False
            s.chip(x,598,'Q%d'%n,str(255+10*n),COL['Q'],w=46,h=46);x+=60
        x1=x-14
        s.raw(f'<path d="M{x0},{590} V{584} H{x1} V{590}" fill="none" stroke="var(--sp-mut)" stroke-width="1.3"/>')
        s.text((x0+x1)/2,658,'P%d: %s'%(pi+1,'vorn → hinten' if pi%2==0 else 'hinten → vorn'),10.5,'m',anchor='middle',w=700)
    s.wire([(680,514),(755,514),(755,621),(790,621)],'dmx')
    # Pixel Lines
    s.text(1084,722,'PIXEL LINES AM DISPLAY 98 ZOLL, in Steckfolge von rechts',11.5,'m',w=800,ls='0.08em')
    pl=[('PL3','453','rechts oben','3 m'),('PL4','482','rechts unten','5 m'),('PL2','424','links unten','3 m'),('PL1','395','links oben','')]
    for i,(n,a,p,cl) in enumerate(pl):
        x=1420-i*112
        if i: s.wire([(x+112,757),(x+80,757)],'dmx',arrow=True);s.text(x+96,750,pl[i-1][3],10.5,'m',anchor='middle',w=700)
        s.chip(x,734,n,'Adr. '+a,COL['PL']);s.text(x+40,796,p,11.5,'m',anchor='middle')
    s.wire([(1533,644),(1533,757),(1500,757)],'dmx')
    s.text(1546,704,'DMX',11.5,'m');s.text(1546,719,'5 m',11.5,'m')
    s.text(1084,818,'DMX: 5 m vom letzten Spot, 3 m, 5 m hinter dem Display, 3 m',12.5,'m')
    # PATT
    s.zone(400,826,300,262,'AN DER TRAVERSE, NEBEN DEN PATT')
    pos=['rechte Seite vorn','rechte Seite hinten','hinten rechts','hinten Mitte rechts']
    for i in range(4):
        y=848+i*58
        s.box(440,y,240,46,'PATT Driver %d'%(i+1),[],accent=COL['patt'])
        s.text(668,y+20,'2.0.0.%d'%(31+i),11.5,'m',anchor='end');s.text(668,y+36,'U3, Adr. %d'%(1+60*i),11.5,'m',anchor='end')
        if i: s.wire([(470,y-12),(470,y)],'eth',arrow=False)
        s.wire([(680,y+23),(900,y+23)],'patt',label='4-pol XLR 5 m',lpos=(790,y+23))
        s.chip(900,y,'A%d'%(i+1),None,COL['A'],w=60,h=46);s.text(974,y+28,'PATT 2017, '+pos[i],12.5,'t')
    s.wire([(310,484),(370,484),(370,871),(440,871)],'eth',label='EtherCon 10 m',lpos=(370,700))
    s.text(420,842,'',10,'m')
    s.text(1196,872,'Driver hängen oben neben ihrer PATT, feste IP wie gezeichnet.',12.5,'m')
    s.text(1196,912,'Brücken: 1 zu 2 Cat5 3 m, 2 zu 3 Cat5 5 m, 3 zu 4 Cat5 3 m',12.5,'m')
    s.text(1196,892,'Am Driver: DMX Input Ethernet, Ethernet mode Artnet',12.5,'m')
    # Hinweise
    yN=s.notes(30,730,300,'HINWEISE',[
     'Alle Leitungen von der Bar laufen über das hintere rechte Bein (bei den Kühlschränken) nach oben und dann in der Traverse weiter.',
     'XLR IN an beiden PowerBoxen frei lassen. Liegt dort DMX an, schaltet die Box Art-Net ab.',
     'Zählung der Universen am ersten Gerät prüfen (ab 0 oder ab 1). Umstellen auf der Seite Lampentest.',
     'Reihenfolge in den DMX-Ketten wie gezeichnet. Die Startadresse steht an jeder Lampe.',
     'Am Boden von der Bar zum Bein alle Leitungen abkleben.',
     'Tetris hat eigenes Licht und hängt nicht am Showcontrol.'])
    yL=max(1108,yN+16);s.h=yL+24
    s.legend(yL,[('eth','Netzwerk (Art-Net)',3),('dmx','DMX 5-pol',3),('kombi','Kombikabel Strom und DMX',3),('hyb','Hybridkabel DMX und TRUE1',3),('patt','PATT-Kabel 4-pol XLR',3),('usb','USB',3)])
    return s.out()

def video():
    s=Svg(1600,1000,'SIGNALLAUFPLAN VIDEO',SUB1,SUB2,'spVideo')
    s.zone(30,104,640,446,'REGIE AN DER BAR')
    s.box(60,140,250,70,'Stream Deck+',['Stimmungen, Drehregler'])
    s.box(60,280,250,150,'Show-Rechner',['Showcontrol im Browser Edge','Laptop-Display: Dashboard','Fenster quer: Screen 98 Zoll','Fenster hoch: Screen 55 Zoll','Start mit start.bat'],accent='#801624')
    s.box(410,300,230,110,'Bildausgänge',['1: HDMI-Buchse am Rechner','2: Adapter USB-C auf HDMI','Dock 40A9 hat kein HDMI'])
    s.wire([(185,210),(185,280)],'usb',label='USB',lpos=(185,245))
    s.wire([(310,355),(410,355)],'usb',arrow=False)
    # Displays
    def disp(x,y,w,h,port,title,subs,iw,ih):
        s.box(x,y,w,h,'',[])
        cx=x+90;cy=y+h/2
        s.raw(f'<rect x="{cx-iw/2}" y="{cy-ih/2}" width="{iw}" height="{ih}" rx="3" fill="#801624" stroke="var(--sp-fg)" stroke-width="2"/>')
        s.text(cx,cy+5,port,12,'t',anchor='middle',w=800)
        s.raw(f'<text x="{cx}" y="{cy+5}" font-size="12" font-weight="800" text-anchor="middle" fill="#fff">{port}</text>')
        s.text(x+190,y+34,title,16,'t',w=800)
        for i,t in enumerate(subs): s.text(x+190,y+56+i*18,t,12.5,'m')
    disp(1040,120,530,180,'QUER','Display 98 Zoll, quer',['iiyama LH9875UHS, 3840 x 2160','abgehängt an der hinteren Traverse','Windows-Anzeige: Querformat','Content 1920 x 1080, wird hochgezogen'],140,80)
    disp(1040,350,530,200,'HOCH','Display 55 Zoll, hochkant',['Samsung QM55C','am vorderen linken Bein','Windows-Anzeige: Hochformat','Content 1080 x 1920, synchron zum 98er'],80,140)
    s.wire([(640,330),(840,330),(840,210),(1040,210)],'hdmi',width=3.5,label='HDMI Glasfaser 20 m',lpos=(940,210),sub='Weg rund 11,5 m')
    s.wire([(640,380),(840,380),(840,450),(1040,450)],'hdmi',width=3.5,label='HDMI Glasfaser 20 m',lpos=(940,450),sub='Weg rund 17 m')
    s.text(648,323,'Ausgang 1',10.5,'m',w=700);s.text(648,398,'Ausgang 2',10.5,'m',w=700)
    # Reserve
    s.zone(30,596,740,216,'RESERVE')
    s.box(60,630,250,84,'Mediaplayer Molitor MP01',['Full HD, spielt vom USB-Stick','nicht synchron zum Licht'],dashed=True)
    s.box(480,630,260,84,'Ein Display im Notbetrieb',['98 Zoll oder 55 Zoll','falls der Show-Rechner ausfällt'],dashed=True)
    s.wire([(310,672),(480,672)],'hdmi',label='HDMI 2 m',lpos=(395,672))
    s.text(60,750,'Kabelreserve: 2 x HDMI Glasfaser 10 m, 2 x HDMI 5 m, 3 x HDMI 2 m, 1 x HDMI 1 m',12.5,'m')
    s.text(60,772,'Zweiter Adapter USB-C auf HDMI als Ersatz',12.5,'m')
    # Tetris
    s.zone(830,596,740,216,'TETRIS, EIGENSTÄNDIG')
    s.box(860,630,250,64,'Tetris-Rechner',['ThinkBook, eigener Content'])
    s.box(860,728,250,60,'StreamDeck Studio',['32 Tasten'])
    s.box(1290,630,250,84,'Display 55 Zoll, hochkant',['Samsung QM55C','auf Displaystativ neben dem Stand'])
    s.wire([(1110,662),(1290,662)],'hdmi',label='HDMI 5 m',lpos=(1200,662))
    s.wire([(985,728),(985,694)],'usb',label='USB',lpos=(985,711))
    yN=s.notes(30,860,1540,'HINWEISE',[
     'Beide HDMI-Kabel laufen über das hintere rechte Bein (bei den Kühlschränken) nach oben und dann in der Traverse zu den Displays.',
     'Am Boden von der Bar zum Bein abkleben. Glasfaser nicht knicken und nicht betreten.',
     'Glasfaserkabel haben eine Richtung. Der Stecker mit „Source“ gehört an den Rechner, der mit „Display“ an den Screen.',
     'Den 55er in den Windows-Anzeigeeinstellungen auf Hochformat drehen, Skalierung beider Displays auf 100 %.',
     'Beide Screens und das Licht laufen auf derselben Show-Uhr im Rechner. Ein Sync-Kabel gibt es nicht.',
     'start.bat legt Dashboard und beide Screen-Fenster auf die Displays. Passt die Zuordnung nicht: Positionen in start.json.',
     'Das Kabel zum 55er ist mit rund 17 m von 20 m knapp. Nicht in Schlaufen legen.'],cols=2)
    yL=yN+18;s.h=yL+26
    s.legend(yL,[('hdmi','HDMI',3.5),('usb','USB und USB-C',3)])
    return s.out()


def ton():
    s=Svg(1600,1000,'SIGNALLAUFPLAN TON',SUB1,SUB2,'spTon')
    s.zone(30,104,570,690,'IN DER BAR')
    s.box(60,138,250,84,'Zuspieler',['Show-Rechner oder Handy','Videos im Showcontrol sind ohne Ton'])
    s.box(60,276,250,76,'DI-Box Palmer PLI 04',['2 Kanäle, für Laptop und Handy'])
    s.box(60,410,250,124,'Pult Allen & Heath CQ18T',['Musik auf Mono stellen','Limiter auf die Summe','Ausgang Main L und R'],accent='#801624')
    s.box(60,596,250,160,'Amp Dynacord LX 2200',['2 x 1.100 W an 4 Ohm','Regler zurücknehmen'],accent=COL['lsa'])
    s.text(302,650,'Kanal A',11,'t',anchor='end',w=800);s.text(302,722,'Kanal B',11,'t',anchor='end',w=800)
    s.wire([(185,222),(185,276)],'usb',label='USB-C auf Klinke 3,5 mm',lpos=(185,249))
    s.wire([(185,352),(185,410)],'nf',label='2 x XLR 1,5 m',lpos=(185,381))
    s.wire([(185,534),(185,596)],'nf',label='2 x XLR 3 m',lpos=(185,565))
    s.box(370,430,200,84,'Mikrofon Shure SM 58',['mit Schalter','für Durchsagen'])
    s.wire([(370,472),(310,472)],'nf');s.text(340,462,'XLR',10.5,'m',anchor='middle',w=700);s.text(340,494,'5 m',10.5,'m',anchor='middle',w=700)
    s.box(370,560,200,84,'iPad (Fernbedienung)',['steuert das Pult','über das Remote-Set'],dashed=True)
    # Lautsprecher
    s.zone(660,104,910,300,'AN DER TRAVERSE, über das hintere rechte Bein')
    def spk(x,y,n,pos):
        s.box(x,y,270,76,'',[]);s.raw(f'<rect class="chip" x="{x+12}" y="{y+14}" width="56" height="48" rx="6" stroke="#ffe14d"/>');s.text(x+40,y+44,n,15,'t',anchor='middle',w=800)
        s.text(x+82,y+32,'Seeburg TS Nano',14,'t',w=700);s.text(x+82,y+52,pos,12.5,'m')
    spk(850,150,'S4','hinten, Mitte rechts');spk(1270,150,'S2','hinten links')
    spk(850,290,'S3','vorn, Mitte');spk(1270,290,'S1','vorn links')
    s.wire([(310,646),(630,646),(630,188),(850,188)],'lsa',width=4,label='NL2 10 m',lpos=(742,188))
    s.wire([(1120,188),(1270,188)],'lsa',width=4,label='NL2 5 m',lpos=(1195,188))
    s.wire([(310,718),(645,718),(645,328),(850,328)],'lsb',width=4,label='NL2 15 m',lpos=(750,328))
    s.wire([(1120,328),(1270,328)],'lsb',width=4,label='NL2 5 m',lpos=(1195,328))
    s.text(850,252,'Kanal A: hinteres Paar, durchgeschleift, 2 x 16 Ohm ergibt 8 Ohm',12.5,'m')
    s.text(850,392,'Kanal B: vorderes Paar, durchgeschleift, 2 x 16 Ohm ergibt 8 Ohm',12.5,'m') if False else s.text(850,384,'Kanal B: vorderes Paar, durchgeschleift, 8 Ohm',12.5,'m')
    # Draufsicht
    s.zone(660,440,910,354,'DRAUFSICHT, vorn ist unten')
    sc=96;ox=1115;oy=612
    def P(x,z): return (ox+x*sc,oy+z*sc)
    x0,y0=P(-3.935,-1.435);x1,y1=P(3.935,1.435)
    s.raw(f'<rect x="{x0}" y="{y0}" width="{x1-x0}" height="{y1-y0}" fill="none" stroke="var(--sp-mut)" stroke-width="2"/>')
    s.raw(f'<line x1="{x0}" y1="{y0}" x2="{x1}" y2="{y0}" stroke="var(--sp-fg)" stroke-width="5"/><line x1="{x1}" y1="{y0}" x2="{x1}" y2="{y1}" stroke="var(--sp-fg)" stroke-width="5"/>')
    s.text((x0+x1)/2,y0-10,'Molton hinten und rechts',11.5,'m',anchor='middle')
    s.text((x0+x1)/2,y1+22,'Gang und Publikum',11.5,'m',anchor='middle')
    bx,by=P(1.25,-0.45);bx2,by2=P(3.2,1.3)
    s.raw(f'<rect class="dev" x="{bx}" y="{by}" width="{bx2-bx}" height="{by2-by}" rx="6"/>');s.text((bx+bx2)/2,(by+by2)/2+24,'Bar',12.5,'m',anchor='middle',w=700)
    ax,ay=P(2.15,0.12);s.raw(f'<rect x="{ax-22}" y="{ay-13}" width="44" height="26" rx="4" fill="#801624"/>');s.raw(f'<text x="{ax}" y="{ay+4.5}" font-size="11.5" font-weight="800" text-anchor="middle" fill="#fff">Amp</text>')
    lx,ly=P(3.79,-1.29);s.raw(f'<rect x="{lx-9}" y="{ly-9}" width="18" height="18" fill="var(--sp-fg)"/>');s.text(lx-16,ly+30,'Bein',11.5,'t',anchor='end',w=700)
    def pts(*a): return [P(x,z) for x,z in a]
    s.wire(pts((2.15,0.02),(2.15,-0.75),(3.74,-0.75),(3.74,-1.29),(0.6,-1.29)),'lsa',width=4,arrow=False)
    s.wire(pts((0.6,-1.25),(-3.55,-1.25)),'lsa',width=4,arrow=False)
    s.wire(pts((2.27,0.02),(2.27,-0.63),(3.84,-0.63),(3.84,1.3),(0,1.3)),'lsb',width=4,arrow=False)
    s.wire(pts((0,1.26),(-3.0,1.26)),'lsb',width=4,arrow=False)
    for n,x,z in (('S1',-3.0,1.28),('S2',-3.55,-1.27),('S3',0,1.28),('S4',0.6,-1.27)):
        cx,cy=P(x,z);s.raw(f'<circle cx="{cx}" cy="{cy}" r="15" fill="var(--sp-panel)" stroke="#ffe14d" stroke-width="2.5"/>');s.text(cx,cy+4.5,n,11.5,'t',anchor='middle',w=800,top=True)
    yN=s.notes(30,840,1540,'HINWEISE',[
     'Die Lautsprecherleitungen laufen von der Bar über das hintere rechte Bein (bei den Kühlschränken) nach oben und dann in der Traverse.',
     'Der Amp kann weit mehr, als die Lautsprecher vertragen (120 W je Box). Regler am Amp nur so weit auf wie nötig, am Pult einen Limiter auf die Summe setzen.',
     'Musik am Pult auf Mono stellen, damit vorn und hinten dasselbe läuft.',
     'Lautstärke an der Standgrenze höchstens 70 dB. Musik ist GEMA-pflichtig.',
     'Am Boden von der Bar zum Bein alle Leitungen abkleben.'],cols=2)
    yL=yN+18;s.h=yL+26
    s.legend(yL,[('lsa','Lautsprecher Kanal A (NL2)',4),('lsb','Lautsprecher Kanal B (NL2)',4),('nf','Tonleitung XLR',3),('usb','Klinke',3)])
    return s.out()

CIRC=[('A1','L1','Cluster C1 bis C4','TRUE1 3 m zu C1, dann von Cluster zu Cluster TRUE1 1,5 m, je 620 W max.',2480),
('A2','L2','Cluster C5 bis C8','TRUE1 5 m + 3 m zu C5, dann von Cluster zu Cluster TRUE1 1,5 m',2480),
('A3','L3','PowerBox 1 und 2, Switch B','TRUE1 1,5 m zu PowerBox 1, weiter zu PowerBox 2, Switch B über Adapter TRUE1 auf Schuko',700),
('A4','L1','Display 55 Zoll am Bein','Adapter TRUE1 auf Schuko, Schuko 3 m',150),
('A5','L2','QuikSpots Q1 bis Q8 (Rohr P1 bis P3)','TRUE1 3 m zum ersten Spot Q3 (P1 vorn), weiter per Hybridkabel, Rohrwechsel TRUE1 3 m',320),
('A6','L3','QuikSpots Q9 bis Q13 (Rohr P4, P5), Pixel Lines PL1 bis PL4','TRUE1 5 m + 3 m zu Q9 (P4 hinten), ab Q11 weiter zu den Pixel Lines: TRUE1 5 m, 3 m, 5 m, 3 m',440),
('B1','L1','4 PATT Driver an der Traverse','Schuko 10 m über das hintere rechte Bein, Netzkabel Schuko auf TRUE1, dann durchgeschleift',960),
('B2','L2','Display 98 Zoll','Schuko 10 m + 5 m über das hintere rechte Bein und die hintere Traverse',350),
('B3','L3','Siebträgermaschine, Kaffeemühle','nichts dazustecken',1550),
('B4','L1','2 Kühlschränke','bleibt über Nacht an',300),
('B5','L2','Amp Dynacord LX 2200, Pult CQ18T','Ton',460),
('B6','L3','Show-Rechner mit Dock, Switch A, Jägermeister-Maschine','Tischsteckdose an der Bar',300),
('S1','L3','Tetris: Display 55 Zoll, Rechner, Röhren, QuikSpots','Phase am Verteiler prüfen',610)]
def de(n): return f'{n:,}'.replace(',','.')
def strom():
    s=Svg(1600,1244,'STROMLAUFPLAN',SUB1,SUB2,'spStrom')
    s.box(30,108,230,104,'Hallenanschluss',['CEE 32 A, 400 V, 3 Phasen','bis 7,3 kW je Phase','kommt hinten rechts an'],accent=COL['cee'])
    s.wire([(145,212),(145,292)],'cee',width=6,label='CEE 32 A, 10 m',lpos=(145,252))
    s.box(30,292,230,330,'Stromverteiler 32 A',['LED-Video-Stromverteiler','hinten rechts, zwischen','Kühlschränken und Molton','','2 x HAN16:','je 6 Kreise mit 16 A,','RCBO 30 mA je Kreis','','2 x Schuko'],accent=COL['cee'])
    for y,t in [(350,'HAN A'),(480,'HAN B'),(585,'Schuko')]: s.text(250,y+4,t,11,'t',anchor='end',w=800)
    s.box(30,672,230,92,'Potentialausgleich',['Traverse an die PE-Schraube','Erdungskabel 10 m'],accent=COL['pe'])
    s.wire([(145,672),(145,622)],'pe',width=3.5)
    def rows(y0,items,zone_label,zh):
        s.zone(440,y0-58,1130,zh,zone_label)
        s.raw(f'<rect x="452" y="{y0-24}" width="7" height="{(len(items)-1)*60+48}" rx="3" fill="var(--sp-fg)"/>') if len(items)>1 else None
        for i,(k,ph,t,d,w) in enumerate(items):
            y=y0+i*60;c=COL[ph];a=w/230
            s.raw(f'<rect class="chip" x="470" y="{y-22}" width="74" height="44" rx="6" stroke="{c}"/>')
            s.text(488,y+5,k,15,'t',w=800);s.raw(f'<text x="536" y="{y+5}" font-size="12" font-weight="800" text-anchor="end" fill="{c}">{ph}</text>')
            s.wire([(544,y),(596,y)],ph,width=3.5)
            s.box(596,y-23,640,46,'',[])
            s.text(610,y-3,t,14,'t',w=700);s.text(610,y+15,d,11.5,'m')
            s.text(1310,y+5,de(w)+' W',13.5,'t',anchor='end',w=700)
            s.text(1384,y+5,f'{a:.1f}'.replace('.',',')+' A',13.5,'t',anchor='end',w=700)
            s.raw(f'<rect class="barbg" x="1400" y="{y-6}" width="150" height="12" rx="3"/><rect x="1400" y="{y-6}" width="{150*a/16:.1f}" height="12" rx="3" fill="{c}"/>')
    s.text(1310,96,'Leistung',11,'m',anchor='end',w=700);s.text(1384,96,'Strom',11,'m',anchor='end',w=700);s.text(1400,96,'Anteil an 16 A',11,'m',w=700)
    rows(170,CIRC[0:6],'ABGANG A: PLUGBOX 6 x TRUE1 AM TECHNIKPUNKT, LINKE TRAVERSE OBEN',404)
    rows(604,CIRC[6:12],'ABGANG B: PLUGBOX 6 x SCHUKO AM BODEN HINTER DER BAR',404)
    rows(1038,CIRC[12:13],'SCHUKO-ABGANG AM VERTEILER',100)
    s.wire([(260,350),(300,350),(300,320),(452,320)],'han',width=6,arrow=False,label='Multicore 10 m + 5 m',lpos=(372,320))
    s.text(372,276,'über das hintere rechte',11.5,'m',anchor='middle');s.text(372,291,'Bein in die Traverse',11.5,'m',anchor='middle')
    s.wire([(260,480),(320,480),(320,754),(452,754)],'han',width=6,arrow=False,label='Multicore 5 m',lpos=(386,754))
    s.wire([(260,585),(290,585),(290,1038),(470,1038)],'sch',width=3.5,label='Schuko 20 m',lpos=(380,1038))
    s.text(380,1016,'hinter dem Molton',11.5,'m',anchor='middle')
    # Phasen
    ph={'L1':0,'L2':0,'L3':0}
    for k,p,t,d,w in CIRC: ph[p]+=w
    tot=sum(ph.values())
    s.text(30,812,'PHASEN IM WORST CASE',11.5,'m',w=800,ls='0.08em')
    for i,p in enumerate(['L1','L2','L3']):
        y=842+i*52;a=ph[p]/230
        s.raw(f'<text x="30" y="{y}" font-size="15" font-weight="800" fill="{COL[p]}">{p}</text>')
        s.text(66,y,de(ph[p])+' W',13.5,'t',w=700);s.text(260,y,f'{a:.1f}'.replace('.',',')+' A, '+str(round(a/32*100))+' %',13.5,'t',anchor='end',w=700)
        s.raw(f'<rect class="barbg" x="30" y="{y+9}" width="230" height="10" rx="3"/><rect x="30" y="{y+9}" width="{230*a/32:.1f}" height="10" rx="3" fill="{COL[p]}"/>')
    s.text(30,1004,'Gesamt '+de(tot)+' W',14,'t',w=800);s.text(30,1024,'rund 50 % von 22 kW',12.5,'m')
    yN=s.notes(440,1112,1130,'HINWEISE',[
     'Nach oben geht alles über das hintere rechte Bein (bei den Kühlschränken). Nichts hinter dem Molton hochführen.',
     'Worst Case: alle Geräte an, Cluster mit voller Leistung. Belegt sind Cluster (620 W), Display 98 Zoll und PATT Driver (240 W), der Rest ist geschätzt.',
     'Die Phasen der HAN-Kreise (1 bis 6 gleich L1, L2, L3, L1, L2, L3) sind angenommen. Am Verteiler prüfen.',
     'Vor dem Einschalten: Traverse erden, Anlage mit dem Prüfgerät messen.',
     'Jeden Abend nach Messeschluss alle Kreise aus. Nur B4 (Kühlschränke) bleibt an.'],cols=2,size=12,lh=16)
    yL=yN+18;s.h=yL+26
    s.legend(yL,[('cee','CEE 32 A',6),('han','Multicore HAN16',6),('L1','Kreis auf L1',3.5),('L2','Kreis auf L2',3.5),('L3','Kreis auf L3',3.5),('sch','Schuko',3.5),('pe','Potentialausgleich',3.5)])
    return s.out(),ph,tot
if __name__=='__main__':
    L=licht();V=video();S,ph,tot=strom();T=ton();print(ph,tot)
    open('/tmp/plan/licht.svg','w').write(L);open('/tmp/plan/video.svg','w').write(V);open('/tmp/plan/strom.svg','w').write(S);open('/tmp/plan/ton.svg','w').write(T)
    for mode,css in (('light',LIGHT),('dark',DARK)):
        h='<!DOCTYPE html><html lang="de"><head><meta charset="utf-8"><title>FoF 26: Signal- und Stromlaufpläne</title><style>'+css+CSS+'@page{size:A3 landscape;margin:8mm}html,body{margin:0;background:var(--sp-bg)}.pg{page-break-after:always;height:281mm;display:flex;align-items:center;justify-content:center}.pg:last-child{page-break-after:auto}.pg svg{max-width:100%;max-height:281mm;width:auto;height:281mm}</style></head><body>'+''.join('<div class="pg">'+x+'</div>' for x in (L,V,T,S))+'</body></html>'
        open('/tmp/plan/plan_%s.html'%mode,'w').write(h)
