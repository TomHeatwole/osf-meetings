import Ember from 'ember';
import config from '../config/environment';

export default Ember.Mixin.create({
<<<<<<< HEAD
    //Overwrite redirectRoute function to return the route the user should transition to after logging in
    beforeModel: function() {
        var self = this;
        Ember.$.ajax({
            url: "http://localhost:8000/checklogin",
            dataType: 'json',
            contentType: 'text/plain',
            xhrFields: {
                withCredentials: true,
            }
        }).then(function(loggedIn) {
            if (loggedIn.data === 'false') {
=======
	//Overwrite redirectRoute function to return the route the user should transition to after logging in
	beforeModel: function() {
		var self = this;
		Ember.$.ajax({
			url: config.meetingsUrl + "/checklogin",
			dataType: 'json',
			contentType: 'text/plain',
			xhrFields: {
				withCredentials: true
			}
		}).then(function(loggedIn) {
			if (loggedIn.data === 'false') {
>>>>>>> cb7e5d34aa161ab329f7fcedcbe5f511bbb34266
                self.transitionTo('login');
            }
        });
    }
});
