import Ember from 'ember';
import LoginRedirect from 'osf-meetings/mixins/login-redirect';

export default Ember.Route.extend(LoginRedirect, {
    model() {
        return this.store.createRecord('node', {
            conference: this.modelFor('conference.index'),
        });
    },
    deactivate: function() {
        var controller = this.get('controller');
        controller.send('killSubmission');
        controller.set('kill',true);
        controller.set('displayErrors',false);
    },
    actions: {
        cancelSubmission() {
            let conferenceModel = this.modelFor('conference.index');
            this.transitionTo('conference.index.index', conferenceModel.id);
        }
    }
});
