## Overview
Script that will extract emotion css in js definitions and put them into a css module.

It will remove the emotion declartions, allow you to rename classes, add an import for the css module and update the class names to use the css module definitions.

It currently doesn't remove emotion imports, or update any JS variables in the CSS.  


## Installation

The `./install.sh` script will copy it to your home bin folder making it runnable anywhere, assuming you have the home bin directory set up. 

## Usage
If install using the `./install.sh` script you should be able to run `js-to-css` 

To convert a JS file navigate to where its located and run `js-to-css -f ./MyComponent.js`. It will prompt you to rename any classes its find, you can leave it empty if you do not want to rename it (untested).

It should generate `MyComponent.module.css` and `MyComponent_updated.js`

If you're happy with the changes in `MyComponent_updated.js` then `mv MyComponent_updated.js MyComponent.js`, but remember you'll still have to update any js variables in the CSS and update the emotion imports, particularly to switch to using `classnames` if the component has conditional classes.  


