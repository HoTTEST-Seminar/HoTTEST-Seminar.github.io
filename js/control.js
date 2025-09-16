// Accordion animation
var acc = document.getElementsByClassName('accordion');
var i;
for (i = 0; i < acc.length; i++) {
  acc[i].addEventListener('click', function() {
    this.classList.toggle('active');
    var panel = this.nextElementSibling;
    if (panel.style.maxHeight) {
      panel.style.maxHeight = null;
    } else {
      panel.style.maxHeight = panel.scrollHeight + 'px';
    } 
  });
}

// Show More/Less abstracts functionality
document.querySelectorAll('.panel table').forEach(function(table) {
  // For each row except the header
  table.querySelectorAll('tr').forEach(function(row, idx) {
    // Skip header row
    if (idx === 0) return;
    let cells = row.querySelectorAll('td');
    if (cells.length === 0) return;
    let lastCell = cells[cells.length - 1];
    if (!lastCell.classList.contains('show-more-processed')) {
        lastCell.classList.add('show-more-processed');
        let abst = lastCell.querySelector('.abstract');
        // Make title into a button
        let btn = lastCell.querySelector('.talk-title')
        let img = new Image(10, 10);
        img.src = 'images/expand-button.png';
        img.style.marginInlineEnd = '5px';
        btn.insertAdjacentElement('afterbegin', img);
        btn.addEventListener('click', function() {
          let expanded = abst.classList.toggle('expanded');
          img.src = expanded ? 'images/retract-button.png' : 'images/expand-button.png';
          // Update panel height if inside accordion
          let panel = lastCell.closest('.panel');
          if (panel) {
              requestAnimationFrame(function() {
                  panel.style.maxHeight = panel.scrollHeight + "px";
              });
            }
        });
    }
    });
});

// Stops icons from expanding abstract
function stopEvent(event) { event.stopPropagation(); }
document.querySelectorAll('.icon').forEach(function(icon) {
  icon.addEventListener('click', stopEvent, false);
});

// Opens first accordion on start
var firstPanel = document.getElementsByClassName('panel')[0];
firstPanel.style.maxHeight = firstPanel.scrollHeight + 'px';
document.getElementsByClassName('accordion')[0].classList.toggle('active');

// Opens first 'Show More' button on start
var firstBtn = document.querySelector('.talk-title');
if (firstBtn) {
    var abst = document.querySelector('.abstract');
    if (abst && abst.classList) {
        abst.classList.add('expanded');
        firstBtn.childNodes[0].src = 'images/retract-button.png';
        // Update panel height if inside accordion
        let panel = firstBtn.closest('.panel');
        if (panel) {
            requestAnimationFrame(function() {
                panel.style.maxHeight = panel.scrollHeight + "px";
            });
        }
    }
}

// "Expand Terms" button functionality
document.getElementById('expand-term-btn').addEventListener('click', function() {
  for (i = 0; i < acc.length; i++) {
    if (!acc[i].classList.contains('active')) {
      var accPanel = acc[i].nextElementSibling;
      accPanel.style.maxHeight = accPanel.scrollHeight + 'px';
      acc[i].classList.toggle('active');
    }
  }
});

// "Expand Abstracts" button functionality
document.getElementById('expand-abst-btn').addEventListener('click', function() {
  for (i = 0; i < acc.length; i++) {
    if (!acc[i].classList.contains('active')) {
      var accPanel = acc[i].nextElementSibling;
      accPanel.style.maxHeight = accPanel.scrollHeight + 'px';
      acc[i].classList.toggle('active');
    }
  }
  document.querySelectorAll('.talk-title').forEach((title) => {
    var abst = title.nextSibling.nextSibling;
    if (abst && abst.classList) {
      abst.classList.add('expanded');
      title.childNodes[0].src = 'images/retract-button.png';
      // Update panel height if inside accordion
      let panel = title.closest('.panel');
      if (panel) {
          requestAnimationFrame(function() {
              panel.style.maxHeight = panel.scrollHeight + "px";
          });
      }
    }
  });
});

// Sets all links to "noreferrer"
document.querySelectorAll('a').forEach((el) => {
    el.setAttribute('rel', 'noreferrer');
});
