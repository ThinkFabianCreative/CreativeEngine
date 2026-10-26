// Client-side story discovery only. External donation and story destinations are unchanged.
const cards = [...document.querySelectorAll('.mosaic > a.tile')];
for (const card of cards) {
  card.dataset.storyFormat = card.href.includes('youtube.com') ? 'video' : 'read';
  card.dataset.storyUpdate = String(card.textContent.includes('Where Are They Now?'));
}
document.querySelector('.filters')?.addEventListener('click', event => {
  const button = event.target.closest('button');
  if (!button) return;
  const filter = button.textContent.trim();
  for (const card of cards) card.hidden = !(filter === 'All' || card.dataset.storyFormat === filter.toLowerCase() || (filter === 'Where Are They Now?' && card.dataset.storyUpdate === 'true'));
  document.querySelectorAll('.mosaic > .drawing').forEach(card => { card.hidden = filter !== 'All'; });
});
