const html = `<!doctype html><html lang="ru"><meta charset="utf-8"><title>AI Mode Router</title><body><main><h2>Рекомендация готова</h2><p id="mode">Проверьте выбранные настройки ChatGPT.</p><button data-action="выполняй">Подтвердить и выполнить</button><button data-action="подбери дешевле">Дешевле</button><button data-action="подбери надёжнее">Надёжнее</button></main><script>
document.querySelectorAll('[data-action]').forEach(button=>button.onclick=()=>parent.postMessage({jsonrpc:'2.0',method:'ui/message',params:{content:button.dataset.action}},'*'));
</script></body></html>`;

export default {
  async fetch(request) {
    const url = new URL(request.url);
    if (url.pathname === '/health') return new Response('ok');
    if (url.pathname === '/ui') return new Response(html, {headers:{'content-type':'text/html; charset=utf-8','content-security-policy':"default-src 'none'; script-src 'unsafe-inline'; style-src 'unsafe-inline'"}});
    return new Response('MCP endpoint will be enabled after deployment review.', {status: 404});
  }
};
