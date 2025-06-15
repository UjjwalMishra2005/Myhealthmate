  let intro = introJs();  // create ONE instance

//  intro.setOptions({
  //  steps: [
    //  { intro: "👋 Welcome to the site!" },
      //{ element: document.querySelector('#feature1'), intro: "Feature 1 explained." },
      //{ element: document.querySelector('#feature2'), intro: "Feature 2 explained." }
  //  ]
  //});

  // Attach event handlers to the correct instance
  let check = 'working';
  intro.onexit(function () {
    document.getElementById('skip-tutorial').style.display = 'none';
  });

  intro.oncomplete(function () {
    document.getElementById('skip-tutorial').style.display = 'none';
  });

  intro.start(); // start after event handlers are set

  // Other unrelated logic...
  const btn = document.getElementById('hamburger-btn');
  const menu = document.getElementById('hamburger-menu');

  btn.addEventListener('click', () => {
    btn.classList.toggle('open');
    menu.classList.toggle('hidden');
  });

  window.addEventListener('click', (e) => {
    if (!btn.contains(e.target) && !menu.contains(e.target)) {
      btn.classList.remove('open');
      menu.classList.add('hidden');
    }
  });

  // Skip Tutorial button manually
  function endTutorial() {
    intro.exit(); // use the same instance
    document.getElementById('skip-tutorial').style.display = 'none';
  }

  

  