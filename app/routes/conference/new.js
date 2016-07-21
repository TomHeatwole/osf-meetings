import Ember from 'ember';
import CheckLoginMixin from 'osf-meetings/mixins/check-login-mixin';
import config from '../../config/environment';


export default Ember.Route.extend(CheckLoginMixin, {
    model() {
        return Ember.RSVP.hash({
            meta : Ember.$.ajax({
<<<<<<< HEAD
                url : "http://localhost:8000/conferences/",
                type : "OPTIONS",
                xhrFields : {
                    withCredentials : true
                },
                crossDomain : true
=======
                url : config.meetingsUrl + "/conferences/",
                type : "OPTIONS"
>>>>>>> cb7e5d34aa161ab329f7fcedcbe5f511bbb34266
            }),
            newConf : this.store.createRecord('conference')
        });
    },
//    deactivate: function() {
//        var controller = this.get('controller');
//        controller.send('killConference');
//        controller.set('kill',true);
//        controller.set('displayErrors',false);
//    },
    actions: {
        back() {
            this.transitionTo('index').then(function(newRoute) {
                newRoute.controller.set('visited', true);
            });
        },
        saveConference(newConf) {
            var router = this;
            newConf.save().then(function(params) {
                router.transitionTo('conference.index', params.id);
            });
        }
    }
});
