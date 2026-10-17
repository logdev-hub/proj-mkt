from pathlib import Path
from reportlab.lib import colors
from reportlab.lib.enums import TA_LEFT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import mm
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak, KeepTogether

OUT=Path(__file__).resolve().parents[1]/'assets'/'docs'/'roadmaps'
OUT.mkdir(parents=True,exist_ok=True)
blue=colors.HexColor('#003b68'); orange=colors.HexColor('#f58220'); pale=colors.HexColor('#eef5f9'); ink=colors.HexColor('#13283b'); muted=colors.HexColor('#64748b')
styles=getSampleStyleSheet()
styles.add(ParagraphStyle(name='Cover',parent=styles['Title'],fontName='Helvetica-Bold',fontSize=25,leading=29,textColor=blue,spaceAfter=10))
styles.add(ParagraphStyle(name='Sub',parent=styles['Normal'],fontSize=11,leading=16,textColor=muted,spaceAfter=10))
styles.add(ParagraphStyle(name='H2x',parent=styles['Heading2'],fontName='Helvetica-Bold',fontSize=16,leading=20,textColor=blue,spaceBefore=14,spaceAfter=7))
styles.add(ParagraphStyle(name='H3x',parent=styles['Heading3'],fontName='Helvetica-Bold',fontSize=11,leading=14,textColor=ink,spaceBefore=7,spaceAfter=4))
styles.add(ParagraphStyle(name='Bodyx',parent=styles['BodyText'],fontSize=9.5,leading=14,textColor=ink,spaceAfter=6))
styles.add(ParagraphStyle(name='Smallx',parent=styles['BodyText'],fontSize=8,leading=11,textColor=muted,spaceAfter=3))
styles.add(ParagraphStyle(name='Cell',parent=styles['BodyText'],fontSize=7.5,leading=10,textColor=ink))
def P(t,s='Bodyx'): return Paragraph(t,styles[s])
def bullets(items): return [P('• '+x,'Bodyx') for x in items]
def table(rows,widths):
    data=[[P(str(c),'Cell') for c in row] for row in rows]
    t=Table(data,colWidths=widths,repeatRows=1)
    t.setStyle(TableStyle([('BACKGROUND',(0,0),(-1,0),blue),('TEXTCOLOR',(0,0),(-1,0),colors.white),('GRID',(0,0),(-1,-1),.35,colors.HexColor('#cfdde6')),('VALIGN',(0,0),(-1,-1),'TOP'),('LEFTPADDING',(0,0),(-1,-1),6),('RIGHTPADDING',(0,0),(-1,-1),6),('TOPPADDING',(0,0),(-1,-1),6),('BOTTOMPADDING',(0,0),(-1,-1),6),('ROWBACKGROUNDS',(0,1),(-1,-1),[colors.white,pale])]))
    return t
def footer(canvas,doc):
    canvas.saveState(); canvas.setStrokeColor(colors.HexColor('#dce6ef')); canvas.line(18*mm,14*mm,192*mm,14*mm); canvas.setFont('Helvetica',7); canvas.setFillColor(muted); canvas.drawString(18*mm,9*mm,'MKT-N1 · Roteiro curricular proposto · Plano de Curso 339'); canvas.drawRightString(192*mm,9*mm,f'{doc.page}'); canvas.restoreState()

uc_rows=[
['UC1','Estratégias de marketing','Pesquisa, plano e indicadores','Fundamentos digitais: arquivos, planilha, pesquisa e IA para ideação; visualização simples de dados.'],
['UC2','Ações comerciais e relacionamento','Cadastro de clientes, vendas e relatórios','Planilhas estruturadas, CRM conceitual, formulários e registro de interações.'],
['UC3','PI Assistente de Marketing e Vendas','Articulação das UCs 1–2','Documentação de projeto, apresentação e evidências; tecnologia como suporte à decisão.'],
['UC4','Identidade da marca','Pesquisa, posicionamento e marca','Adobe para repertório profissional; GIMP para fundamentos de imagem, arquivos e variações.'],
['UC5','Comunicação corporativa','Planos, canais e avaliação','Adobe/Canva/GIMP para peças; organização de assets e formatos por canal.'],
['UC6','Implantar negócio digital','Plano, loja virtual e ações corretivas','HTML/CSS introdutórios, CMS/plataforma, noções de analytics, LGPD e jornada digital.'],
['UC7','Campanhas em mídias sociais','Pesquisa, público, conteúdo e formatos','Adobe Express/Creative Cloud quando disponível; IA para ideação com verificação; calendário editorial.'],
['UC8','Monitorar campanhas','Métricas, coleta e relatórios','Planilhas, dashboards, UTMs, leitura de dados e automações leves.'],
['UC9','PI Assistente de Marketing Digital','Articulação das UCs 6–8','Campanha documentada com criativos, métricas, aprendizados e plano corretivo.'],
['UC10','Estruturar comércio on-line','Modelo, operação, legislação e estratégia','Arquitetura de catálogo, UX, SEO básico, meios de pagamento e políticas.'],
['UC11','Plataformas de negócios digitais','Interface, jornada e atendimento','HTML/CSS/Bootstrap, protótipo navegável, acessibilidade, LGPD e testes com usuários.'],
['UC12','Processos operacionais de e-commerce','Produtos, pedidos, estoque e financeiro','ERP conceitual, planilha de operação, cadastro, fluxo de pedido e logística.'],
['UC13','Monitorar etapas de e-commerce','Indicadores, dados e comportamento','Analytics, funil, conversão, abandono, relatório e plano de otimização.'],
['UC14','PI Assistente de E-commerce','Articulação das UCs 10–13','Protótipo ou loja documentada com catálogo, operação, métricas e experiência.'],
['UC15','Relacionamento com cliente','Segmentação, atendimento e feedback','CRM, automação responsável, base de clientes, consentimento e pós-venda.'],
['UC16','Experiências inovadoras','Campanhas experienciais, conteúdo e influência','IA aplicada com mediação, Adobe/open source, prototipação, testes e métricas de satisfação.'],
['UC17','PI Técnico em Marketing','Integração do perfil profissional','Projeto final com estratégia, dados, conteúdo, tecnologia, operação e apresentação executiva.']]

routes={
'01-trilha-linear-integrada':('Trilha linear integrada','Sequência progressiva para nivelar fundamentos antes de avançar para campanhas, e-commerce, dados e inovação.','Indicada para turmas com níveis digitais muito diferentes; reduz a sobrecarga cognitiva e cria uma base comum.',[
('Etapa 1 · Fundamentos','UC1–UC5','Arquivos, pesquisa, planilhas, imagem, identidade e comunicação. Entregável: kit de marca com pesquisa, mapa de público e peças em formatos diferentes.'),
('Etapa 2 · Digital','UC6–UC9','Negócio digital, campanhas, métricas e PI. Entregável: campanha com landing page, calendário, criativos, UTMs e relatório.'),
('Etapa 3 · E-commerce','UC10–UC14','Modelo, plataforma, operação, estoque, pedidos, métricas e PI. Entregável: protótipo/loja com catálogo e fluxo operacional.'),
('Etapa 4 · Relacionamento e inovação','UC15–UC17','CRM, experiências, IA aplicada e projeto final. Entregável: jornada integrada, automação conceitual e apresentação executiva.')]),
'02-projeto-transversal':('Projeto transversal de um negócio','Um mesmo negócio evolui em todas as UCs; cada docente recebe e devolve artefatos para a etapa seguinte.','É a melhor opção para conectar dados e evitar simulações desconectadas.',[
('Descoberta e marca','UC1–UC5','Pesquisa, posicionamento, identidade, comunicação e base de assets. O negócio nasce com problema, público e proposta de valor.'),
('Presença digital','UC6–UC9','O negócio ganha presença digital, campanha e indicadores. Cada entrega atualiza um dossiê compartilhado.'),
('Operação e experiência','UC10–UC14','Catálogo, plataforma, UX, pedidos, estoque, indicadores e melhorias alimentam o mesmo negócio.'),
('Relacionamento e escala','UC15–UC17','CRM, pós-venda, inovação, IA e projeto integrado fecham o ciclo com dados e decisões.')]),
'03-laboratorio-digital':('Laboratório digital por desafios','Organização em desafios curtos que simulam demandas reais: lançamento, campanha, loja, atendimento, análise e experiência.','Amplia portfólio, permite comparar segmentos e aproxima a escola da dinâmica de agência e cliente.',[
('Desafio 1 · Diagnóstico','UC1–UC4','Pesquisa, dados, público e marca. Ferramentas: planilhas, IA para perguntas e Adobe/GIMP para moodboards.'),
('Desafio 2 · Conteúdo e campanha','UC5–UC9','Comunicação, negócio digital, campanha, métricas e PI. Ferramentas: Adobe, open source, calendário, dashboards e UTMs.'),
('Desafio 3 · Comércio','UC10–UC14','E-commerce completo: modelo, plataforma, cadastro, operação, métricas e PI.'),
('Desafio 4 · Relação e inovação','UC15–UC17','CRM, experiência, influência, automação e projeto final com banca.')]),
'04-agencia-escola':('Agência-escola e portfólio profissional','Equipes assumem papéis de atendimento, estratégia, criação, dados, operação e apresentação.','Desenvolve colaboração, comunicação e autonomia — competências destacadas no plano e exigidas em times enxutos.',[
('Briefing e atendimento','UC1–UC3','Leitura de briefing, escopo, pesquisa, proposta e apresentação de diagnóstico.'),
('Branding e comunicação','UC4–UC5','Sistema visual, peças e plano de comunicação; Adobe como referência profissional e GIMP/Kdenlive como alternativas.'),
('Performance digital','UC6–UC9','Campanha, conteúdo, negócio digital, métricas e relatório para cliente.'),
('E-commerce e CX','UC10–UC16','Loja, operação, dados, CRM, experiência e teste de hipóteses.'),
('Portfólio final','UC17','Case completo com problema, processo, solução, evidências, resultados e reflexão.')])}

def build(path,title,intro,why,steps):
    doc=SimpleDocTemplate(str(path),pagesize=A4,rightMargin=18*mm,leftMargin=18*mm,topMargin=17*mm,bottomMargin=20*mm,title=title,author='MKT-N1')
    story=[P('MKT-N1 · PLANO DE IMPLEMENTAÇÃO','Smallx'),P(title,'Cover'),P(intro,'Sub'),P('<b>Nota de enquadramento:</b> este roteiro é uma proposta pedagógica derivada do Plano de Curso 339. Não substitui o documento oficial nem altera cargas horárias, correquisitos ou critérios de avaliação.','Smallx'),Spacer(1,5*mm),P('Por que esta possibilidade?', 'H2x'),P(why),P('Roteiro de implementação','H2x')]
    for name,ucs,desc in steps:
        story += [P(name,'H3x'),P('<b>UCs relacionadas:</b> '+ucs,'Smallx'),P(desc)]
    story += [P('Tecnologias e fundamentos por momento','H2x'),table([['Momento','Fundamentos e tecnologias','Evidência esperada'],['Início','Organização de arquivos, formatos, pesquisa, planilhas e segurança digital','Repositório organizado, pesquisa documentada e decisão justificada'],['Produção','Adobe/Canva, GIMP, Kdenlive, IA com verificação e produção multimídia','Assets exportados em formatos corretos e processo registrado'],['Digital','HTML/CSS/Bootstrap introdutórios, CMS, analytics, UTMs e acessibilidade','Página/protótipo navegável, campanha rastreável e relatório'],['Operação','CRM, ERP conceitual, catálogo, estoque, pedidos, atendimento e indicadores','Fluxo operacional, base de dados simulada e painel de acompanhamento']],[32*mm,78*mm,62*mm]),P('Evidências e avaliação formativa','H2x'),P('Em cada etapa, registrar briefing, hipótese, versão inicial, testes, feedback, correção de rota e reflexão. A avaliação deve observar não só a peça final, mas a capacidade de pesquisar, justificar escolhas, trabalhar em equipe, usar tecnologia com responsabilidade e conectar ações a objetivos de negócio.'),P('Conexão com o mercado contemporâneo','H2x'),P('A proposta combina domínio técnico, pensamento analítico, criatividade, colaboração e autonomia digital. Esse conjunto responde à realidade de equipes de marketing cada vez mais integradas a dados, tecnologia, conteúdo, atendimento e operações. A tecnologia é usada para ampliar a capacidade humana de decidir e criar, não para substituir a mediação crítica.'),PageBreak(),P('Matriz UC por UC','H2x'),table([['UC','Competência do plano','Fundamento/tecnologia no momento certo'],*uc_rows],[14*mm,54*mm,104*mm]),P('Fontes e limites','H2x'),P('Base curricular: Plano de Curso 339 — Habilitação Profissional Técnica em Marketing, Senac São Paulo, vigente a partir de 01/02/2026. As associações tecnológicas e os roteiros são recomendações de implementação, construídas a partir das competências, conhecimentos, cargas horárias e correquisitos do documento.'),P('Mercado: a proposta considera a combinação de tecnologia, IA, dados, criatividade e competências humanas apontada no Future of Jobs Report 2025 do World Economic Forum. A adoção concreta deve respeitar infraestrutura, licenças, acessibilidade, proteção de dados e o planejamento docente.')]
    doc.build(story,onFirstPage=footer,onLaterPages=footer)

for slug,(title,intro,why,steps) in routes.items(): build(OUT/f'{slug}.pdf',title,intro,why,steps)
