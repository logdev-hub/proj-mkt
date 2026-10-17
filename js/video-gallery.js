document.addEventListener('DOMContentLoaded',()=>{
  const page=new URLSearchParams(location.search).get('pagina');
  if(page!=='galeria') return;
  const old=document.querySelector('.video-card');
  if(!old) return;
  old.outerHTML=`<div class="video-grid mt-5"><article class="video-item"><div class="video-copy"><span class="eyebrow">🎥 REGISTRO EM VÍDEO · 01</span><h2>Atividades e bastidores</h2><p>Momentos de interação, colaboração e construção coletiva durante as atividades.</p><span class="video-tag">Bastidores</span></div><video controls preload="metadata" poster="assets/images/galeria/001.jpeg"><source src="assets/videos/video001.mp4" type="video/mp4"></video></article><article class="video-item"><div class="video-copy"><span class="eyebrow">🎥 REGISTRO EM VÍDEO · 02</span><h2>Apresentações e troca de ideias</h2><p>Registro audiovisual das apresentações e das trocas realizadas pelas equipes.</p><span class="video-tag">Apresentações</span></div><video controls preload="metadata" poster="assets/images/galeria/004.jpeg"><source src="assets/videos/video002.mp4" type="video/mp4"></video></article></div>`;
});
