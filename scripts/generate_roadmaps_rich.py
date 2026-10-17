from pathlib import Path
import runpy
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import mm
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak, KeepTogether

DATA=runpy.run_path(str(Path(__file__).with_name('generate_roadmaps.py')))
routes, uc_rows = DATA['routes'], DATA['uc_rows']
OUT=Path(__file__).resolve().parents[1]/'assets'/'docs'/'roadmaps'; OUT.mkdir(parents=True,exist_ok=True)
BLUE=colors.HexColor('#003b68'); BLUE2=colors.HexColor('#005594'); ORANGE=colors.HexColor('#f58220'); PALE=colors.HexColor('#f4f7fa'); PALE2=colors.HexColor('#eef5f9'); INK=colors.HexColor('#13283b'); MUTED=colors.HexColor('#64748b'); LINE=colors.HexColor('#dce6ef')
styles=getSampleStyleSheet()
styles.add(ParagraphStyle(name='CoverTitle',parent=styles['Title'],fontName='Helvetica-Bold',fontSize=28,leading=31,textColor=BLUE,spaceAfter=10))
styles.add(ParagraphStyle(name='CoverSub',parent=styles['Normal'],fontSize=11,leading=16,textColor=MUTED,spaceAfter=8))
styles.add(ParagraphStyle(name='H2R',parent=styles['Heading2'],fontName='Helvetica-Bold',fontSize=17,leading=21,textColor=BLUE,spaceBefore=12,spaceAfter=7))
styles.add(ParagraphStyle(name='H3R',parent=styles['Heading3'],fontName='Helvetica-Bold',fontSize=11.5,leading=14,textColor=INK,spaceBefore=6,spaceAfter=4))
styles.add(ParagraphStyle(name='BodyR',parent=styles['BodyText'],fontSize=9.2,leading=13.5,textColor=INK,spaceAfter=5))
styles.add(ParagraphStyle(name='SmallR',parent=styles['BodyText'],fontSize=7.7,leading=10.5,textColor=MUTED,spaceAfter=3))
styles.add(ParagraphStyle(name='CellR',parent=styles['BodyText'],fontSize=7.2,leading=9.4,textColor=INK))
styles.add(ParagraphStyle(name='HeaderCellR',parent=styles['BodyText'],fontName='Helvetica-Bold',fontSize=7.2,leading=9.4,textColor=colors.white))
styles.add(ParagraphStyle(name='WhiteR',parent=styles['BodyText'],fontSize=9,leading=13,textColor=colors.white))
def P(t,s='BodyR'): return Paragraph(t,styles[s])
def table(rows,widths,header=True):
    data=[]
    for row_index,r in enumerate(rows):
        style='HeaderCellR' if header and row_index==0 else 'CellR'
        data.append([P(str(c),style) for c in r])
    t=Table(data,colWidths=widths,repeatRows=1 if header else 0,hAlign='LEFT')
    ts=[('GRID',(0,0),(-1,-1),.35,LINE),('VALIGN',(0,0),(-1,-1),'TOP'),('LEFTPADDING',(0,0),(-1,-1),6),('RIGHTPADDING',(0,0),(-1,-1),6),('TOPPADDING',(0,0),(-1,-1),6),('BOTTOMPADDING',(0,0),(-1,-1),6),('ROWBACKGROUNDS',(0,1 if header else 0),(-1,-1),[colors.white,PALE])]
    if header: ts += [('BACKGROUND',(0,0),(-1,0),BLUE),('TEXTCOLOR',(0,0),(-1,0),colors.white)]
    t.setStyle(TableStyle(ts)); return t
def card(title,body,accent=ORANGE):
    t=Table([[P(title,'H3R')],[P(body)]],colWidths=[174*mm]); t.setStyle(TableStyle([('BACKGROUND',(0,0),(-1,-1),colors.white),('BOX',(0,0),(-1,-1),.6,LINE),('LINEBEFORE',(0,0),(0,-1),4,accent),('LEFTPADDING',(0,0),(-1,-1),12),('RIGHTPADDING',(0,0),(-1,-1),12),('TOPPADDING',(0,0),(-1,-1),8),('BOTTOMPADDING',(0,0),(-1,-1),8)])); return t
def header_footer(canvas,doc):
    canvas.saveState(); canvas.setFillColor(BLUE); canvas.rect(0,A4[1]-8*mm,A4[0],8*mm,fill=1,stroke=0); canvas.setFillColor(ORANGE); canvas.rect(18*mm,A4[1]-6.2*mm,18*mm,3.6*mm,fill=1,stroke=0); canvas.setFillColor(colors.white); canvas.setFont('Helvetica-Bold',7); canvas.drawString(40*mm,A4[1]-5.2*mm,'MKT-N1  /  ROTEIRO CURRICULAR'); canvas.setStrokeColor(LINE); canvas.line(18*mm,14*mm,192*mm,14*mm); canvas.setFillColor(MUTED); canvas.setFont('Helvetica',7); canvas.drawString(18*mm,9*mm,'Plano de Curso 339 · proposta pedagógica de implementação'); canvas.drawRightString(192*mm,9*mm,f'{doc.page}'); canvas.restoreState()
def cover(title,intro,why):
    banner=Table([[P('MKT-N1','WhiteR'),P('PLANO DE IMPLEMENTAÇÃO','WhiteR')]],colWidths=[34*mm,140*mm]); banner.setStyle(TableStyle([('BACKGROUND',(0,0),(-1,-1),BLUE),('BACKGROUND',(0,0),(0,0),ORANGE),('VALIGN',(0,0),(-1,-1),'MIDDLE'),('LEFTPADDING',(0,0),(-1,-1),10),('RIGHTPADDING',(0,0),(-1,-1),10),('TOPPADDING',(0,0),(-1,-1),9),('BOTTOMPADDING',(0,0),(-1,-1),9)]))
    return [banner,Spacer(1,12*mm),P('ROTEIRO CURRICULAR','SmallR'),P(title,'CoverTitle'),P(intro,'CoverSub'),Spacer(1,7*mm),card('Por que esta possibilidade?',why,ORANGE),Spacer(1,7*mm),P('Como usar este PDF','H2R'),table([['Passo','Ação docente','Resultado esperado'],['01','Escolha o negócio, desafio ou cliente que dará contexto à turma.','Um problema concreto e um briefing inicial.'],['02','Defina quais evidências serão produzidas em cada etapa.','Critérios visíveis para acompanhamento e feedback.'],['03','Introduza a tecnologia somente quando ela apoiar a competência.','Menos foco em ferramenta; mais foco em decisão e processo.'],['04','Feche cada etapa com teste, reflexão e correção de rota.','Aprendizagem documentada e melhoria contínua.']],[15*mm,86*mm,73*mm]),Spacer(1,6*mm),P('<b>Importante:</b> este documento é uma proposta derivada do Plano de Curso 339. Não substitui o plano oficial nem altera cargas horárias, correquisitos ou critérios de avaliação.','SmallR'),PageBreak()]
def rich_step(title,ucs,desc,index):
    activities=['Ler o briefing e delimitar o problema','Pesquisar público, referências e restrições','Escolher a ferramenta adequada e registrar a justificativa','Produzir uma primeira versão ou protótipo','Testar com colegas, dados ou cenário simulado','Apresentar evidências, receber feedback e corrigir a rota']
    deliver=['Briefing e hipótese de trabalho','Mapa de público e referências','Decisão tecnológica registrada','Versão inicial do artefato','Registro de teste e feedback','Versão final + reflexão individual'][index%6]
    step=Table([[P(f'{index+1:02d}','WhiteR'),P(title,'WhiteR')],[P('<b>UCs relacionadas:</b> '+ucs,'SmallR'),P(desc,'BodyR')],[P('<b>Passo a passo didático</b>','H3R'),P('<br/>'.join(f'{i+1}. {a}' for i,a in enumerate(activities)),'BodyR')],[P('<b>Entregável principal</b>','SmallR'),P(deliver,'BodyR')]],colWidths=[22*mm,152*mm])
    step.setStyle(TableStyle([('BACKGROUND',(0,0),(-1,0),BLUE2),('BACKGROUND',(0,1),(0,-1),PALE2),('BOX',(0,0),(-1,-1),.6,LINE),('INNERGRID',(0,0),(-1,-1),.3,LINE),('VALIGN',(0,0),(-1,-1),'TOP'),('LEFTPADDING',(0,0),(-1,-1),9),('RIGHTPADDING',(0,0),(-1,-1),9),('TOPPADDING',(0,0),(-1,-1),7),('BOTTOMPADDING',(0,0),(-1,-1),7)])); return step
def build(slug,title,intro,why,steps):
    doc=SimpleDocTemplate(str(OUT/f'{slug}.pdf'),pagesize=A4,rightMargin=18*mm,leftMargin=18*mm,topMargin=15*mm,bottomMargin=20*mm,title=title,author='MKT-N1')
    story=cover(title,intro,why)+[P('Roteiro detalhado de implementação','H2R'),P('A sequência abaixo organiza a proposta em etapas de ação-reflexão-ação. O docente pode ajustar a duração interna de cada atividade às horas presenciais e a distância previstas no plano oficial.','BodyR')]
    for i,(name,ucs,desc) in enumerate(steps): story += [rich_step(name,ucs,desc,i),Spacer(1,5*mm)]
    story += [PageBreak(),P('Tecnologias no momento certo','H2R'),P('A lógica é introduzir fundamentos antes de exigir produção complexa, e conectar cada ferramenta a uma decisão de marketing. O estudante deve saber explicar por que usou determinado recurso, qual problema resolveu e como verificou o resultado.','BodyR'),table([['Momento','Fundamentos e tecnologias','Evidência'],['Fundamentos','Arquivos, formatos, pesquisa, planilhas, segurança e IA com verificação.','Repositório organizado, pesquisa e decisão justificada.'],['Produção','Adobe/Canva, GIMP, Kdenlive, fotografia, vídeo e assets para canais.','Peças exportadas corretamente e processo registrado.'],['Digital','HTML/CSS/Bootstrap introdutórios, CMS, analytics, UTMs e acessibilidade.','Página/protótipo navegável e campanha rastreável.'],['Operação','CRM, ERP conceitual, catálogo, estoque, pedidos, atendimento e indicadores.','Fluxo operacional, base simulada e painel.']],[31*mm,86*mm,63*mm]),Spacer(1,6*mm),P('Roteiro de feedback e avaliação','H2R'),table([['Momento de feedback','Perguntas orientadoras','Evidência'],['Diagnóstico','Qual problema está sendo resolvido? Para quem?','Briefing e hipótese.'],['Primeira versão','A solução atende ao objetivo ou apenas ficou visualmente pronta?','Protótipo/rascunho comentado.'],['Teste','O que o usuário, dado ou colega revelou?','Registro de teste.'],['Refinamento','O que mudou e por quê?','Versão final comparada.'],['Fechamento','O que seria feito em uma situação real?','Apresentação e reflexão.']],[35*mm,90*mm,55*mm]),Spacer(1,6*mm),P('Conexão com o mercado contemporâneo','H2R'),P('O roteiro combina estratégia, criatividade, tecnologia, dados, relacionamento e operação. Isso acompanha a realidade de equipes de marketing integradas e enxutas, nas quais profissionais precisam interpretar dados, produzir conteúdos, colaborar com tecnologia, usar IA com responsabilidade e explicar decisões. O foco é formar autonomia para escolher e combinar ferramentas, não apenas operar um software específico.','BodyR'),PageBreak(),P('Matriz UC por UC','H2R'),P('A matriz abaixo sintetiza a análise do Plano de Curso 339 e indica o momento recomendado para os fundamentos tecnológicos.','BodyR'),table([['UC','Competência do plano','Conhecimentos e competência','Fundamento/tecnologia no momento certo'],*uc_rows],[13*mm,45*mm,53*mm,61*mm]),Spacer(1,6*mm),P('Referências e limites','H2R'),P('Base curricular: Plano de Curso 339 — Habilitação Profissional Técnica em Marketing, Senac São Paulo, vigente a partir de 01/02/2026. As associações tecnológicas e o passo a passo são recomendações de implementação; a organização oficial do curso permanece a referência para planejamento e avaliação.','SmallR'),P('Conexão de mercado: Future of Jobs Report 2025, World Economic Forum. O relatório destaca a crescente importância de IA, dados, pensamento criativo, análise, colaboração, flexibilidade e aprendizagem contínua.','SmallR')]
    doc.build(story,onFirstPage=header_footer,onLaterPages=header_footer)
for slug,(title,intro,why,steps) in routes.items(): build(slug,title,intro,why,steps)
