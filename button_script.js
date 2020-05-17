var clicks = 0;

function clickCounter() {
    // increment the click variable by 2 everytime the button is pressed
    clicks += 2;
    // Caps the counter at 20 as there are 20 rakaats in taraweeh
    if (clicks > 20) {
        clicks = 20;
    }
    // i assume this assigns the clicks variable to a tag named clicks   
    document.getElementById("clicks").innerHTML = clicks;
};

function resetCounter(){
    // resets the counter when the button is pressed
    clicks = 0;
    // updates the click variable on the browser
    document.getElementById("clicks").innerHTML = clicks;
}

