document.addEventListener('DOMContentLoaded', function() {
  const $ = id => document.getElementById(id);
  if (typeof renderIdeasList === 'function') renderIdeasList();
  const startBtn = $('startBtn');
  const projectName = $('projectName');
  if (startBtn && projectName) {
    startBtn.disabled = !projectName.value.trim();
    projectName.addEventListener('input', (e) => { startBtn.disabled = !e.target.value.trim(); });
    projectName.addEventListener('keypress', (e) => { if (e.key === 'Enter' && e.target.value.trim()) startQuiz(); });
    startBtn.addEventListener('click', startQuiz);
  }
});
