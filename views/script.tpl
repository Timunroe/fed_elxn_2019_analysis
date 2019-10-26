const data_init = {
    // if no other content picaTargetClass: '#div1785 div, #div3511 div, #div4680 div',
    // of if content ... picaTargetClass: '#div1786 div, #div3795 div, #div4681 div',
	// otherwise, it's '.pica-target' for manual insertion
    picaTargetClass: '.pica-target',
	picaTestClass: 'pica-results',
};

const url = 'https://thespec.net/dataviz/{{site}}.json';

// FETCH DATA
function fetch_data(url, data) {
	fetch(url)
  .then(function(response) {
    return response.json();
  })
  .then(function(results) {
		var the_HTML = results["html"];
	  applyTemplate(the_HTML, data.picaTargetClass);
  });
}											 

// INSERT HTML
function applyTemplate(html_string, targetClass) {
	var targets = document.querySelectorAll(targetClass);
	// apply template results to target elements
	targets.forEach(function(el, i) {
		el.innerHTML = html_string;
	});
    var acc = document.getElementsByClassName("pica-accordion");
    var i;
    for (i = 0; i < acc.length; i++) {
        acc[i].addEventListener("click", function() {
            /* Toggle between adding and removing the "active" class,
            to highlight the button that controls the panel */
            this.classList.toggle("pica-active");
    
            /* Toggle between hiding and showing the active panel */
            var panel = this.nextElementSibling;
            if (panel.style.display === "block") {
                panel.style.display = "none";
            } else {
                panel.style.display = "block";
            }
        });
    }
    var defaults = document.querySelectorAll('.pica-accordion')
    Array.prototype.forEach.call(defaults, function(el, i) {
        el.click();
    });
}

// MAIN START							 											 
var matches = document.querySelectorAll("."+ data_init.picaTestClass);
if (matches.length == 0) { // RUN CHECK
  
  var pica_add = (function() {
    var executed = false;
    return function() {
      if (!executed) {
        if (document.getElementById("pica-style") === null) {
            executed = true;
            var css = '.pica-table{font-size:14px;width:100%;padding-top:8px;padding-bottom:8px;border-collapse:collapse;border-spacing:0;font-family:-apple-system,BlinkMacSystemFont,"avenir next",avenir,"helvetica neue",helvetica,ubuntu,roboto,noto,"segoe ui",arial,sans-serif}.pica-table thead tr th{font-weight:600;text-transform:uppercase;padding-top:8px;padding-bottom:8px;padding-right:12px;color:grey;border-bottom:1px solid #c7c7c7}.pica-table tbody tr td{padding-top:8px;padding-bottom:8px;padding-right:12px;border-bottom:1px solid #c7c7c7}.pica-accordion,.pica-accordion-burl,.pica-accordion-ham{background-color:#eee;color:#444;cursor:pointer;padding:18px;width:100%;text-align:left;border:none;outline:0;transition:.4s}.pica-accordion-burl:hover,.pica-accordion-ham:hover,.pica-accordion:hover,.pica-active{background-color:#ccc}.pica-panel{background-color:#fff;display:none;overflow:hidden}button.pica-accordion-burl:after,button.pica-accordion-ham:after,button.pica-accordion:after{content:"+";color:#777;font-weight:700;float:right;margin-left:5px}button.pica-accordion-burl.pica-active:after,button.pica-accordion-ham.pica-active:after,button.pica-accordion.pica-active:after{content:"-"}.striped--light-gray:nth-child(odd){background-color:#dcdcdc}'
              head = document.head || document.getElementsByTagName('head')[0],
              style = document.createElement('style');
            style.setAttribute('id', 'pica-style');
            style.type = 'text/css';
            if (style.styleSheet){
              style.styleSheet.cssText = css;
            } else {
              style.appendChild(document.createTextNode(css));
            }
            head.appendChild(style);
          }
        }
    };
})();
  pica_add();
	fetch_data(url, data_init);
} else { // END RUN CHECK
	console.log("Already done");
}
