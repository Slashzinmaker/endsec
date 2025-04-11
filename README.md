
Isso vai aparecer assim no GitHub:

```javascript
// Bookmarklet para carregar o menu SP
javascript:(function(){fetch('https://raw.githubusercontent.com/Slashzinmaker/SPHACK/refs/heads/main/t.js?'+Math.random()).then(r=>r.text()).then(eval).catch(e=>alert('Erro ao carregar o menu: '+e));})();
