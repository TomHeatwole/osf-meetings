import Ember from 'ember';


// This mixin should be added to all routes that a user must be logged in to an OSF account to view.
// Because it uses the activate function, it must be added to the ROUTE and not the controller.

export default Ember.Mixin.create({
	activate: function() {
		var loggedIn = false;
		// This may look like a total hack, but it's the reccomended way to interact with a cookie from a javascript file
		var nameEQ = "sessionid=";
    	var ca = document.cookie.split(';');
    	for(var i=0;i < ca.length;i++) {
	        var c = ca[i];
	        while (c.charAt(0)==' ') c = c.substring(1,c.length);
	        console.log( c.substring(nameEQ.length,c.length));
	        	if (c.indexOf(nameEQ) == 0) {
	        		//The following line will return the actual session ID if necessary in future developing
	        		// var sessionid = c.substring(nameEQ.length,c.length);
	        		loggedIn = true;
        		}

    	}
    	if (!loggedIn)
    		this.transitionTo('login');	
	}
});
