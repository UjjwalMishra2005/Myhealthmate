document.addEventListener("DOMContentLoaded", function () {
  const meta = document.querySelector('meta[name="csrf-token"]');
  if (meta) {
    document.body.addEventListener('htmx:configRequest', (event) => {
      event.detail.headers['X-CSRFToken'] = meta.content;
    });
  }
});
