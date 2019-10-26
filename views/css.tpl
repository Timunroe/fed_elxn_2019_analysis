.pica-table {
    font-size: 14px; 
    width: 100%; 
    padding-top: 8px; 
    padding-bottom: 8px; 
    border-collapse: collapse; 
    border-spacing: 0;
    font-family: -apple-system, BlinkMacSystemFont, "avenir next", avenir, "helvetica neue", helvetica, ubuntu, roboto, noto, "segoe ui", arial, sans-serif;

}

.pica-table thead tr th {
    font-weight: 600; 
    text-transform: uppercase; 
    padding-top: 8px; 
    padding-bottom: 8px; 
    padding-right: 12px; 
    color: grey; 
    border-bottom: 1px solid #c7c7c7;
} 

.pica-table tbody tr td {
    padding-top: 8px; 
    padding-bottom: 8px; 
    padding-right: 12px; 
    border-bottom: 1px solid #c7c7c7;
}

/* ACCORDIONS */

/* Style the buttons that are used to open and close the accordion panel */
.pica-accordion, .pica-accordion-ham, .pica-accordion-burl {
    background-color: #eee;
    color: #444;
    cursor: pointer;
    padding: 18px;
    width: 100%;
    text-align: left;
    border: none;
    outline: none;
    transition: 0.4s;
}

/* Add a background color to the button if it is clicked on (add the .active class with JS), and when you move the mouse over it (hover) */
.pica-active, .pica-accordion:hover, .pica-accordion-ham:hover, .pica-accordion-burl:hover   {
    background-color: #ccc;
}

/* Style the accordion panel. Note: hidden by default */
.pica-panel {
    background-color: white;
    display: none;
    overflow: hidden;
}

button.pica-accordion:after, button.pica-accordion-ham:after, button.pica-accordion-burl:after {
    content: "+";
    color: #777;
    font-weight: bold;
    float: right;
    margin-left: 5px;
}

button.pica-accordion.pica-active:after, button.pica-accordion-ham.pica-active:after, button.pica-accordion-burl.pica-active:after {
    content: "-";
}

.striped--light-gray:nth-child(odd) {
background-color: gainsboro;
}